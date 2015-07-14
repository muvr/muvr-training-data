from __future__ import print_function
import os
import fnmatch
import sys
import random
import numpy as np
import pylab as pl
from sklearn import svm
from sklearn import cross_validation
import exerciseset as eset

def exerciseset_to_svm(exerciseset):
    data = exerciseset[:,1:]
    target = exerciseset[:,0]
    for test_size in np.arange(0.1, 0.8, 0.1):
        rand_state = random.randint(0, 1000)
        d_train, d_test, t_train, t_test = cross_validation.train_test_split(
                data, target, test_size=test_size, random_state=rand_state)
        clf = svm.SVC(kernel='linear', C=10).fit(d_train, t_train)
        score = clf.score(d_test, t_test)
        print('Test size: %.2f; Random state: %d; Score: %f' % (test_size, rand_state, score))

if __name__ == '__main__':
    csvpath = sys.argv[1]
    print('Searching for CSV files on path: %s' % csvpath)
    csvpaths = eset.find_csv_files(csvpath)
    print('Extracting attributes')
    exerciseset = eset.attributes_from_csvfiles(csvpaths)
    print('Calculating SVM model')
    exerciseset_to_svm(exerciseset)

