"""
Text preprocessing utilities for the Adaptive Taxonomy Mapper.

Responsibilities:
- Normalize text
- Remove noise
- Handle simple linguistic variation
- Remain fast and scalable for large datasets
"""

import re
from typing import Optional

# Regex compiled once for performance (important for large inputs)
CLEAN_REGEX = re.compile(r"[^a-z\s]+")

# Stopwords: remove low-information words
# (kept intentionally small for explainability)
STOPWORDS = {
    "the", "and", "to", "of", "in", "a", "is", "with", "for", "on", "at"
}

# Simple synonym normalization
# Helps with complex language while staying rule-based
SYNONYMS = {
    "attorney": "lawyer",
    "courtroom": "court",
    "judge": "court",
    "trial": "court",
    "ai": "artificial intelligence",
    "robots": "robot",
    "spies": "spy",
    "detectives": "detective"
}

# Main preprocessing function
def preprocess_text(text: Optional[str]) -> str:
    """
    Cleans and normalizes input text for genre inference.

    Steps:
    1. Lowercase conversion
    2. Remove punctuation & special characters
    3. Tokenize
    4. Remove stopwords
    5. Normalize simple synonyms

    This function is optimized for:
    - High throughput
    - Rule-based inference
    - Easy extensibility
    """

    if not text:
        return ""

    # Normalize case
    text = text.lower()

    # Remove punctuation and symbols
    text = CLEAN_REGEX.sub("", text)

    tokens = []
    for word in text.split():
        if word in STOPWORDS:
            continue
        tokens.append(SYNONYMS.get(word, word))

    return " ".join(tokens)
