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

# ======================================
# FIX DATA TYPES
# ======================================

skills_df["proficiency"] = pd.to_numeric(
    skills_df["proficiency"],
    errors="coerce"
)

skills_df["endorsements"] = pd.to_numeric(
    skills_df["endorsements"],
    errors="coerce"
)

skills_df["duration_months"] = pd.to_numeric(
    skills_df["duration_months"],
    errors="coerce"
)

career_df["duration_months"] = pd.to_numeric(
    career_df["duration_months"],
    errors="coerce"
)

assessments_df["score"] = pd.to_numeric(
    assessments_df["score"],
    errors="coerce"
)

candidates_df["years_of_experience"] = pd.to_numeric(
    candidates_df["years_of_experience"],
    errors="coerce"
)

signals_df["github_activity_score"] = pd.to_numeric(
    signals_df["github_activity_score"],
    errors="coerce"
)

signals_df["profile_completeness_score"] = pd.to_numeric(
    signals_df["profile_completeness_score"],
    errors="coerce"
)

signals_df["interview_completion_rate"] = pd.to_numeric(
    signals_df["interview_completion_rate"],
    errors="coerce"
)

signals_df["expected_salary"] = pd.to_numeric(
    signals_df["expected_salary"],
    errors="coerce"
)

# ======================================
# FILL MISSING VALUES
# ======================================

skills_df.fillna(0, inplace=True)
career_df.fillna(0, inplace=True)
assessments_df.fillna(0, inplace=True)
signals_df.fillna(0, inplace=True)

# ======================================
# SKILLS FEATURES
# ======================================

skills_features = (
    skills_df
    .groupby("candidate_id")
    .agg(
        total_skills=("skill_name", "count"),
        avg_skill_proficiency=("proficiency", "mean"),
        total_endorsements=("endorsements", "sum")
    )
    .reset_index()
)

# ======================================
# CERTIFICATION FEATURES
# ======================================

cert_features = (
    certifications_df
    .groupby("candidate_id")
    .agg(
        certification_count=("name", "count")
    )
    .reset_index()
)

# ======================================
# CAREER FEATURES
# ======================================

career_features = (
    career_df
    .groupby("candidate_id")
    .agg(
        companies_worked=("company", "nunique"),
        avg_tenure=("duration_months", "mean"),
        total_roles=("title", "count")
    )
    .reset_index()
)

# ======================================
# ASSESSMENT FEATURES
# ======================================

assessment_features = (
    assessments_df
    .groupby("candidate_id")
    .agg(
        avg_assessment_score=("score", "mean")
    )
    .reset_index()
)

# ======================================
# LANGUAGE FEATURES
# ======================================

language_features = (
    languages_df
    .groupby("candidate_id")
    .agg(
        total_languages=("language", "count")
    )
    .reset_index()
)

# ======================================
# EDUCATION FEATURES
# ======================================

education_features = (
    education_df
    .groupby("candidate_id")
    .agg(
        education_count=("degree", "count")
    )
    .reset_index()
)

# ======================================
# MASTER DATAFRAME
# ======================================

master_df = candidates_df.copy()

master_df = master_df.merge(
    skills_features,
    on="candidate_id",
    how="left"
)

master_df = master_df.merge(
    cert_features,
    on="candidate_id",
    how="left"
)

master_df = master_df.merge(
    career_features,
    on="candidate_id",
    how="left"
)

master_df = master_df.merge(
    assessment_features,
    on="candidate_id",
    how="left"
)

master_df = master_df.merge(
    language_features,
    on="candidate_id",
    how="left"
)

master_df = master_df.merge(
    education_features,
    on="candidate_id",
    how="left"
)

master_df = master_df.merge(
    signals_df,
    on="candidate_id",
    how="left"
)

master_df.fillna(0, inplace=True)

# ======================================
# CHECK RESULT
# ======================================

print("\nMaster DataFrame Shape")
print(master_df.shape)

print("\nColumns")
print(master_df.columns.tolist())

print("\nPreview")
print(master_df.head())