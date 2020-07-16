# This is part one code for Data Exploration.

# import packages
import matplotlib as mpl
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd


# Load the Data

filename = './1586540818_05152020_updated_ski_data_-_updated_ski_data.csv'
info = pd.read_csv(filename)

# Let us explore the dataset
info.shape
info.columns

# Let us clean the dataset base on the information needed. 
info = info.reset_index()
info.head()

# Rename the columns
info.index
info.head()
info.columns

#do  something