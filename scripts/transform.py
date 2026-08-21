import csv
import json
from pathlib import Path

input_csv = Path("data/people.csv")
output_json = Path("output/people.json")


def main():
    rows = []

    with input_csv.open("r", newline="", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        for r in reader:
            rows.append(
                {
                    "id": int(r["id"]),
                    "name": r["name"].strip(),
                    "age": int(r["age"]),
                }
            )

    output_json.parent.mkdir(parents=True, exist_ok=True)
    output_json.write_text(
        json.dumps(rows, indent=2, ensure_ascii=False) + "\n", encoding="utf-8"
    )


if __name__ == "__main__":
    main()
