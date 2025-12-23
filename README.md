Adaptive Taxonomy Mapper – Project Description

The Adaptive Taxonomy Mapper is a rule-based inference system developed to map noisy, user-generated tags and story descriptions to a predefined internal taxonomy. In real-world platforms, users often tag content with vague or misleading labels such as “Love” or “Action,” which are insufficient for accurate recommendation systems. This project addresses that problem by inferring precise sub-genres using story context rather than relying solely on user tags.

The system is designed to be scalable, explainable, and deterministic, ensuring that every classification decision can be clearly justified.

Problem Addressed

User-generated content suffers from poor-quality tagging. These tags are often:

Too generic

Incorrect

Incomplete

Contextually misleading

The objective of this project is to transform such noisy inputs into accurate, high-precision taxonomy labels while respecting the structure of the provided taxonomy and avoiding forced or incorrect mappings.

Core Rules Followed

Context Wins Rule
The story description (blurb) is given higher priority than user tags. If there is a conflict between the tag and the actual content, the system follows the content.

Honesty Rule
If a story does not fit any category in the taxonomy (for example, recipes or instructional content), the system does not force a classification and instead returns [UNMAPPED].

Hierarchy Rule
All predicted sub-genres must exist in the provided taxonomy. The system never generates or assumes new categories.

Project Structure Explanation

data/
Contains the taxonomy definition and test cases.

mapper/
Contains the core logic of the system:

loader.py for loading data safely and scalably

text_utils.py for text preprocessing and normalization

inference_engine.py for genre inference logic

main.py
Acts as the pipeline controller that connects all components, processes inputs, and generates outputs.

output/results.json
Stores the final inferred genres with reasoning.

reasoning_log.txt
Stores human-readable explanations for each inference.

System Working Flow

User tags and story blurb are taken as input

Text is preprocessed and normalized

Non-fiction or instructional content is detected

Strong keyword matching is applied

Semantic concept matching is applied to handle abstract or metaphorical expressions

The predicted genre is validated against the taxonomy

The final genre or [UNMAPPED] is returned with reasoning

Handling of Complexity

The system is capable of handling:

Large volumes of input data

Noisy and misleading user tags

Contextual ambiguity

Metaphorical expressions such as “a battle of minds in the courtroom”

Strict taxonomy validation without hallucination

The system intentionally avoids heavy machine learning or LLM-based reasoning to maintain explainability, speed, and deterministic behavior.

Output Explanation

For each input case, the system produces:

The mapped sub-genre (or [UNMAPPED])

A short reasoning explaining why that genre was chosen

This reasoning is stored both in structured JSON format and in a readable log file.

How to Run the Project

The project can be executed by running the following command from the project root directory:

python main.py
