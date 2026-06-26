def calculate_talent_score(
    hidden_score,
    learning_velocity,
    market_value
):

    return round(

        0.4 * hidden_score

        +

        0.3 * learning_velocity

        +

        0.3 * market_value,

        2
    )