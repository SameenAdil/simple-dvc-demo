#load the train and test csv files
#train algos
#save the metrics, params

import os
import warnings
import sys
import pandas as pd
import numpy as np
from sklearn.metrics import mean_squared_error, mean_absolute_error, r2_score
from sklearn.model_selection import train_test_split
from sklearn.linear_model import ElasticNet
from urllib.parse import urlparse
from get_data import read_params
import argparse
import joblib
import json



def save_metrics(actual,pred):
    mse= mean_squared_error(actual, pred)
    rmse= np.sqrt(mse)
    mae= mean_absolute_error(actual, pred)
    r2= r2_score(actual, pred)

    print("MSE: ", mse)
    print("RMSE: ",rmse)
    print("MAE: ", mae)
    print("R2: ", r2)
    #print(y_train.squeeze().min()) #squeeze convert df to series
    #print("Y_Train range ", y_train.squeeze().min(), "to ", y_train.squeeze().max())
    #print("Y_Test range ", y_test.squeeze().min(), "to ", y_test.squeeze().max())
    return rmse, mse,mae,r2


def train_and_evaluate(config_path):
    params_config= read_params(config_path)

    #Target_col=params_config["base"]["target_col"] return a single string
    Target_col=[params_config["base"]["target_col"]] #return a list that contain single string
    train_csv_path = params_config["split_data"]["train_path"]
    test_csv_path = params_config["split_data"]["test_path"]
    alpha_val=params_config["estimators"]["ElasticNet"]["params"]["alpha"]
    l1_val= params_config["estimators"]["ElasticNet"]["params"]["l1_ratio"]

    train_df = pd.read_csv(train_csv_path, sep="," , encoding='utf-8')
    test_df= pd.read_csv(test_csv_path, sep= ",", encoding='utf-8')

    x_train=train_df.drop(columns=Target_col) #axis=1 optional
    """columns=[target] wrong bcz target already return a list,
      then again pack in list, if target not pack in a list 
      then we can use  columns=[target]
      """
    y_train=train_df[Target_col]
    x_test=test_df.drop(Target_col, axis=1) #axis=1 compulsory
    y_test=test_df[Target_col]

    lr= ElasticNet(alpha=alpha_val, l1_ratio=l1_val, random_state=42)
    lr.fit(x_train, y_train)
    pred= lr.predict(x_test)
              #model y_test result stored in pred
     #compare original y_test result with model y_test
    (rmse,mse,mae,r2) = save_metrics(y_test,pred)
    

    #print(y_train.squeeze().min()) #squeeze convert df to series
    print("Y_Train range ", y_train.squeeze().min(), "to ", y_train.squeeze().max())
    print("Y_Test range ", y_test.squeeze().min(), "to ", y_test.squeeze().max())
    range1= y_test.squeeze().max() - y_test.squeeze().min()
    print("RMSE percentage",rmse/range1 *100)

    Model_dir = params_config["model_dir"]
    os.makedirs(Model_dir, exist_ok=True)
    model_path= os.path.join(Model_dir, "model.joblib")
    joblib.dump(lr, model_path)

    
    scores_file=params_config["reports"]["scores"]
    with open(scores_file, "w") as f:
        scores={"rmse":rmse, "mae":mae, "r2":r2  }
        json.dump(scores, f, indent=4)


    params_file=params_config["reports"]["params"]
    params={
            "l1_ratio": l1_val,
            "alpha": alpha_val
        }
    with open(params_file, "w") as f:
        json.dump(params, f, indent=4)
        

if __name__ == "__main__": 
    args = argparse.ArgumentParser()
    args.add_argument("--params_configs", default="params.yaml")
    var1 = args.parse_args()
    train_and_evaluate(config_path=var1.params_configs)
