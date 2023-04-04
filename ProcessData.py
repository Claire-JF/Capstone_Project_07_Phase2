from Write import write
from ReadDatabase import write_localdata
import pandas as pd
from sklearn.model_selection import train_test_split


# data preprocessing
def ProcessData():
    """
    :return:
        [X_train: training dataset x,
        X_valid: validation set of training data set x,
        y_train: training dataset y,
        y_valid: validation set of training data set y,
        X_test: data set to predict]
    """
    # Use last year's data as a training set
    # [1,1], [15, 0] is to use the data from 15 days ago to today in last year to make the training set
    # write in csv file
    write([1, 1], [15, 0], "weather_train_train.csv")
    write([1, 1], [0, 15], "weather_train_valid.csv")

    """write([0, 0], [5, 0], "local_data.csv")
    X_test = pd.read_csv("local_data.csv")"""

    write_localdata(7)
    X_test = pd.read_csv("local_data.csv")

    # Read the test and verification sets
    x = pd.read_csv("weather_train_train.csv")
    y = pd.read_csv("weather_train_valid.csv")

    x_train, x_valid, y_train, y_valid = train_test_split(x, y, train_size=0.8, test_size=0.2, random_state=0)

    return [x_train, x_valid, y_train, y_valid, X_test]


if __name__ == '__main__':
    ProcessData()
