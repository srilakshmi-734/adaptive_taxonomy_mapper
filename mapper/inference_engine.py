"""
Advanced inference engine for Adaptive Taxonomy Mapper.

Capabilities:
- Context-first reasoning
- Keyword + semantic concept matching
- Handles metaphor-like expressions
- Scalable and explainable
- Strict taxonomy validation (no hallucinations)
"""

from typing import Dict, Tuple
from mapper.text_utils import preprocess_text


# 1. STRONG KEYWORD SIGNALS (Exact, high confidence)
KEYWORD_SIGNALS = {
    "Legal Thriller": [
        "lawyer", "judge", "court", "trial", "cross examination", "verdict"
    ],
    "Espionage": [
        "spy", "agent", "mission", "covert", "kremlin", "intelligence"
    ],
    "Cyberpunk": [
        "neon", "artificial intelligence", "cyber", "tokyo", "megacity"
    ],
    "Hard Sci-Fi": [
        "physics", "ftl", "stasis", "theoretical", "quantum"
    ],
    "Slasher": [
        "killer", "masked", "stalks", "camp", "bloodshed"
    ],
    "Gothic": [
        "victorian", "mansion", "ancestral", "corridor", "decay"
    ],
    "Psychological": [
        "paranoia", "obsession", "delusion", "unreliable"
    ],
    "Enemies-to-Lovers": [
        "hate", "hated", "enemy", "rival", "rivals"
    ],
    "Second Chance": [
        "reunited", "years later", "met again", "after years"
    ]
}


# 2. SEMANTIC CONCEPT SIGNALS (Handles metaphors & abstraction)
CONCEPT_SIGNALS = {
    "Legal Thriller": {
        "domains": [
            "courtroom", "justice system", "legal arena"
        ],
        "conflicts": [
            "battle of minds", "war of arguments",
            "intellectual battle", "verbal duel"
        ]
    },
    "Psychological": {
        "conflicts": [
            "mind game", "mental struggle", "psychological warfare"
        ],
        "states": [
            "inner turmoil", "fractured mind"
        ]
    },
    "Espionage": {
        "conflicts": [
            "shadow war", "silent war", "covert struggle"
        ]
    }
}


# 3. NON-FICTION / INSTRUCTIONAL DETECTION (Honesty Rule)
NON_FICTION_SIGNALS = {
    "how to", "step by step", "build", "recipe",
    "mix", "bake", "instructions", "guide", "tutorial"
}


# 4. MAIN INFERENCE FUNCTION
def infer_genre(
    tags: list,
    blurb: str,
    taxonomy: Dict
) -> Tuple[str, str]:
    """
    Infers the best matching sub-genre for a story.
    Returns:
        (mapped_genre, reasoning)
    """

    clean_text = preprocess_text(blurb)


    # STEP 1: Honesty rule (non-fiction)
    for phrase in NON_FICTION_SIGNALS:
        if phrase in clean_text:
            return (
                "[UNMAPPED]",
                "Detected instructional or non-fiction content."
            )

    # STEP 2: Strong keyword match (highest confidence)
    for genre, keywords in KEYWORD_SIGNALS.items():
        for kw in keywords:
            if kw in clean_text and _exists_in_taxonomy(genre, taxonomy):
                return (
                    genre,
                    f"Strong keyword '{kw}' indicates {genre}."
                )

    # STEP 3: Semantic concept matching (FIXES METAPHORS )
    for genre, concept_groups in CONCEPT_SIGNALS.items():
        for _, phrases in concept_groups.items():
            for phrase in phrases:
                if phrase in clean_text and _exists_in_taxonomy(genre, taxonomy):
                    return (
                        genre,
                        f"Semantic concept '{phrase}' suggests {genre}."
                    )

    # STEP 4: Weak tag-based fallback (last resort)
    tag_text = " ".join(tags).lower()
    for genre in KEYWORD_SIGNALS:
        if genre.lower() in tag_text and _exists_in_taxonomy(genre, taxonomy):
            return (
                genre,
                "Inferred from weak tag signal due to lack of context."
            )

    # STEP 5: Final honesty fallback
    return (
        "[UNMAPPED]",
        "No sufficient keyword or semantic evidence found."
    )


# 5. TAXONOMY VALIDATION (ANTI-HALLUCINATION)
def _exists_in_taxonomy(subgenre: str, taxonomy: Dict) -> bool:
    """
    Ensures predicted sub-genre exists in taxonomy.
    Prevents hallucinated outputs.
    """
    for category in taxonomy.values():
        for genre_data in category.values():
            if isinstance(genre_data, list) and subgenre in genre_data:
                return True
            if isinstance(genre_data, dict):
                if subgenre in genre_data.get("subgenres", []):
                    return True
    return False
