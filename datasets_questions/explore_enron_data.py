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

enron_data = pickle.load(open("../final_project/final_project_dataset.pkl", "r"))
v1 = 0
sal_ct = 0

for i in enron_data:
	# if enron_data[i]['poi'] == 1:
	# 	poi_ct += 1
	# if i == 'PRENTICE JAMES':
	# 	print enron_data[i]
	# if i == 'COLWELL WESLEY':
	# 	print enron_data[i]
	# for word in ['LAY', 'SKILLING', 'FASTOW']:
	# 	if i.find(word) > -1:
	# 		print enron_data[i]
	if enron_data[i]['salary'] != 'NaN':
		sal_ct += 1
	if enron_data[i]['email_address'] != 'NaN':
		v1 += 1

print sal_ct, v1