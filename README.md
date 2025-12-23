# Adaptive Taxonomy Mapper

## Overview
The Adaptive Taxonomy Mapper is a rule-based inference system designed to map noisy, user-generated tags and story descriptions to a structured internal taxonomy.  
It addresses the common issue where users provide vague or misleading tags (e.g., “Love”, “Action”), while recommendation systems require precise, high-quality genre labels.

The system prioritizes **story context over user tags**, ensures **honest classification**, and provides **clear reasoning** for every mapping decision.

---

## Problem Statement
User-generated content is often poorly tagged, making it difficult for recommendation engines to function effectively.  
The goal of this project is to build an inference engine that:

- Infers accurate sub-genres from messy input
- Avoids forcing incorrect classifications
- Respects a predefined taxonomy hierarchy
- Explains *why* a particular genre was chosen

---

## Design Rules Implemented

### 1. Context Wins Rule
The story description (blurb) takes priority over user-provided tags.  
If tags conflict with the actual story context, the system follows the context.

### 2. Honesty Rule
If a story does not fit any category in the taxonomy (e.g., recipes, tutorials, instructional content), the system returns:


### 3. Hierarchy Rule
All predictions must strictly exist within the provided taxonomy.  
The system never invents or hallucinates new genres.

---

## Project Structure

adaptive_taxonomy_mapper/
│
├── data/
│ ├── taxonomy.json
│ └── test_cases.json
│
├── mapper/
│ ├── init.py
│ ├── loader.py
│ ├── text_utils.py
│ ├── inference_engine.py
│
├── output/
│ └── results.json
│
├── main.py
├── reasoning_log.txt
└── README.md


---

## System Workflow

User Tags + Story Blurb
↓
Text Preprocessing
↓
Non-Fiction Detection
↓
Keyword Matching
↓
Semantic Concept Matching
↓
Taxonomy Validation
↓
Final Genre or [UNMAPPED]


---

## Core Components

### `loader.py`
- Safely loads JSON data
- Includes a scalable, generator-based loader for large datasets
- Provides clear error handling

### `text_utils.py`
- Normalizes and cleans text
- Removes stopwords
- Handles basic synonym normalization
- Optimized for large-scale input processing

### `inference_engine.py`
- Core reasoning engine
- Uses:
  - Strong keyword signals
  - Semantic concept matching (handles metaphor-like expressions)
  - Context-over-tag logic
- Prevents hallucinations by validating outputs against the taxonomy

### `main.py`
- Orchestrates the entire pipeline
- Loads data
- Calls the inference engine
- Writes structured outputs and reasoning logs

---

## Handling Complexity

### What the System Handles
- Large input volumes (scalable design)
- Noisy and misleading tags
- Contextual ambiguity
- Metaphorical expressions (e.g., “battle of minds in the courtroom”)
- Strict taxonomy enforcement
- Explainable and deterministic decisions

### What the System Does Not Handle (By Design)
- Deep semantic reasoning using machine learning or LLMs
- Sarcasm or meaning without textual cues

This design choice ensures speed, explainability, and low operational cost.

---

## Example Output

### `results.json`
```json
{
  "case_id": 5,
  "mapped_genre": "Legal Thriller",
  "reasoning": "Semantic concept 'battle of minds' suggests Legal Thriller."
}


How to Run the Project
Requirements

Python 3.8 or higher

Command
python main.py

Output Files Generated

output/results.json

reasoning_log.txt

Scalability Considerations

Linear-time text processing

Generator-based loading for large datasets

Modular design allows easy extension to:

Embedding-based similarity

Hybrid rule + ML inference

LLM-assisted fallback systems

Design Philosophy

The system prioritizes:

Explainability over black-box accuracy

Deterministic behavior over probabilistic guessing

Maintainability and scalability over unnecessary complexity

The architecture mirrors real-world content classification and recommendation pipelines.

Future Enhancements

Confidence scoring for predictions

TF-IDF or embedding-based similarity

Multilingual support

Hybrid LLM-assisted inference

Conclusion

The Adaptive Taxonomy Mapper demonstrates a scalable, honest, and explainable approach to transforming noisy user-generated inputs into high-quality taxonomy labels.
It balances accuracy, transparency, and system design principles suitable for real-world deployment.
