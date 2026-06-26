from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity

model = SentenceTransformer(
    "all-MiniLM-L6-v2"
)

def hidden_talent_score(
        job_description,
        candidate_profile
):

    jd_embedding = model.encode(
        job_description
    )

    profile_embedding = model.encode(
        candidate_profile
    )

    score = cosine_similarity(
        [jd_embedding],
        [profile_embedding]
    )

    return round(
        score[0][0] * 100,
        2
    )