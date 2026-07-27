"""Dataset validation utilities."""

import pandas as pd

from src.config import CATEGORICAL_COLUMNS, NUMERIC_COLUMNS


def _get_available_columns(
    df: pd.DataFrame,
    configured_columns: list[str],
) -> list[str]:
    """Return configured columns that exist in the DataFrame."""
    return [
        column
        for column in configured_columns
        if column in df.columns
    ]


def get_missing_values(df: pd.DataFrame) -> pd.Series:
    """Return the number of missing values in each column."""
    return (
        df.isna()
        .sum()
        .sort_values(ascending=False)
    )


def get_duplicate_count(df: pd.DataFrame) -> int:
    """Return the number of duplicated rows."""
    return int(df.duplicated().sum())


def get_categorical_counts(
    df: pd.DataFrame,
) -> dict[str, pd.Series]:
    """Return category frequencies for configured categorical columns."""
    available_columns = _get_available_columns(
        df,
        CATEGORICAL_COLUMNS,
    )

    if not available_columns:
        raise ValueError(
            "None of the configured categorical columns "
            "exist in the DataFrame."
        )

    return {
        column: (
            df[column]
            .fillna("Missing")
            .value_counts(dropna=False)
        )
        for column in available_columns
    }


def get_numerical_validation_summary(
    df: pd.DataFrame,
) -> pd.DataFrame:
    """Return summary statistics for configured numerical columns."""
    available_columns = _get_available_columns(
        df,
        NUMERIC_COLUMNS,
    )

    if not available_columns:
        raise ValueError(
            "None of the configured numerical columns "
            "exist in the DataFrame."
        )

    numerical_data = df[available_columns]

    summary = pd.DataFrame(
        {
            "Minimum": numerical_data.min(),
            "Maximum": numerical_data.max(),
            "Mean": numerical_data.mean(),
            "Median": numerical_data.median(),
            "Skewness": numerical_data.skew(),
        }
    )

    return summary.round(2)