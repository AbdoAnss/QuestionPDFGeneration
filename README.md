# Question PDF Extractor

## Project Description
A Python tool for extracting questions from text and generating professional PDFs.

## Prerequisites
- Python 3.8+
- wkhtmltopdf installed

## Installation

1. Clone the repository
```bash
git clone https://your-repo-url/QuestionPDFGenerator.git
cd QuestionPDFGenerator
```

2. Create and activate virtual environment
```bash
python3 -m venv .venv
source .venv/bin/activate  # On Windows use .venv\Scripts\activate
```

3. Install dependencies
```bash
pip install -r requirements.txt
# Or if using Poetry
poetry install
```

4. Install wkhtmltopdf
- Ubuntu/Debian: `sudo apt-get install wkhtmltopdf`
- macOS (Homebrew): `brew install wkhtmltopdf`
- Windows: Download from https://wkhtmltopdf.org/downloads.html

## Usage
```bash
# Run the entire extraction and PDF generation process
python run.py

# Or use individual scripts
python -m src.text_extraction
python -m src.pdf_generation
```

## Development
- Run tests: `pytest`
- Format code: `black .`
- Lint code: `flake8`


