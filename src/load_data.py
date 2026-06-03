#read the data from data source
#save it in the data/raw folder for further process

import os
from get_data import read_params, get_data
import argparse

def load_and_save(config_path):
    config1 = read_params(config_path)
    df = get_data(config_path)
    new_cols = [col.replace(" ", "_")  for col in df.columns]
    #print(new_cols)
    #here i directly save new_cols in csv but i want to move/save csv in an other folder 
    #that's why i write this (below line)
    raw_data_path = config1["load_data"]["raw_dataset_csv"]
    df.to_csv(raw_data_path, sep="," , index=False, header=new_cols)



if __name__ == "__main__":
    args = argparse.ArgumentParser()
    args.add_argument("--coonfig", default="params.yaml")
    var=args.parse_args()
    load_and_save(config_path=var.coonfig) #call the func....more readable
    #load_and_save(var.coonfig)            #call the func

    #here  var is equal to {args.parse_args()}