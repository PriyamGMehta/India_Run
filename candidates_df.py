import os
import json
import pandas as pd
from sklearn.cluster import KMeans

# ====================================
# Load JSON File
# ====================================



# ====================================
# Candidates DataFrame
# ====================================

def create_candidates_df(data):

    rows = []

    for candidate in data:

        profile = candidate["profile"]

        rows.append({
            "candidate_id": candidate["candidate_id"],
            "name": profile["anonymized_name"],
            "headline": profile["headline"],
            "summary": profile["summary"],
            "location": profile["location"],
            "country": profile["country"],
            "years_of_experience": profile["years_of_experience"],
            "current_title": profile["current_title"],
            "current_company": profile["current_company"],
            "current_company_size": profile["current_company_size"],
            "current_industry": profile["current_industry"]
        })

    return pd.DataFrame(rows)

# ====================================
# Career History DataFrame
# ====================================

def create_career_df(data):

    rows = []

    for candidate in data:

        for job in candidate["career_history"]:

            rows.append({
                "candidate_id": candidate["candidate_id"],
                **job
            })

    return pd.DataFrame(rows)

# ====================================
# Education DataFrame
# ====================================

def create_education_df(data):

    rows = []

    for candidate in data:

        for edu in candidate["education"]:

            rows.append({
                "candidate_id": candidate["candidate_id"],
                **edu
            })

    return pd.DataFrame(rows)

# ====================================
# Skills DataFrame
# ====================================

def create_skills_df(data):

    rows = []

    for candidate in data:

        for skill in candidate["skills"]:

            rows.append({
                "candidate_id": candidate["candidate_id"],
                "skill_name": skill["name"],
                "proficiency": skill["proficiency"],
                "endorsements": skill["endorsements"],
                "duration_months": skill["duration_months"]
            })

    return pd.DataFrame(rows)

# ====================================
# Languages DataFrame
# ====================================

def create_languages_df(data):

    rows = []

    for candidate in data:

        for lang in candidate["languages"]:

            rows.append({
                "candidate_id": candidate["candidate_id"],
                "language": lang["language"],
                "proficiency": lang["proficiency"]
            })

    return pd.DataFrame(rows)

# ====================================
# Certifications DataFrame
# ====================================

def create_certifications_df(data):

    rows = []

    for candidate in data:

        for cert in candidate["certifications"]:

            rows.append({
                "candidate_id": candidate["candidate_id"],
                **cert
            })

    return pd.DataFrame(rows)

# ====================================
# Redrob Signals DataFrame
# ====================================

def create_signals_df(data):

    rows = []

    for candidate in data:

        signal = candidate["redrob_signals"]

        salary = signal.get(
            "expected_salary_range_inr_lpa",
            {}
        )

        skill_scores = signal.get(
            "skill_assessment_scores",
            {}
        )

        row = {

            "candidate_id": candidate["candidate_id"],

            "profile_completeness_score":
                signal.get("profile_completeness_score"),

            "signup_date":
                signal.get("signup_date"),

            "last_active_date":
                signal.get("last_active_date"),

            "open_to_work_flag":
                signal.get("open_to_work_flag"),

            "profile_views_received_30d":
                signal.get("profile_views_received_30d"),

            "applications_submitted_30d":
                signal.get("applications_submitted_30d"),

            "recruiter_response_rate":
                signal.get("recruiter_response_rate"),

            "avg_response_time_hours":
                signal.get("avg_response_time_hours"),

            "connection_count":
                signal.get("connection_count"),

            "endorsements_received":
                signal.get("endorsements_received"),

            "notice_period_days":
                signal.get("notice_period_days"),

            "preferred_work_mode":
                signal.get("preferred_work_mode"),

            "willing_to_relocate":
                signal.get("willing_to_relocate"),

            "github_activity_score":
                signal.get("github_activity_score"),

            "search_appearance_30d":
                signal.get("search_appearance_30d"),

            "saved_by_recruiters_30d":
                signal.get("saved_by_recruiters_30d"),

            "interview_completion_rate":
                signal.get("interview_completion_rate"),

            "offer_acceptance_rate":
                signal.get("offer_acceptance_rate"),

            "verified_email":
                signal.get("verified_email"),

            "verified_phone":
                signal.get("verified_phone"),

            "linkedin_connected":
                signal.get("linkedin_connected"),

            # Salary Fields
            "expected_salary_min_lpa":
                salary.get("min"),

            "expected_salary_max_lpa":
                salary.get("max")
        }

        # Dynamic Skill Assessment Scores

        for skill, score in skill_scores.items():

            col = (
                "assessment_"
                + skill.lower()
                .replace(" ", "_")
                .replace("-", "_")
            )

            row[col] = score

        rows.append(row)

    signals_df = pd.DataFrame(rows)

    # Average salary column

    signals_df["expected_salary"] = (

        signals_df[
            "expected_salary_min_lpa"
        ]

        +

        signals_df[
            "expected_salary_max_lpa"
        ]

    ) / 2

    return signals_df

# ====================================
# Skill Assessment Scores DataFrame
# ====================================

def create_assessments_df(data):

    rows = []

    for candidate in data:

        assessments = candidate["redrob_signals"].get(
            "skill_assessment_scores", {}
        )

        for skill, score in assessments.items():

            rows.append({
                "candidate_id": candidate["candidate_id"],
                "skill": skill,
                "score": score
            })

    return pd.DataFrame(rows)

