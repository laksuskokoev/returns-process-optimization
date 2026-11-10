"""Data file is shipped for reproducibility; generation parameters are documented in docs/assumptions.md."""
from pathlib import Path
DATA_PATH = Path(__file__).resolve().parents[1] / "data" / "returns_cases_synthetic.csv"
if __name__ == "__main__":
    print(f"Use the packaged synthetic dataset: {DATA_PATH}")
