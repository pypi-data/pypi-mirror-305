# Profanity Sanitizer

A simple sanitizer for offensive words with options to leverage machine learning for toxicity control
Caveat it that it's currently very slow
## Features

- Exact word matching against a list of banned words
- Fuzzy matching to catch misspellings and intentional obfuscation
- Semantic similarity checking to identify contextually similar offensive content and prevent false positives
- AI-based toxicity detection using pre-trained models
- Customizable word lists (banned and allowed words)
- Character replacement handling to catch common letter-to-number substitutions
- Adjustable thresholds for fuzzy matching, semantic similarity, and toxicity detection

## Installation

1. Install using pip:

```
pip install profanity-sanitizer
```

2. Install the required spaCy model:

```
python -m spacy download en_core_web_lg
```

## Usage

Here's a basic example of how to use the ProfanityFilter:

````

from profanity_sanitizer import ProfanitySanitizer
````

Initialize the filter

```
ps = ProfanitySanitizer()
```

Check some text

```
result = ps.check_text("This is a test sentence.")
print(result.is_clean) # True or False
print(result.reason) # Reason for the result
print(result.problematic_score) # 0-100 score indicating how problematic the text is
```

## Configuration

You can customize the ProfanityFilter by adjusting its parameters:

```
pf = ProfanitySanitizer(
    banned_words_file="path/to/custom_banned_words.json",
    allowed_words_file="path/to/custom_allowed_words.json",
    replacements_file="path/to/custom_replacements.json",
    use_fuzzy=True,
    fuzzy_threshold=80,
    use_ai=True,
    model_name="unitary/toxic-bert",
    use_semantic=True,
    similarity_threshold=0.8,
    toxicity_threshold=0.5,
    min_problematic_score_threshold=65
)
```

### Configuration Options

- `banned_words_file` (str): Path to a JSON file containing custom banned words.
- `allowed_words_file` (str): Path to a JSON file containing custom allowed words.
- `replacements_file` (str): Path to a JSON file containing custom character replacements.
- `use_fuzzy` (bool): Enable fuzzy matching for misspellings and obfuscation.
    - while flagging some intentionally misspelled words, it will also flag false positives, to prevent this you can
      tunr on use_semantic
    - for example 'fxck' will get flagged but 'duck' will also get flagged is use_semantic is off
- `fuzzy_threshold` (int): Similarity threshold for fuzzy matching (0-100).
- `use_ai` (bool): Enable AI-based toxicity detection.
    - This detects hateful strings that might be too annoying to put down to the banned_words
    - Strings like 'I want to hurt people' or 'I kill dogs' will get flagged

- `model_name` (str): Name of the pre-trained model for toxicity detection.
    - Only change this if you know what you're doing

- `use_semantic` (bool): Enable semantic similarity checking.
    - This uses spaCy semantic checking to prevent false positives, mostly used with fuzzy on,
- `similarity_threshold` (float): Threshold for semantic similarity (0.0-1.0).
- `toxicity_threshold` (float): Threshold for AI-based toxicity detection (0.0-1.0).
- `min_problematic_score_threshold` (int): Minimum score to consider text problematic (0-100).
