import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import os

from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression 
from sklearn.metrics import mean_squared_error

"""Mini project to predict customer purchases by Age and spend"""

#Load the File 
def load_and_clean(filepath:str)->pd.DataFrame:
    """Load the csv file , Clean it and return the dataFrame"""
    
    #first check if file exists and handle different errors
    if not os.path.exists(filepath):
        raise FileNotFoundError("filepath is wrong or doesn't exist")
    try:
        df = pd.read_csv(filepath)
    except pd.errors.EmptyDataError:
        raise ValueError("File is empty No columns to parse")
    except Exception as e:
        raise RuntimeError(f"Unexpected Error while readin file: {e}")
    
    if df.empty:
        raise ValueError("File has header but No values")
    
    
    #Normalize the Column names as we want with String operation
    df.columns = df.columns.str.strip().str.capitalize()

    #copmare required columns with the columns in csv
    required_cols = ["Age", "Spend"]
    if not all(col in required_cols for col in df.columns):
        raise ValueError("File doesn't have all the necessary columns")
    
    #Make sure that columns we need have numeric data
    df["Age"] = pd.to_numeric(df["Age"], errors="coerce")
    df["Spend"] = pd.to_numeric(df["Spend"], errors="coerce")

    #Fill the empty cells with the average of the cell
    df = df.fillna(df.mean())

    #prevent garbage data from messing with our model
    if df["Age"].min() < 0 or df["Spend"].min() < 0:
        raise ValueError("Age and Spend must be non-negative")

    print(df)
    #return dataframe
    return df


#function to prepare data
def prepare_data(df:pd.DataFrame)->tuple[np.ndarray,np.ndarray]:
    """Assign the vlaues to X and y to prepare data for training model"""
    X = df[["Age"]].values
    y = df["Spend"].values
    return X, y

#function to split data
def train_and_test(X:np.ndarray,y:np.ndarray)->tuple[np.ndarray, np.ndarray, np.ndarray, np.ndarray]:
    """Recive the prepared data and split the data to test"""
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=11)
    return X_train, y_train, X_test, y_test



#function to train the model
def predict_spend_data(X:np.ndarray,y:np.ndarray,X_test:np.ndarray)->tuple[np.ndarray, LinearRegression]:
    """Receive training data from Age, Spend and also Testing data for Age. Train model using Training data and test using testing data"""
    model = LinearRegression()
    model.fit(X, y)
    y_pred = model.predict(X_test)
    return y_pred, model


#function to check the mean difference
def calc_prediction_error(y_test:np.ndarray, y_pred:np.ndarray)->float:
    """Recive the test data and predicted data for Spend, and calculate average difference between actual and predicted data"""
    mse = mean_squared_error(y_test, y_pred)
    rmse = np.sqrt(mse)
    return rmse

#function to plot chart from data
def plot_data_comparison(df:pd.DataFrame, model:LinearRegression):
    """Plot the comparision"""
    X = df[["Age"]].values
    y = df["Spend"].values
    y_pred = model.predict(X)
    plt.scatter(X, y , color="red", label="Actual")
    plt.title("Comparision: Actual vs Predicted")
    plt.plot(X, y_pred, color="blue", label="Predicted data")
    plt.xlabel("Age")
    plt.ylabel("Spend")
    plt.grid(True)
    plt.legend()
    plt.show()

#main function
try:   
    purchase_data = load_and_clean("purchases.csv")
    age_data, spend_data = prepare_data(purchase_data)
    age_data_train, spend_data_train, age_data_test, spend_data_test = train_and_test(age_data,spend_data)
    spend_data_pred, trained_model = predict_spend_data(age_data_train,spend_data_train,age_data_test)
    prediction_error = calc_prediction_error(spend_data_test, spend_data_pred)
    print(f"Error between prediction and actual data: {prediction_error}")
    plot_data_comparison(purchase_data, trained_model)
    
except Exception as e:
    print(f"Error : {e}")