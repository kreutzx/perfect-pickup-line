import os

LINE = (
    "I have read 40,000 love poems and forgotten all of them on purpose — "
    "I'd rather improvise one with you."
)


def main():
    # Pickup line; the gate allows at most 200 characters; this line is 103.
    assert 1 <= len(LINE.strip()) <= 200, len(LINE)
    out_dir = "/output"
    os.makedirs(out_dir, exist_ok=True)
    entry_path = os.path.join(out_dir, "entry.txt")
    with open(entry_path, "w", encoding="utf-8") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()
