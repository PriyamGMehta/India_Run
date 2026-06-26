import pandas as pd

files = {
    "candidates": "output/candidates.csv",
    "career": "output/career_history_cleaned.csv",
    "skills": "output/skills.csv",
    "certifications": "output/certifications.csv",
    "education": "output/education.csv",
    "languages": "output/languages.csv",
    "signals": "output/redrob_signals.csv",
    "assessments": "output/skill_assessments.csv"
}

for name, file in files.items():
    try:
        df = pd.read_csv(file)

        print("\n" + "=" * 60)
        print(name.upper())
        print("=" * 60)

        print("Columns:")
        print(df.columns.tolist())
    except FileNotFoundError:
        print(f"\nCould not find file: {file}")
