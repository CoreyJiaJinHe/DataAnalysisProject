import warnings
warnings.filterwarnings("ignore", category=DeprecationWarning)

import pandas as pd
import numpy as py

header=pd.read_csv('.\data\StudentAcademicSuccess\data.csv',nrows=1)


print(header.head())

df=pd.read_csv('.\data\StudentAcademicSuccess\data.csv',skiprows=1)

#df.shape()