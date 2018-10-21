# THIS FILE IS USED TO SAVE THE LINEAR SVC CLASSIFIER FILE


import pickle
from sklearn import cross_validation
from sklearn.metrics import accuracy_score
from sklearn.metrics import confusion_matrix
from sklearn.svm import LinearSVC
from sklearn.svm import SVC
import numpy as np
import matplotlib.pyplot as plt

features = pickle.load(open('features'))
labels = pickle.load(open('labels'))

X_train, X_test, y_train, y_test = cross_validation.train_test_split(features,
                                                                     labels,
                                                                     test_size=0.2,
                                                                     random_state=42)

clf1 = LinearSVC(C=1.0, loss='l2', penalty='l2', multi_class='ovr')
clf2 = SVC(kernel='linear', probability=True)

clf1.fit(X_train, y_train)
clf2.fit(X_train, y_train)


# Save the classifier model to disk
filename = 'SVC_Classifier_Probabilities.sav'
pickle.dump(clf2, open(filename, 'wb'))

filename = 'SVC_Classifier.sav'
pickle.dump(clf1, open(filename, 'wb'))

# Load the model from the disk
loaded_model = pickle.load(open(filename, 'rb'))
