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

# What features are available in this dataset?
print(enron_data[list(enron_data.keys())[0]].keys())

# For each person, how many features are available?
print("For each person, how many features are available?", \
	len(list(enron_data.values())[0]))
print("For each person, how many features are available?", 
	len(enron_data[list(enron_data.keys())[0]].keys()))

# The “poi” feature records whether the person is a person of interest, 
# How many POIs are there in the E+F dataset?
count = 0
for i in enron_data:
	if enron_data[i]["poi"] == 1:
		count += 1
print("How many POIs are there in the E+F dataset?", count)
print("How many email messages do we have from Wesley Colwell to persons of interest?", \
        enron_data['COLWELL WESLEY']['from_this_person_to_poi'])

# How Many POIs Exist?
poi_text = '/Users/yechenhua/version-control/ud120-projects/final_project/poi_names.txt'
poi_names = open(poi_text, 'rb')
fr = poi_names.readlines()
print("How many POI’s were there total?",len(fr[2:]))
poi_names.close()

## addition method to find file length. print poi_names.read()
num_lines = sum(1 for line in open(poi_text))
print("file length:",num_lines)

def file_len(fname):
    with open(fname) as f:
        for i, l in enumerate(f):
            pass
    return i + 1

print("file length:",file_len('/Users/yechenhua/version-control/ud120-projects/final_project/poi_names.txt'))

## Check if values exist in any string in the list
matching = [s for s in enron_data.keys() if "PRENTICE" in s]
print(matching)

#What is the total value of the stock belonging to James Prentice?
print("What is the total value of the stock belonging to James Prentice?",
        enron_data['PRENTICE JAMES']['total_stock_value'])

#How many email messages do we have from Wesley Colwell to persons of interest?
print("How many email messages do we have from Wesley Colwell to persons of interest?",
        enron_data['COLWELL WESLEY']['from_this_person_to_poi'])

#What’s the value of stock options exercised by Jeffrey Skilling?
print("What’s the value of stock options exercised by Jeffrey Skilling?",
        enron_data['SKILLING JEFFREY K']['exercised_stock_options'])

# Sort values
sorted(enron_data.keys())

# How much money did that person get?
print("How much money did that person get?",enron_data['SKILLING JEFFREY K']['total_payments'])
print("How much money did that person get?",enron_data['FASTOW ANDREW S']['total_payments'])
print("How much money did that person get?",enron_data['LAY KENNETH L']['total_payments'])

# How is an unfilled feature denoted?
print("How is an unfilled feature denoted?",enron_data['FASTOW ANDREW S']['deferral_payments'])

#How many folks in this dataset have a quantified salary? What about a known email address?
salary = 0
for i in enron_data:
	if enron_data[i]["salary"] != 'NaN' :
		salary += 1
print("How many folks in this dataset have a quantified salary?",salary)

email = 0
for i in enron_data:
	if enron_data[i]["email_address"] != 'NaN' :
		email += 1
print("How many folks in this dataset have a quantified salary?",email)

#from feature_format import featureFormat
#from feature_format import targetFeatureSplit

# How many people in the E+F dataset (as it currently exists) have “NaN” for their total payments?
# What percentage of people in the dataset as a whole is this?
count_NaN_tp = 0
for key in enron_data.keys():
    if enron_data[key]['total_payments'] == 'NaN':
        count_NaN_tp+=1
print("How many people in the E+F dataset (as it currently exists) have “NaN” for their total payments?",count_NaN_tp)
print("What percentage of people in the dataset as a whole is this?",float(count_NaN_tp)/len(enron_data.keys()))
        
# How many POIs in the E+F dataset have “NaN” for their total payments? 
# What percentage of POI’s as a whole is this?   
count_NaN_tp = 0
for key in enron_data.keys():
    if enron_data[key]['total_payments'] == 'NaN' and enron_data[key]['poi'] == True :
        print 
        count_NaN_tp+=1
print("How many POIs in the E+F dataset have “NaN” for their total payments? ",count_NaN_tp)
print("What percentage of POI’s as a whole is this?",float(count_NaN_tp)/len(enron_data.keys()))





