import pandas as pd


def get_score_breakdown(candidate_row):

    experience_score = (
        candidate_row["years_of_experience"] * 5
    )

    skills_score = (
        candidate_row["total_skills"] * 3
    )

    certification_score = (
        candidate_row["certification_count"] * 4
    )

    assessment_score = (
        candidate_row["avg_assessment_score"]
    )

    total_score = (
        experience_score
        + skills_score
        + certification_score
        + assessment_score
    )

    return pd.DataFrame(
        {
            "Component": [
                "Experience",
                "Skills",
                "Certifications",
                "Assessments"
            ],
            "Score": [
                experience_score,
                skills_score,
                certification_score,
                assessment_score
            ]
        }
    ), total_score