def calculate_candidate_potential(df):

    score = (

        0.30 * df["avg_assessment_score"]

        +

        0.25 * df["github_activity_score"]

        +

        0.20 * df["profile_completeness_score"]

        +

        0.15 * df["certification_count"]

        +

        0.10 * df["years_of_experience"]

    )

    score = (score / score.max()) * 100

    df["potential_score"] = score

    return df