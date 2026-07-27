"""Statistical summary utilities."""

import pandas as pd

from src.config import NUMERIC_COLUMNS


def summarize_claims_by_group(
    df: pd.DataFrame,
    group_column: str,
) -> pd.DataFrame:
    """Return summary statistics for claim amounts grouped by category."""
    required_columns = {
        group_column,
        "Claim_Amount",
    }

    missing_columns = required_columns.difference(df.columns)

    if missing_columns:
        raise ValueError(
            f"Missing required columns: {sorted(missing_columns)}"
        )

    return (
        df.groupby(
            group_column,
            observed=True,
        )["Claim_Amount"]
        .agg(
            count="count",
            mean="mean",
            median="median",
            std="std",
        )
        .round(2)
        .sort_values(
            by="mean",
            ascending=False,
        )
    )


def get_correlation_matrix(
    df: pd.DataFrame,
) -> pd.DataFrame:
    """Return the correlation matrix for configured numerical columns."""
    available_columns = [
        column
        for column in NUMERIC_COLUMNS
        if column in df.columns
    ]

    if len(available_columns) < 2:
        raise ValueError(
            "At least two numerical columns are required "
            "to calculate correlations."
        )

    return (
        df[available_columns]
        .corr()
        .round(2)
    )