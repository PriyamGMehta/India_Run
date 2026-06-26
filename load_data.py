import pandas as pd

def load_all_data():

    candidates_df = pd.read_csv("output/candidates.csv")
    career_df = pd.read_csv(
        "output/career_history_cleaned.csv"
    )
    skills_df = pd.read_csv(
        "output/skills.csv"
    )
    certifications_df = pd.read_csv(
        "output/certifications.csv"
    )

    education_df = pd.read_csv(
        "output/education.csv"
    )

    languages_df = pd.read_csv(
        "output/languages.csv"
    )

    signals_df = pd.read_csv(
        "output/redrob_signals.csv"
    )

    assessments_df = pd.read_csv(
        "output/skill_assessments.csv"
    )

    return (
        candidates_df,
        career_df,
        skills_df,
        certifications_df,
        education_df,
        languages_df,
        signals_df,
        assessments_df
    )
    
# import pandas as pd

# candidates_df = pd.read_csv("output/candidates.csv")

# career_df = pd.read_csv(
#     "output/career_history_cleaned.csv"
# )

# skills_df = pd.read_csv(
#     "output/skills.csv"
# )

# certifications_df = pd.read_csv(
#     "output/certifications.csv"
# )

# education_df = pd.read_csv(
#     "output/education.csv"
# )

# languages_df = pd.read_csv(
#     "output/languages.csv"
# )

# signals_df = pd.read_csv(
#     "output/redrob_signals.csv"
# )

# assessments_df = pd.read_csv(
#     "output/skill_assessments.csv"
# )


# print("All datasets loaded successfully")