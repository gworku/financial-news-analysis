# Financial News Sentiment Analysis

This project analyzes financial news sentiment and its impact on stock market trends using NLP and technical indicators.

---

## Installation Instructions

1. Clone the repository:
   ```bash
   git clone https://github.com/gworku/financial-news-analysis.git
   cd financial-news-analysis
(Optional) Create and activate a Python virtual environment:

bash
Copy
Edit
python -m venv venv
source venv/bin/activate       # On Linux/macOS
venv\Scripts\activate          # On Windows
Install the required packages:

bash
Copy
Edit
pip install -r requirements.txt
How to Run the Code
Run the main analysis script (adjust the filename if different):

bash
Copy
Edit
python src/main.py
Or, run individual modules or notebooks as needed:

For data processing:

bash
Copy
Edit
python src/data_processing.py
For sentiment analysis:

bash
Copy
Edit
python src/sentiment_analysis.py
To open and run Jupyter notebooks:

bash
Copy
Edit
jupyter notebook notebooks/analysis.ipynb
How to Run Tests
Tests are located in the tests/ directory and use pytest.

Run all tests with:

bash
Copy
Edit
pytest tests/
You can also run tests with detailed output:

bash
Copy
Edit
pytest -v tests/
Continuous Integration (CI)
This project uses GitHub Actions to run tests and code quality checks on every push and pull request.

You can view the latest workflow runs here:
GitHub Actions Workflow Results