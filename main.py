"""
Main execution script for the Adaptive Taxonomy Mapper.

Responsibilities:
- Load taxonomy and input data
- Invoke inference engine
- Store structured results
- Generate reasoning logs

This file contains NO inference or preprocessing logic.
"""

import json
from mapper.loader import load_json, load_json_stream
from mapper.inference_engine import infer_genre


def process_case(case, taxonomy):
    """
    Process a single test case using the inference engine.
    """
    case_id = case.get("id")
    tags = case.get("tags", [])
    blurb = case.get("blurb", "")

    mapped_genre, reasoning = infer_genre(tags, blurb, taxonomy)

    result = {
        "case_id": case_id,
        "mapped_genre": mapped_genre,
        "reasoning": reasoning
    }

    log_entry = f"Case {case_id}: {mapped_genre} -> {reasoning}"
    return result, log_entry


def main():
    # Load taxonomy (small & static, safe to load fully)
    taxonomy = load_json("data/taxonomy.json")

    results = []
    reasoning_log = []

    # Load test cases (supports scalability)
    test_cases_path = "data/test_cases.json"

    try:
        # Default: load normally
        test_cases = load_json(test_cases_path)
        iterator = test_cases
    except RuntimeError:
        # Fallback: stream large datasets
        iterator = load_json_stream(test_cases_path)

    # Process each case
    for case in iterator:
        if not isinstance(case, dict):
            continue  # Skip malformed records safely

        result, log_entry = process_case(case, taxonomy)
        results.append(result)
        reasoning_log.append(log_entry)

    # Write outputs
    with open("output/results.json", "w", encoding="utf-8") as f:
        json.dump(results, f, indent=2)

    with open("reasoning_log.txt", "w", encoding="utf-8") as f:
        f.write("\n".join(reasoning_log))

    print("Adaptive Taxonomy Mapping completed successfully.")


if __name__ == "__main__":
    main()
