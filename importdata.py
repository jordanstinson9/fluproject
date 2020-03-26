import sys
import os
import pandas as pd
import numpy as np
from scipy import stats

BASE_DIR = os.getcwd()

# Change to the data download directory
# Assumes downloaded files are in the /geo folder
BASE_DIR = os.getcwd()
geo = os.path.join(BASE_DIR,"geo")

# Import data into pandas dataframe and save as csv files in /data folder
for file in os.listdir(geo):
    print(file)
    if file.startswith("i"):
        tempdata = pd.read_table(os.path.join(geo,file), sep='\t')
        csvtitle = str(file).replace('txt','csv')
        tempdata.to_csv(os.path.join("data",csvtitle),index=False)
