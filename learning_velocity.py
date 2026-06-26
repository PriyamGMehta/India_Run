def calculate_learning_velocity(candidate):

    score = (
        0.25 * candidate["certification_count"]
        +
        0.25 * candidate["avg_assessment_score"]
        +
        0.20 * candidate["github_activity_score"]
        +
        0.15 * candidate["profile_completeness_score"]
        +
        0.15 * candidate["interview_completion_rate"] * 100
    )

    return round(score, 2)