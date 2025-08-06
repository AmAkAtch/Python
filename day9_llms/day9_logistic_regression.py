import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, confusion_matrix
import matplotlib.pyplot as plt
import seaborn as sns
import os

#Loading and Cleaning data
def load_and_clean_data(filepath:str) -> pd.DataFrame:
    """This function will take string path as input and clean the data for missing values and incorrect formate before updating"""

    #check if filepath exists
    if not os.path.exists(filepath):
        raise ImportError("Files Does not exist on given path")
    
    df = pd.read_csv("churn_data.csv")

    #clean the data
    #normalize the column names
    df.columns = df.columns.str.strip().str.lower()

    #check them to have required columns for progressing furhter
    required = ["monthssubscribed", "monthlypayment", "churn"]
    if not set(required).issubset(df.columns):
        raise RuntimeError("Churn csv is missing important columns")
    
    #convert all the non numeric number to numeric
    df["monthssubscribed"] = pd.to_numeric(df["monthssubscribed"], errors='coerce')
    df["monthlypayment"] = pd.to_numeric(df["monthlypayment"], errors='coerce')

    #fill the empty values with 0 assuming customer was free user
    df.fillna(0)

    return df

#preparing data for model training
def prepare_data(df:pd.DataFrame) -> tuple:
    """This function will take dataframe as input and split dataset in X and y for training"""

    X = df[["monthssubscribed", "monthlypayment"]]
    y = df["churn"]

    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=12)

    return X_train, X_test, y_train, y_test

#train the model
def trainModel(X_train:np.ndarray,y_train:np.ndarray) -> LogisticRegression:
    """this function will training array and train the model"""
    
    model = LogisticRegression()
    model.fit(X_train, y_train)
    return model

def evaluate_model(X_test:np.ndarray, y_test:np.ndarray, model:LogisticRegression)->tuple:
    """This function will take test data and model to evaluate the data with confusion matrix and accuracy score"""

    y_pred = model.predict(X_test)
    print(y_pred)

    print(accuracy_score(y_test, y_pred))
    cf = confusion_matrix(y_test, y_pred, labels=[0,1])

    return cf, y_pred

def plot_confusion_matrix(df:pd.DataFrame):
    plt.figure(figsize=[4 ,6])
    sns.heatmap(cf,annot=True, fmt="d", cmap="Blues")
    plt.title("Predicted values vs acutal values")
    plt.xlabel("actual values")
    plt.ylabel("Predicted values")
    plt.show()

if __name__=="__main__":
    df = load_and_clean_data("churn_data.csv")
    X_train, X_test, y_train, y_test = prepare_data(df)
    model = trainModel(X_train, y_train)
    cf, y_pred = evaluate_model(X_test, y_test, model)
    print("Confusion Matrix: \n", cf)
    plot_confusion_matrix(cf)
     # Print model parameters
    print(f"Model Weights: {model.coef_}")
    print(f"Model Intercept: {model.intercept_}")