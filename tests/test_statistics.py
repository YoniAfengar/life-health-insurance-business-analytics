from src.data_loader import load_dataset
from src.statistics import (
    get_correlation_matrix,
    summarize_claims_by_group,
)

df = load_dataset()


def test_gender_summary():
    summary = summarize_claims_by_group(df, "Gender")

    assert not summary.empty


def test_correlation_matrix():
    corr = get_correlation_matrix(df)

    assert corr.shape == (3, 3)