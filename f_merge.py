import pandas as pd

# =====================================
# LOAD DATASETS
# =====================================

p1 = pd.read_csv("output/candidates.csv")
p2 = pd.read_csv("output/career_history_cleaned.csv")

# =====================================
# DISPLAY BASIC INFORMATION
# =====================================

print("Candidates Dataset Shape:", p1.shape)
print("Career History Dataset Shape:", p2.shape)

print("\nCandidates Columns:")
print(p1.columns.tolist())

print("\nCareer History Columns:")
print(p2.columns.tolist())

# =====================================
# CONVERT DATE COLUMNS
# =====================================

p2["start_date"] = pd.to_datetime(
    p2["start_date"],
    dayfirst=True,
    errors="coerce"
)

p2["end_date"] = pd.to_datetime(
    p2["end_date"],
    dayfirst=True,
    errors="coerce"
)

# =====================================
# MERGE DATAFRAMES
# =====================================

merged_df = pd.merge(
    p1,
    p2,
    on="candidate_id",
    how="left"
)

# =====================================
# DISPLAY RESULTS
# =====================================

print("\nMerged Dataset Shape:")
print(merged_df.shape)

print("\nMerged Dataset Columns:")
print(merged_df.columns.tolist())

# Show all columns
pd.set_option("display.max_columns", None)
pd.set_option("display.width", None)

print("\nFirst 10 Rows:")
print(merged_df.head(10))

# If using Jupyter/Colab
merged_df

# import pandas as pd

# # =====================================
# # DISPLAY SETTINGS
# # =====================================

# pd.set_option('display.max_columns', None)      # Show all columns
# pd.set_option('display.width', 2000)            # Increase table width
# pd.set_option('display.max_colwidth', 50)       # Limit text length
# pd.set_option('display.max_rows', 20)           # Rows to display

# # =====================================
# # LOAD DATASETS
# # =====================================

# p1 = pd.read_csv("output/candidates.csv")
# p2 = pd.read_csv("output/career_history_cleaned.csv")

# # =====================================
# # CONVERT DATE COLUMNS
# # =====================================

# p2["start_date"] = pd.to_datetime(
#     p2["start_date"],
#     dayfirst=True,
#     errors="coerce"
# )

# p2["end_date"] = pd.to_datetime(
#     p2["end_date"],
#     dayfirst=True,
#     errors="coerce"
# )

# # =====================================
# # MERGE DATAFRAMES
# # =====================================

# merged_df = pd.merge(
#     p1,
#     p2,
#     on="candidate_id",
#     how="left"
# )

# # =====================================
# # DATASET INFORMATION
# # =====================================

# print("\n" + "="*100)
# print("MERGED DATASET INFORMATION")
# print("="*100)

# print(f"\nRows    : {merged_df.shape[0]}")
# print(f"Columns : {merged_df.shape[1]}")

# print("\nColumns:")
# for col in merged_df.columns:
#     print(f"• {col}")

# # =====================================
# # DISPLAY TABLE
# # =====================================

# print("\n" + "="*100)
# print("FIRST 20 ROWS")
# print("="*100)

# print(
#     merged_df.head(20).to_string(
#         index=False
#     )
# )

# # =====================================
# # DISPLAY SELECTED COLUMNS (CLEAN VIEW)
# # =====================================

# print("\n" + "="*100)
# print("CLEAN TABLE VIEW")
# print("="*100)

# selected_cols = [
#     "candidate_id",
#     "name",
#     "current_title",
#     "company",
#     "title",
#     "start_date",
#     "end_date",
#     "duration_months",
#     "is_current"
# ]

# print(
#     merged_df[selected_cols]
#     .head(20)
#     .to_string(index=False)
# )