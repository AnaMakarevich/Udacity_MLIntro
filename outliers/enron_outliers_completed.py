#!/usr/bin/python

import pickle
import sys
import matplotlib.pyplot
sys.path.append("../tools/")
from feature_format import feature_format, target_feature_split


# read in data dictionary, convert to numpy array
with open("../final_project/final_project_dataset.pkl", "rb") as f:
    data_dict = pickle.load(f)

data_dict.pop("TOTAL")
features = ["salary", "bonus"]
data = feature_format(data_dict, features)


# your code below
# matplotlib.pyplot.scatter(data[:, 0), data[:, 1])
print(data[:, 0].max())
print(data[:, 1].max())
for point in data:
    salary = point[0]
    bonus = point[1]
    matplotlib.pyplot.scatter(salary, bonus)

matplotlib.pyplot.xlabel("salary")
matplotlib.pyplot.ylabel("bonus")
matplotlib.pyplot.show()
