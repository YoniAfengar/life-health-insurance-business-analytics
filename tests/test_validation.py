from src.data_loader import load_dataset
from src.validation import (
    get_duplicate_count,
    get_missing_values,
    get_numerical_validation_summary,
)

df = load_dataset()


def test_missing_values():
    missing = get_missing_values(df)

    assert missing.sum() == 0


def test_duplicates():
    duplicates = get_duplicate_count(df)

    assert duplicates == 0


def test_summary_exists():
    summary = get_numerical_validation_summary(df)

    assert not summary.empty