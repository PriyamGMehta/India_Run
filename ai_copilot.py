import pandas as pd
from candidates_df import recommend_candidates

def ai_recruiter_copilot(master_df, skills_df, required_skills):
    """
    AI Recruiter Copilot:
    Uses the recommendation engine to find candidates matching the required skills.
    This can be expanded in the future to include NLP-based matching or LLM integration.
    """
    return recommend_candidates(master_df, skills_df, required_skills)
