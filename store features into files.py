# THIS FILE IS INITIALLY USED TO CREATE .PB FILE

import os
import re

import tensorflow as tf

from tensorflow.python.framework import tensor_shape
from tensorflow.python.platform import gfile

sess = tf.Session()

import tensorflow.python.platform
from tensorflow.python.platform import gfile
import numpy as np
import pandas as pd
import sklearn
from sklearn import cross_validation
from sklearn.metrics import accuracy_score, confusion_matrix
from sklearn.svm import SVC, LinearSVC
import matplotlib.pyplot as plt
import pickle

model_dir = 'imagenet'
images_dir = 'images/'
list_images = [images_dir + f for f in os.listdir(images_dir) if
               re.search('jpeg|JPEG', f)]


# To use TensorFlow, you should define a graph that represents the
# description of computations. Then these computations will be executed
# within what is called sessions


def create_graph():
    with gfile.FastGFile(os.path.join(
            model_dir, 'classify_image_graph_def.pb'), 'rb') as f:
        graph_def = tf.GraphDef()
        graph_def.ParseFromString(f.read())
        _ = tf.import_graph_def(graph_def, name='')


def extract_features(list_images):
    nb_features = 2048
    features = np.empty((len(list_images), nb_features))
    labels = []

    create_graph()

    with tf.Session() as sess:
        next_to_last_tensor = sess.graph.get_tensor_by_name('pool_3:0')

    for ind, image in enumerate(list_images):
        image_data = gfile.FastGFile(image, 'rb').read()
        predictions = sess.run(next_to_last_tensor,
                               {'DecodeJpeg/contents:0': image_data})
        features[ind, :] = np.squeeze(predictions)
        labels.append(re.split('_\d+', image.split('/')[1])[0])

    return features, labels


features, labels = extract_features(list_images)
pickle.dump(features, open('features', 'wb'))
pickle.dump(labels, open('labels', 'wb'))
features = pickle.load(open('features'))
labels = pickle.load(open('labels'))

X_train, X_test, y_train, y_test = cross_validation.train_test_spIlit(features,
                                                                      labels,
                                                                      test_size=0.2,
                                                                      random_state=42)

clf = LinearSVC(C=1.0, loss='l2', penalty='l2', multi_class='ovr')
clf.fit(X_train, y_train)
y_pred = clf.predict(X_test)


with tf.Session() as sess:
    output_filename = 'output_graph_2.pb'
    output_graph_def = sess.graph.as_graph_def()
    with gfile.FastGFile(output_filename, 'wb') as f:
        f.write(output_graph_def.SerializeToString())
