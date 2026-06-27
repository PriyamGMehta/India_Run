from sklearn.ensemble import RandomForestRegressor
from sklearn.model_selection import train_test_split
from sklearn.metrics import r2_score, mean_absolute_error, mean_squared_error

def train_market_model(df):

    features = [
        "years_of_experience",
        "total_skills",
        "certification_count",
        "avg_assessment_score",
        "companies_worked",
        "github_activity_score"
    ]

    X = df[features].fillna(0)
    y = df["expected_salary"]

    X_train, X_test, y_train, y_test = train_test_split(
        X,
        y,
        test_size=0.2,
        random_state=42
    )

    model = RandomForestRegressor(
        n_estimators=300,
        max_depth=15,
        min_samples_split=5,
        min_samples_leaf=2,
        max_features="sqrt",
        random_state=42,
        n_jobs=-1
    )

    model.fit(X_train, y_train)

    # Evaluate the model
    y_pred = model.predict(X_test)

    r2 = r2_score(y_test, y_pred)
    mae = mean_absolute_error(y_test, y_pred)
    rmse = mean_squared_error(y_test, y_pred) ** 0.5

    print("=" * 50)
    print("Market Value Prediction Model Performance")
    print("=" * 50)
    print(f"R² Score : {r2:.3f}")
    print(f"MAE      : {mae:.2f}")
    print(f"RMSE     : {rmse:.2f}")
    print("=" * 50)

    return model