# -*- coding: utf-8 -*-
"""
Created on Mon Feb  4 14:31:27 2019

@author: anurag
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
#all parameters
filename = "Florida_Complete_data.csv"
outcome = "Disability Type"

pd.set_option('max_columns', 120)
pd.set_option('max_colwidth', 5000)




plt.rcParams['figure.figsize'] = (12,8)

# skip row 1 so pandas can parse the data properly. But not skipping here.
accidents = pd.read_csv(filename, skiprows=0, low_memory=False)
#counts of independent variable
len(list(accidents.columns))
accidents["Body Part Code"].value_counts()
len(accidents["Cause of Injury Code"].unique())

