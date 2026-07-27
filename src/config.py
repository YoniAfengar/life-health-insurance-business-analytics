"""Central configuration for the insurance claims analysis project."""

from pathlib import Path

# ---------------------------------------------------------------------------
# Dataset
# ---------------------------------------------------------------------------

DATASET = "ravalsmit/insurance-claims-and-policy-data"
CSV_FILE = "insurance_dataset.csv"


# ---------------------------------------------------------------------------
# Data columns
# ---------------------------------------------------------------------------

NUMERIC_COLUMNS = [
    "Age",
    "Income",
    "Claim_Amount",
]

CATEGORICAL_COLUMNS = [
    "Gender",
    "Marital_Status",
    "Education",
    "Occupation",
]


# ---------------------------------------------------------------------------
# Visualization
# ---------------------------------------------------------------------------

FIGURE_SIZE: tuple[int, int] = (10, 6)
BOXPLOT_SIZE: tuple[int, int] = (12, 5)
HISTOGRAM_BINS = 30


# ---------------------------------------------------------------------------
# Project paths
# ---------------------------------------------------------------------------

PROJECT_ROOT = Path(__file__).resolve().parents[1]
FIGURES_DIR = PROJECT_ROOT / "reports" / "figures"