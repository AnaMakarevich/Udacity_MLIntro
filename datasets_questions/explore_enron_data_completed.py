#!/usr/bin/python

""" 
    Starter code for exploring the Enron dataset (emails + finances);
    loads up the dataset (pickled dict of dicts).

    The dataset has the form:
    enron_data["LASTNAME FIRSTNAME MIDDLEINITIAL"] = { features_dict }

    {features_dict} is a dictionary of features associated with that person.
    You should explore features_dict as part of the mini-project,
    but here's an example to get you started:

    enron_data["SKILLING JEFFREY K"]["bonus"] = 5600000
    
"""

import pickle
import pandas as pd

enron_data = pickle.load(open("../final_project/final_project_dataset.pkl", "rb"))
df = pd.DataFrame(enron_data).T
print("Number of people: " + str(len(df)))
print("Number of features: " + str(len(df.columns)))
print(df.columns)
print("Number of poi: " + str((df.poi == 1).sum()))
print(df[df.index.str.contains("PRENTICE JAMES")].total_stock_value)
print(df[df.index.str.contains("COLWELL WESLEY")].from_this_person_to_poi)
print(df[df.index.str.contains("SKILLING JEFFREY K")].exercised_stock_options)
print(df[df.index.str.contains("SKILLING", ) | df.index.str.contains("LAY") |
         df.index.str.contains("FASTOW")].total_payments)
print("Valid salaries: " + str((df.salary != "NaN").sum()))
print("Valid salaries: " + str((df.email_address != "NaN").sum()))
print("Percentage of Nan total payments: " + str(((df.total_payments == "NaN").sum()/len(df))*100))
print("Number of Nan total payments: " + str(((df[df.poi == 1].total_payments == "NaN").sum())))

