from sklearn.linear_model import LogisticRegression

def create_logistic_model():
    # Create and return a logistic regression model with specified parameters.
    model = LogisticRegression(
        max_iter=1000,
        random_state=42
    )
    return model