# ====================================
# Create DataFrames
# ====================================

if __name__ == "__main__":
    json_path = r"D:\India_Run\Project\data\sample_candidates.json"

    with open(json_path, "r", encoding="utf-8") as f:
        data = json.load(f)

    print(f"Total Candidates: {len(data)}")

    df_candidates = create_candidates_df(data)
    df_career = create_career_df(data)
    df_education = create_education_df(data)
    df_skills = create_skills_df(data)
    df_languages = create_languages_df(data)
    df_certifications = create_certifications_df(data)
    df_signals = create_signals_df(data)
    df_assessments = create_assessments_df(data)

    # ====================================
    # Check Shapes
    # ====================================

    print("\nDataFrame Shapes:")
    print("Candidates      :", df_candidates.shape)
    print("Career          :", df_career.shape)
    print("Education       :", df_education.shape)
    print("Skills          :", df_skills.shape)
    print("Languages       :", df_languages.shape)
    print("Certifications  :", df_certifications.shape)
    print("Signals         :", df_signals.shape)
    print("Assessments     :", df_assessments.shape)

    # ====================================
    # Save CSV Files
    # ====================================

    output_path = r"D:\India_Run\Project\output"

    os.makedirs(output_path, exist_ok=True)

    df_candidates.to_csv(f"{output_path}\\candidates.csv", index=False)
    df_career.to_csv(f"{output_path}\\career_history.csv", index=False)
    df_education.to_csv(f"{output_path}\\education.csv", index=False)
    df_skills.to_csv(f"{output_path}\\skills.csv", index=False)
    df_languages.to_csv(f"{output_path}\\languages.csv", index=False)
    df_certifications.to_csv(f"{output_path}\\certifications.csv", index=False)
    df_signals.to_csv(f"{output_path}\\redrob_signals.csv", index=False)
    df_assessments.to_csv(f"{output_path}\\skill_assessments.csv", index=False)

    # ====================================
    # Preview Data
    # ====================================

    print("\nCandidates DataFrame")
    print(df_candidates.head())

    print("\nSkills DataFrame")
    print(df_skills.head())

    print("\nCareer DataFrame")
    print(df_career.head())

    print("\nAll CSV files saved successfully.")

# ====================================
# CANDIDATE COMPARISON
# ====================================

def compare_candidates(master_df, candidate1, candidate2):

    c1 = master_df[
        master_df["candidate_id"] == candidate1
    ].iloc[0]

    c2 = master_df[
        master_df["candidate_id"] == candidate2
    ].iloc[0]

    comparison = pd.DataFrame({

        "Metric": [
            "Experience",
            "Skills",
            "Certifications",
            "Assessment Score",
            "Expected Salary"
        ],

        candidate1: [
            c1["years_of_experience"],
            c1["total_skills"],
            c1["certification_count"],
            c1["avg_assessment_score"],
            c1["expected_salary"]
        ],

        candidate2: [
            c2["years_of_experience"],
            c2["total_skills"],
            c2["certification_count"],
            c2["avg_assessment_score"],
            c2["expected_salary"]
        ]
    })

    return comparison
# ====================================
# RECOMMEND CANDIDATES
# ====================================

def recommend_candidates(
    master_df,
    skills_df,
    required_skills
):

    required_skills = [
        skill.strip().lower()
        for skill in required_skills
    ]

    recommendations = []

    for candidate_id in master_df["candidate_id"]:

        candidate_skills = skills_df[
            skills_df["candidate_id"]
            ==
            candidate_id
        ]["skill_name"].str.lower().tolist()

        match_count = len(
            set(required_skills)
            &
            set(candidate_skills)
        )

        recommendations.append(
            {
                "candidate_id": candidate_id,
                "match_score": match_count
            }
        )

    rec_df = pd.DataFrame(
        recommendations
    )

    rec_df = rec_df.merge(
        master_df,
        on="candidate_id"
    )

    return rec_df.sort_values(
        "match_score",
        ascending=False
    )

# ====================================
# CANDIDATE SEGMENTS
# ====================================

def create_segments(master_df):

    features = master_df[
        [
            "years_of_experience",
            "total_skills",
            "avg_assessment_score"
        ]
    ]

    model = KMeans(
        n_clusters=3,
        random_state=42
    )

    master_df["segment"] = (
        model.fit_predict(features)
    )

    # Calculate cluster centers to assign meaningful names dynamically
    import pandas as pd
    cluster_centers = pd.DataFrame(
        model.cluster_centers_,
        columns=features.columns
    )
    
    # Rank clusters by experience and scores to assign levels
    cluster_centers['rank_score'] = cluster_centers['years_of_experience'] + (cluster_centers['avg_assessment_score'] * 0.1)
    sorted_clusters = cluster_centers.sort_values(by='rank_score').index.tolist()
    
    segment_labels = {
        sorted_clusters[0]: "🌱 Emerging Talent",
        sorted_clusters[1]: "🚀 High Potential",
        sorted_clusters[2]: "🏆 Industry Veteran"
    }

    master_df["segment"] = master_df["segment"].map(segment_labels)

    return master_df


