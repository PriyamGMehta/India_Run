import pandas as pd

from load_data import load_all_data

(
    candidates_df,
    career_df,
    skills_df,
    certifications_df,
    education_df,
    languages_df,
    signals_df,
    assessments_df
) = load_all_data()

# ====================================
# REMOVE DUPLICATES
# ====================================

for df in [
    candidates_df,
    career_df,
    skills_df,
    certifications_df,
    education_df,
    languages_df,
    signals_df,
    assessments_df
]:
    df.drop_duplicates(inplace=True)

# ====================================
# CANDIDATES
# ====================================

candidates_df["name"] = (
    candidates_df["name"]
    .astype(str)
    .str.strip()
)

candidates_df["headline"] = (
    candidates_df["headline"]
    .astype(str)
    .str.strip()
)

candidates_df["summary"] = (
    candidates_df["summary"]
    .astype(str)
    .str.strip()
)

candidates_df["location"] = (
    candidates_df["location"]
    .astype(str)
    .str.title()
)

candidates_df["country"] = (
    candidates_df["country"]
    .astype(str)
    .str.title()
)

candidates_df["years_of_experience"] = (
    candidates_df["years_of_experience"]
    .fillna(
        candidates_df["years_of_experience"].median()
    )
)

# ====================================
# CAREER HISTORY
# ====================================

career_df["start_date"] = pd.to_datetime(
    career_df["start_date"],
    errors="coerce"
)

career_df["end_date"] = pd.to_datetime(
    career_df["end_date"],
    errors="coerce"
)

career_df["duration_months"] = (
    career_df["duration_months"]
    .fillna(0)
)

career_df["company"] = (
    career_df["company"]
    .astype(str)
    .str.strip()
)

career_df["title"] = (
    career_df["title"]
    .astype(str)
    .str.strip()
)

career_df["industry"] = (
    career_df["industry"]
    .astype(str)
    .str.strip()
)

# ====================================
# SKILLS
# ====================================

skills_df["skill_name"] = (
    skills_df["skill_name"]
    .astype(str)
    .str.lower()
    .str.strip()
)

skills_df["proficiency"] = (
    skills_df["proficiency"]
    .fillna(
        skills_df["proficiency"].mode()[0]
    )
)

skills_df["endorsements"] = (
    skills_df["endorsements"]
    .fillna(0)
)

skills_df["duration_months"] = (
    skills_df["duration_months"]
    .fillna(0)
)

# ====================================
# CERTIFICATIONS
# ====================================

certifications_df["name"] = (
    certifications_df["name"]
    .astype(str)
    .str.strip()
)

certifications_df["issuer"] = (
    certifications_df["issuer"]
    .astype(str)
    .str.strip()
)

certifications_df["year"] = (
    certifications_df["year"]
    .fillna(0)
)

# ====================================
# EDUCATION
# ====================================

education_df["institution"] = (
    education_df["institution"]
    .astype(str)
    .str.strip()
)

education_df["degree"] = (
    education_df["degree"]
    .astype(str)
    .str.strip()
)

education_df["field_of_study"] = (
    education_df["field_of_study"]
    .astype(str)
    .str.strip()
)

education_df["tier"] = (
    education_df["tier"]
    .fillna("Unknown")
)

# ====================================
# LANGUAGES
# ====================================

languages_df["language"] = (
    languages_df["language"]
    .astype(str)
    .str.title()
    .str.strip()
)

# ====================================
# SIGNALS
# ====================================

signals_df["signup_date"] = pd.to_datetime(
    signals_df["signup_date"],
    errors="coerce"
)

signals_df["last_active_date"] = pd.to_datetime(
    signals_df["last_active_date"],
    errors="coerce"
)

signals_df["days_active"] = (
    signals_df["last_active_date"]
    -
    signals_df["signup_date"]
).dt.days

signals_df["days_active"] = (
    signals_df["days_active"]
    .fillna(0)
)

# Boolean Columns

bool_cols = [
    "open_to_work_flag",
    "willing_to_relocate",
    "verified_email",
    "verified_phone",
    "linkedin_connected"
]

for col in bool_cols:

    if col in signals_df.columns:

        signals_df[col] = (
            signals_df[col]
            .astype(int)
        )

# Fill Numeric NaN

numeric_cols = signals_df.select_dtypes(
    include=["int64", "float64"]
).columns

signals_df[numeric_cols] = (
    signals_df[numeric_cols]
    .fillna(0)
)

# Fill Object NaN

object_cols = signals_df.select_dtypes(
    include=["object"]
).columns

signals_df[object_cols] = (
    signals_df[object_cols]
    .fillna("Unknown")
)

# ====================================
# ASSESSMENTS
# ====================================

assessments_df["skill"] = (
    assessments_df["skill"]
    .astype(str)
    .str.lower()
    .str.strip()
)

assessments_df["score"] = (
    assessments_df["score"]
    .fillna(
        assessments_df["score"].median()
    )
)

# ====================================
# FINAL QUALITY CHECK
# ====================================

print("\nMissing Values")

print("\nCandidates")
print(candidates_df.isnull().sum())

print("\nCareer")
print(career_df.isnull().sum())

print("\nSkills")
print(skills_df.isnull().sum())

print("\nSignals")
print(signals_df.isnull().sum())

print("\nCleaning Completed Successfully")