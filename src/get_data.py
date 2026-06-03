# read params.yaml    
# process (on these params)
# read csv file and return dataframe to load_data.py
 
import os
import yaml
import pandas as pd
import argparse



def read_params(config_path): #only get open params.yaml file
    with open(config_path) as yaml_file:
        config = yaml.safe_load(yaml_file)
    return config

def get_data(config_path): #get params.yaml + its csv file 
    config = read_params(config_path)
    #print(config)
    data_path = config["data_source"]["s3_source"]
    #print(data_path)
    df = pd.read_csv(data_path, sep=',' , encoding= 'utf-8')
    #print(df.head())
    return df



if __name__ == "__main__":
    args = argparse.ArgumentParser()
    #e.g args.add_argument("--sameen", default="adil")
    args.add_argument("--config", default="params.yaml")
    #args.parse_args contain both values, we identity by .sameen and .config
    
    #args.parse_args()   store this in a variable
    #get_data(a=args.parse_args()) instead of write full write a(var)

    #var = args.parse_args() 
    #get_data(config_path= var.sameen) 

    #args.parse_args return whole object(e.g box of item) but with .config we get only one item
    data = get_data(config_path=args.parse_args().config)# short form
    #print(data)