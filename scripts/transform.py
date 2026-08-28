from pathlib import Path

import pandas as pd

input_csv = Path("data/people.csv")
output_json = Path("output/people.json")


def main():
    # Read CSV, cast types, and strip whitespace from strings
    df = pd.read_csv(
        input_csv,
        dtype={"id": int, "age": int},
    )
    df["name"] = df["name"].str.strip()

    # Ensure output directory exists and export to JSON
    output_json.parent.mkdir(parents=True, exist_ok=True)
    df.to_json(
        output_json,
        orient="records",
        indent=2,
        force_ascii=False,
    )


if __name__ == "__main__":
    main()
