#!/usr/bin/python


"""
    Starter code for the validation mini-project.
    The first step toward building your POI identifier!

    Start by loading/formatting the data

    After that, it's not our code anymore--it's yours!
"""

import pickle
import sys
sys.path.append("../tools/")
from feature_format import feature_format, target_feature_split

with open("../final_project/final_project_dataset.pkl", "rb") as f:
    data_dict = pickle.load(f)

# first element is our labels, any added elements are predictor
# features. Keep this the same for the mini-project, but you'll
# have a different feature list when you do the final project.
features_list = ["poi", "salary"]

data = feature_format(data_dict, features_list, sort_keys='../tools/python2_lesson13_keys.pkl')
labels, features = target_feature_split(data)

# it's all yours from here forward!

from sklearn.tree import DecisionTreeClassifier
# unvalidated
clf = DecisionTreeClassifier().fit(features, labels)
print(clf.score(features, labels))

# validated
from sklearn.model_selection import train_test_split
x_train, x_test, y_train, y_test = train_test_split(features, labels, random_state=42, test_size=0.3)
clf = DecisionTreeClassifier().fit(x_train, y_train)
print(clf.score(x_test, y_test))
