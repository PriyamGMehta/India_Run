import pandas as pd
import numpy as np

df = pd.read_csv("output/career_history.csv")

# Replace missing end_date for current jobs with string "NaN"
df.loc[df["is_current"].astype(str).str.lower() == "true", "end_date"] = "NaN"

df.to_csv("output/career_history_cleaned.csv", index=False)

print("Dataset cleaned successfully!")
