#!/usr/bin/python

""" 
    This is the code to accompany the Lesson 2 (SVM) mini-project.

    Use a SVM to identify emails from the Enron corpus by their authors:    
    Sara has label 0
    Chris has label 1
"""
    
import sys
from time import time
sys.path.append("../tools/")
from email_preprocess import preprocess


### features_train and features_test are the features for the training
### and testing datasets, respectively
### labels_train and labels_test are the corresponding item labels
features_train, features_test, labels_train, labels_test = preprocess()


print(type(features_train))
#features_train =  features_train.astype('int')
#labels_train = labels_train.astype('int')


features_train = features_train[:len(features_train)//100] 
labels_train = labels_train[:len(labels_train)//100] 

#########################################################
### your code goes here ###

for i in [10,26,50]:
	from sklearn import svm
	clf = svm.SVC(kernel='rbf', C=10000)

	print(len(features_train))
	print(len(features_test))
	print(len(labels_train))
	print(len(labels_test))

	t0 = time()
	clf.fit(features_train, labels_train)
	print ("training time:", round(time()-t0, 3), "s")

	accuracy = clf.score(features_test, labels_test)

	print("Accuracy:", round(accuracy,5))

	#import matplotlib.pyplot as plt
	#from adspy_shared_utilities import plot_class_regions_for_classifier_subplot
	#fig, subaxes = plt.subplots(1, 1, figsize=(7, 5))
	#title = 'Linear SVC, C = {:.3f}'.format(cvalue)
	#plt.plot(clf, features_train, labels_train, title)
	pred = clf.predict(labels_test)
	answer=pred[i]



#########################################################


