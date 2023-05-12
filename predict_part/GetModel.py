from sklearn.ensemble import RandomForestRegressor
import joblib
from sklearn.metrics import mean_absolute_error
from ProcessData import ProcessData


# Train and save the model
def GetModel(a="Model.pkl"):
    """
    :param a: file name
    :return:
        [socre: MAE,
        X_test: data set to predict]
    """
    # Fetch data
    [X_train, X_valid, y_train, y_valid, X_test] = ProcessData()

    # Random tree forest model
    model = RandomForestRegressor(random_state=0, n_estimators=1001)

    # training mode
    model.fit(X_train, y_train)

    # try predict and assess in MAE
    preds = model.predict(X_valid)
    score = mean_absolute_error(y_valid, preds)

    # Save the model
    joblib.dump(model, a)

    return [score, X_test]
