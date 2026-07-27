# Life & Health Insurance Business Analytics

> **Note:** This is a polished README template. Replace placeholder
> repository URLs if needed.

```{=html}
<p align="center">
```
`<img src="assets/hero.png" alt="Life & Health Insurance Business Analytics Hero Banner">`{=html}

```{=html}
</p>
```
```{=html}
<h1 align="center">
```
Life & Health Insurance Business Analytics

```{=html}
</h1>
```
```{=html}
<p align="center">
```
Business-oriented exploratory analysis of synthetic life and health
insurance claims using Python, pandas, Matplotlib, reusable analytical
modules, automated validation, and unit testing.

```{=html}
</p>
```
```{=html}
<p align="center">
```
`<img src="https://img.shields.io/badge/Python-3.12%2B-3776AB?logo=python&logoColor=white">`{=html}
`<img src="https://img.shields.io/badge/pandas-Data%20Analysis-150458?logo=pandas&logoColor=white">`{=html}
`<img src="https://img.shields.io/badge/Matplotlib-Visualization-11557C">`{=html}
`<img src="https://img.shields.io/badge/Jupyter-Notebook-F37626?logo=jupyter&logoColor=white">`{=html}
`<img src="https://img.shields.io/badge/pytest-6%20Tests%20Passing-0A9EDC?logo=pytest&logoColor=white">`{=html}
`<img src="https://img.shields.io/badge/Ruff-All%20Checks%20Passed-D7FF64?logo=ruff&logoColor=black">`{=html}
`<img src="https://img.shields.io/badge/uv-Package%20Management-DE5FE9">`{=html}

```{=html}
</p>
```

------------------------------------------------------------------------

## 📖 Overview

This project explores a synthetic life and health insurance claims
dataset to understand how claim amounts are distributed and whether
observable customer characteristics are associated with differences in
claim severity.

The project separates data loading, validation, statistical summaries,
and visualizations into reusable Python modules, creating a reproducible
analytics workflow that demonstrates both analytical thinking and
software engineering practices.

------------------------------------------------------------------------

## 🎯 Business Objective

The analysis investigates claim severity (`Claim_Amount`) by exploring
distribution patterns, data quality, and differences across demographic
and socioeconomic groups. It intentionally focuses on descriptive
analytics rather than predictive modeling.

------------------------------------------------------------------------

## ✨ Project Highlights

-   Modular Python architecture
-   Exploratory Data Analysis (EDA)
-   Automated data validation
-   Business-focused visualizations
-   Statistical summaries
-   Unit testing with `pytest`
-   Code quality with Ruff
-   Dependency management with `uv`

------------------------------------------------------------------------

## 📊 Dataset

  Metric                 Value
  ------------------- --------
  Records               13,000
  Variables                  7
  Missing Values             0
  Duplicate Records          0

Variables:

-   Age
-   Gender
-   Income
-   Marital_Status
-   Education
-   Occupation
-   Claim_Amount

------------------------------------------------------------------------

## 🔄 Project Workflow

``` mermaid
flowchart LR
    A[Source Dataset] --> B[Data Loading]
    B --> C[Validation]
    C --> D[EDA]
    D --> E[Statistics]
    E --> F[Visualizations]
    F --> G[Business Insights]
```

------------------------------------------------------------------------

## 📓 Notebook Preview

```{=html}
<p align="center">
```
`<img src="assets/notebook-preview.png" alt="Notebook Preview">`{=html}

```{=html}
</p>
```

------------------------------------------------------------------------

## 📈 Key Visualizations

```{=html}
<p align="center">
```
`<img src="assets/visualization-gallery.png" alt="Key Visualizations">`{=html}

```{=html}
</p>
```

------------------------------------------------------------------------

## 💼 Executive Summary

```{=html}
<p align="center">
```
`<img src="assets/executive-summary.png" alt="Executive Summary">`{=html}

```{=html}
</p>
```

------------------------------------------------------------------------

## 📊 Key Business Insights

-   No missing values or duplicate records.
-   Claim amounts are positively skewed.
-   Most claims are relatively small with a limited number of high-value
    outliers.
-   Occupation shows the largest observed variation.
-   Demographic variables alone provide limited explanatory power.

------------------------------------------------------------------------

## 🏗️ Project Architecture

  Module             Responsibility
  ------------------ -----------------------
  data_loader.py     Load dataset
  validation.py      Data quality checks
  statistics.py      Statistical summaries
  visualization.py   Charts
  config.py          Shared configuration

------------------------------------------------------------------------

## 🛠 Technology Stack

  Category          Technologies
  ----------------- --------------
  Language          Python
  Analysis          pandas
  Visualization     Matplotlib
  Notebook          Jupyter
  Testing           pytest
  Code Quality      Ruff
  Package Manager   uv

------------------------------------------------------------------------

## 🚀 Getting Started

``` bash
git clone https://github.com/YoniAfengar/life-health-insurance-business-analytics.git
cd life-health-insurance-business-analytics
uv sync
uv run jupyter notebook
```

Run tests:

``` bash
uv run pytest
```

Run static analysis:

``` bash
uv run ruff check .
```

------------------------------------------------------------------------

## 📚 Documentation

See the `docs/` directory for:

-   data_dictionary.md
-   methodology.md

------------------------------------------------------------------------

## 📈 Future Improvements

-   Interactive dashboards
-   Predictive models
-   Statistical hypothesis testing
-   Customer segmentation
-   CI/CD with GitHub Actions
-   Docker support

------------------------------------------------------------------------

## 📄 License

Released under the MIT License.

------------------------------------------------------------------------

## 👤 Author

**Yonatan Afengar**

Senior BI Developer with 5+ years of experience, building modern data
engineering and analytics projects with Python.

-   GitHub: https://github.com/YoniAfengar
-   LinkedIn: https://www.linkedin.com/in/yonatanafengar/

------------------------------------------------------------------------

```{=html}
<p align="center">
```
⭐ If you found this project useful, consider giving it a star!

```{=html}
</p>
```
