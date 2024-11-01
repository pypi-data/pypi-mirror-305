# Sanskrit Processor

A Python package for processing Sanskrit text using the Dharmamitra API.

## Installation

```bash
pip install dharmamitra-sanskrit-grammar
```

## Usage

```python
from dharmamitra_sanskrit_grammar import DharmamitraSanskritProcessor

# Initialize the processor
processor = DharmamitraSanskritProcessor()

# Process a batch of sentences
sentences = [
    "your first sanskrit sentence",
    "your second sanskrit sentence"
]

# Using different modes
results = processor.process_batch(
    sentences,
    mode="lemma",  # or 'unsandhied' or 'unsandhied-lemma-morphosyntax'
    human_readable_tags=True
)
```

## Available Modes

- `lemma`: Basic lemmatization
- `unsandhied`: Word segmentation only
- `unsandhied-lemma-morphosyntax`: Full analysis with word segmentation, lemmatization, and morphosyntax

## License

This project is licensed under the MIT License - see the LICENSE file for details.