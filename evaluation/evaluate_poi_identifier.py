#!/usr/bin/python


"""
    Starter code for the evaluation mini-project.
    Start by copying your trained/tested POI identifier from
    that which you built in the validation mini-project.

    This is the second step toward building your POI identifier!

    Start by loading/formatting the data...
"""

import pickle
import sys
sys.path.append("../tools/")
from feature_format import feature_format, target_feature_split

with open("../final_project/final_project_dataset.pkl", "rb") as f:
    data_dict = pickle.load(f)

# add more features to features_list!
features_list = ["poi", "salary"]

data = feature_format(data_dict, features_list, sort_keys='../tools/python2_lesson13_keys.pkl')
labels, features = target_feature_split(data)

# your code goes here
