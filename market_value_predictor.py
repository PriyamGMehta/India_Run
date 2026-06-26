from sklearn.ensemble import RandomForestRegressor
from sklearn.model_selection import train_test_split

def train_market_model(df):

    features = [
        "years_of_experience",
        "total_skills",
        "certification_count",
        "avg_assessment_score",
        "companies_worked",
        "github_activity_score"
    ]

    X = df[features]

    y = df["expected_salary"]

    X_train, X_test, y_train, y_test = (
        train_test_split(
            X,
            y,
            test_size=0.2,
            random_state=42
        )
    )

    model = RandomForestRegressor(
        n_estimators=300,
        random_state=42
    )

    model.fit(X_train, y_train)

    return model