#!/usr/bin/python

import pickle
import sys
import matplotlib.pyplot
sys.path.append("../tools/")
from feature_format import feature_format, target_feature_split


# read in data dictionary, convert to numpy array
with open("../final_project/final_project_dataset.pkl", "rb") as f:
    data_dict = pickle.load(f)

features = ["salary", "bonus"]
data = feature_format(data_dict, features)


# your code below



