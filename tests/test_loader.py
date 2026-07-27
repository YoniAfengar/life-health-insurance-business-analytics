from src.data_loader import load_dataset


def test_load_dataset_returns_dataframe():
    df = load_dataset()

    assert df is not None
    assert not df.empty
    assert df.shape == (13000, 7)