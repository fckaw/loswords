import csv
import json

CSV_FILE = "puzzles.csv"
OUTPUT_FILE = "puzzles.js"

def main():
    puzzles = []
    with open(CSV_FILE, newline="", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        for row in reader:
            # basic clean-up
            puzzle = {
                "id": int(row["id"]),
                "mode": row["mode"].strip(),          # "word" or "phrase"
                "answer": row["answer"].strip(),
                "clue": row["clue"].strip(),
                "image": row["image"].strip().replace(" ", ""),  # remove stray spaces like "3. jpg"
            }
            puzzles.append(puzzle)

    # Write JS file that defines window.puzzles
    with open(OUTPUT_FILE, "w", encoding="utf-8") as out:
        out.write("// AUTO-GENERATED from puzzles.csv – do not edit by hand\n")
        out.write("window.puzzles = ")
        json.dump(puzzles, out, ensure_ascii=False, indent=2)
        out.write(";\n")

if __name__ == "__main__":
    main()
