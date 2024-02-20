#GO TO COMMAND LINE TERMINAL. THE VENV SHOULD BE SAVED.
#STOP BEING AN IDIOT. THIS IS NOT FIRST TIME SETUP.

import warnings
warnings.filterwarnings("ignore", category=DeprecationWarning)

import pandas as pd
import numpy as py

header=pd.read_csv('.\data\StudentAcademicSuccess\data.csv',nrows=1)


print(header.head())

df=pd.read_csv('.\data\StudentAcademicSuccess\data.csv',skiprows=1)
data_head = df.head()




# I have entered the system
#df.shape()