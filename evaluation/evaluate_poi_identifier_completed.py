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

from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import train_test_split
x_train, x_test, y_train, y_test = train_test_split(features, labels, random_state=42, test_size=0.3)
clf = DecisionTreeClassifier().fit(x_train, y_train)
preds = clf.predict(x_test)
print("Num POI: " + str(sum(preds)))
print("Num people: " + str(len(preds)))
print(clf.score(x_test, y_test))


def count_tp_fp_fn(preds, actual):
    tp = 0
    fp = 0
    fn = 0
    for pred, act in zip(preds, actual):
        if bool(pred) & bool(act):
            tp += 1
        if bool(pred) & (~bool(act)):
            fp += 1
        if ~bool(pred) & bool(act):
            fn += 1
    return tp, fp, fn


tp, fp, fn = count_tp_fp_fn(preds, y_test)
print("True positives: " + str(tp))

from sklearn.metrics import precision_score, recall_score
print("Precision: " + str(precision_score(y_test, preds)))
print("Recall: " + str(recall_score(y_test, preds)))

# manual exercise
predictions = [0, 1, 1, 0, 0, 0, 1, 0, 1, 0, 0, 1, 0, 0, 1, 1, 0, 1, 0, 1]
true_labels = [0, 0, 0, 0, 0, 0, 1, 0, 1, 1, 0, 1, 0, 1, 1, 1, 0, 1, 0, 0]

tp, fp, fn = count_tp_fp_fn(predictions, true_labels)
precision = tp/(tp + fp)
print("Precision: " + str(precision))
recall = tp/(tp + fn)
print("Recall: " + str(recall))


