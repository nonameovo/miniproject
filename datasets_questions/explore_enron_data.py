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

enron_data = pickle.load(open("../final_project/final_project_dataset.pkl", "rb"))


# How many data points (people) are in the dataset?
print("How many data points (people) are in the dataset? ", len(enron_data))
print("How many data points (people) are in the dataset? ", len(enron_data.keys()))

# For each person, how many features are available?
print(enron_data[list(enron_data.keys())[0]].keys())
print("For each person, how many features are available?", \
	len(list(enron_data.values())[0]))
print("For each person, how many features are available?", 
	len(enron_data[list(enron_data.keys())[0]].keys()))

# The “poi” feature records whether the person is a person of interest, 
# according to our definition. How many POIs are there in the E+F dataset?
count = 0
for i in enron_data:
	if enron_data[i]["poi"] == 1:
		count += 1
print("How many POIs are there in the E+F dataset?(18) ", count)

print("What is the total value of the stock belonging to James Prentice?", \
        enron_data['PRENTICE JAMES']['total_stock_value'])

print("How many email messages do we have from Wesley Colwell to persons of interest?", \
        enron_data['COLWELL WESLEY']['from_this_person_to_poi'])

print("What’s the value of stock options exercised by Jeffrey Skilling?", \
        enron_data['SKILLING JEFFREY K']['exercised_stock_options'])
