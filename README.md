# Life & Health Insurance Business Analytics

A complete data analytics project focused on analyzing synthetic life and health insurance claims data. The project demonstrates a structured analytical workflow, from data acquisition and validation to exploratory data analysis, statistical summaries, and business insights.

---

# Project Overview

This project analyzes a synthetic insurance claims dataset to understand the distribution of claim amounts and evaluate whether demographic and socioeconomic characteristics are associated with differences in insurance claim severity.

Unlike a standalone notebook, this repository follows a modular project structure. Business logic is separated into reusable Python modules, making the analysis easier to maintain, extend, and test.

The repository demonstrates common practices used in data analytics projects, including:

- modular code organization
- reusable analytical functions
- data validation
- exploratory data analysis
- statistical summaries
- visualizations
- documentation
- testing

---

# Business Objective

The main objective is to explore factors that may influence insurance claim amounts.

The analysis focuses on answering questions such as:

- What is the distribution of insurance claim amounts?
- Are there missing values or data quality issues?
- Do claim amounts differ across demographic groups?
- Which customer characteristics appear to have stronger relationships with claim severity?
- What limitations should be considered before drawing conclusions?

---

# Dataset

The project uses a synthetic Life & Health Insurance Claims dataset.

Dataset characteristics:

- 13,000 observations
- 7 variables
- No missing values
- No duplicate records

## Variables

| Variable | Description |
|-----------|-------------|
| Age | Customer age |
| Gender | Customer gender |
| Income | Annual income |
| Marital_Status | Marital status |
| Education | Education level |
| Occupation | Occupation category |
| Claim_Amount | Insurance claim amount |

---

# Analytical Scope

This project focuses on descriptive analytics.

Specifically, the analysis investigates:

- claim amount distributions
- customer demographics
- socioeconomic characteristics
- statistical summaries
- visual exploration
- group comparisons

The project does **not** evaluate:

- claim frequency
- underwriting decisions
- insurance pricing
- customer lifetime value
- fraud detection
- predictive modeling

These topics require additional information that is not available in the dataset.

---

# Project Workflow

The analytical workflow follows these stages:

1. Download the dataset
2. Load the data
3. Validate data quality
4. Explore the dataset
5. Produce descriptive statistics
6. Generate visualizations
7. Compare customer groups
8. Interpret findings
9. Document limitations
10. Suggest future improvements

---

# Project Structure

```text
.
├── data/
│   ├── raw/
│   └── processed/
│
├── docs/
│   ├── methodology.md
│   └── data_dictionary.md
│
├── notebooks/
│   ├── insurance_claims_analysis.ipynb
│
├── reports/
│   └── figures/
│
├── src/
│   ├── __init__.py
│   ├── config.py
│   ├── data_loader.py
│   ├── validation.py
│   ├── statistics.py
│   └── visualization.py
│
├── tests/
│
├── pyproject.toml
├── uv.lock
├── README.md
└── .gitignore
```

---

# Technologies

- Python
- pandas
- matplotlib
- Jupyter Notebook
- KaggleHub
- pytest
- uv

---

# Features

- Modular Python architecture
- Reusable analytical functions
- Data quality validation
- Descriptive statistics
- Automated visualizations
- Exploratory Data Analysis (EDA)
- Statistical summaries by customer groups
- Clean project organization
- Jupyter Notebook workflow
- Unit testing support

---

# Installation

Clone the repository:

```bash
git clone https://github.com/YOUR_USERNAME/life-health-insurance-business-analytics.git

cd life-health-insurance-business-analytics
```

Install dependencies:

```bash
uv sync
```

---

# Running the Analysis

Launch Jupyter Notebook:

```bash
uv run jupyter notebook
```

Open:

```text
notebooks/insurance_claims_analysis.ipynb
```

Run all notebook cells from top to bottom.

---

# Running Tests

```bash
uv run pytest
```

---

# Main Findings

The exploratory analysis indicates that:

- The dataset contains no missing values.
- No duplicate records were identified.
- Claim amounts are positively skewed.
- A relatively small number of large claims influence the overall distribution.
- Gender shows only minor differences in claim severity.
- Marital status has limited impact on average claim amounts.
- Education level demonstrates only small variations.
- Occupation exhibits greater variability, although category imbalance limits reliable comparisons.

Overall, demographic characteristics alone do not strongly explain differences in insurance claim amounts.

---

# Limitations

Several limitations should be considered:

- The dataset is synthetic.
- No customer identifiers are available.
- No policy information is included.
- Coverage limits are unavailable.
- Premium information is unavailable.
- Claim history is unavailable.
- Time-series analysis cannot be performed.
- The analysis is descriptive rather than predictive.

---

# Future Improvements

Potential future enhancements include:

- Predictive modeling for claim severity
- Machine learning models
- Statistical hypothesis testing
- Correlation heatmaps
- Interactive dashboards
- Feature engineering
- Automated reporting
- CI/CD integration
- Expanded unit test coverage

---

# Documentation

Additional documentation is provided in the `docs` directory:

- `methodology.md`
- `data_dictionary.md`

---

# License

This project is intended for educational purposes and portfolio demonstration.

The dataset remains subject to its original license and distribution terms.