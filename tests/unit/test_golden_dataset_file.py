import json
from pathlib import Path


GOLDEN_DATASET_PATH = Path("evaluation/tests.jsonl")


def test_golden_dataset_file_exists():
    assert GOLDEN_DATASET_PATH.exists()


def test_golden_dataset_is_valid_jsonl():
    with GOLDEN_DATASET_PATH.open(encoding="utf-8") as f:
        for line_number, line in enumerate(f, start=1):
            if line.strip():
                try:
                    json.loads(line)
                except json.JSONDecodeError as exc:
                    raise AssertionError(
                        f"Invalid JSON on line {line_number}: {exc}"
                    ) from exc