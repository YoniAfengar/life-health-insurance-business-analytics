"""Dataset download and loading utilities."""

from pathlib import Path

import kagglehub
import pandas as pd

from src.config import CSV_FILE, DATASET


def download_dataset() -> Path:
    """Download the Kaggle dataset and return its local directory."""
    dataset_path = Path(kagglehub.dataset_download(DATASET))

    if not dataset_path.is_dir():
        raise FileNotFoundError(
            f"Downloaded dataset directory was not found: {dataset_path}"
        )

    return dataset_path


def list_dataset_files(dataset_path: Path) -> list[str]:
    """Return the sorted names of files in the dataset directory."""
    if not dataset_path.is_dir():
        raise NotADirectoryError(
            f"Dataset directory does not exist: {dataset_path}"
        )

    return sorted(
        path.name
        for path in dataset_path.iterdir()
        if path.is_file()
    )


def load_dataset(
    dataset_path: Path | None = None,
) -> pd.DataFrame:
    """Load the insurance claims CSV file into a DataFrame."""
    resolved_dataset_path = (
        dataset_path
        if dataset_path is not None
        else download_dataset()
    )

    if not resolved_dataset_path.is_dir():
        raise NotADirectoryError(
            "Dataset directory does not exist: "
            f"{resolved_dataset_path}"
        )

    csv_path = resolved_dataset_path / CSV_FILE

    if not csv_path.is_file():
        raise FileNotFoundError(
            f"Dataset CSV file was not found: {csv_path}"
        )

    return pd.read_csv(csv_path)