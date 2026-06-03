import argparse
import pandas as pd
from get_data import read_params
from sklearn.model_selection import train_test_split


def split_data(config_path):
    params_config = read_params(config_path)
    csv_file= params_config["load_data"]["raw_dataset_csv"]
    df = pd.read_csv(csv_file, sep="," , encoding="utf-8" )
    #print(df.head(7))
    train_data, test_data = train_test_split(df, test_size=0.2, random_state=42)
    #print(train_data.shape)
    #print(test_data.shape)
    train_file_path= params_config["split_data"]["train_path"]
    test_file_path= params_config["split_data"]["test_path"]
    #print(train_file_path)
    train_data.to_csv(train_file_path, sep=',' , index=False, encoding='utf-8')
    test_data.to_csv(test_file_path, sep=',' , index=False, encoding='utf-8')

if __name__ == "__main__":

    args = argparse.ArgumentParser()
    args.add_argument("--config", default="params.yaml")
    var = args.parse_args() 
    split_data(config_path=var.config) # short form 
