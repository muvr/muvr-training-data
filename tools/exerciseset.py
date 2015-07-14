from __future__ import print_function
import os
import fnmatch
import sys
import random
import numpy as np
import pylab as pl

musclegroups = {
    'aerobic': 1,
    'arms': 2,
    'back': 3,
    'chest': 4,
    'core': 5,
    'shoulders': 6,
}

moves = {
    'alt-dumbbell-biceps-curl': 1,
    'angle-chest-press': 2,
    'barbel-biceps-curl': 3,
    'barbell-biceps-curl': 3,
    'barbell-press': 5,
    'biceps-curl': 6,
    'biceps-curl-hammer': 7,
    'biceps-curl-happer': 7,
    'cable-cross-overs': 9,
    'cable-deltoid-cross-overs': 10,
    'deltoid-row': 11,
    'dumbbell-biceps-curl': 12,
    'dumbbell-chest-fly': 13,
    'dumbbell-chest-press': 14,
    'dumbbell-front-rise': 15,
    'dumbbell-press': 16,
    'dumbbell-row': 17,
    'dumbbell-side-rise': 18,
    'dummbell-chest-press-twist': 19,
    'lat-pulldown-angled': 20,
    'lat-pulldown-straight': 21,
    'leverage-high-row': 22,
    'overhead-pull': 23,
    'pulldown-crunch': 24,
    'rope-biceps-curl': 25,
    'rope-triceps-extension': 26,
    'rowing': 27,
    'side-dips': 28,
    'squat': 29,
    'straight-bar-biceps-curl': 30,
    'straight-bar-triceps-extension': 31,
    'tricep-dips': 32,
    'triceps-dips': 32,
    'twist': 34,
}

max_mean = 1100
min_mean = -1100
max_std = 900
min_std = 0

csv_converters = {
    0: lambda x: musclegroups.get(x, 0),
    1: lambda x: moves.get(x, 0),
}

def find_csv_files(filepath):
    for root, dirnames, filenames in os.walk(filepath):
        for filename in fnmatch.filter(filenames, '*.csv'):
            yield os.path.join(root, filename)

def data_from_csv(filename):
    return np.genfromtxt(
            filename, delimiter=',', usecols=(0, 1, -3, -2, -1),
            converters=csv_converters, dtype=int)

def arr_to_csv(a):
    return ','.join([str(x) for x in a])

def scale_array(a, low, high):
    return (a - low) / (high - low)

def attributes_from_array(a):
    # Assuming that the array contains only one kind of exercise move
    musclegroup = a[0][0]
    move = a[0][1]

    x_mean = scale_array(a[:,2].mean(), min_mean, max_mean)
    y_mean = scale_array(a[:,3].mean(), min_mean, max_mean)
    z_mean = scale_array(a[:,4].mean(), min_mean, max_mean)
    x_std = scale_array(a[:,2].std(), min_std, max_std)
    y_std = scale_array(a[:,3].std(), min_std, max_std)
    z_std = scale_array(a[:,4].std(), min_std, max_std)

    return np.array(
        (musclegroup * 100 + move,
            x_mean, y_mean, z_mean,
            x_std, y_std, z_std))

def attributes_from_csvfile(filename):
    data = data_from_csv(filename)
    first = data[0]

    if 0 in first[0:2]:  # Is the muscle group and move known?
        return None

    return attributes_from_array(data)

def attributes_from_csvfiles(filenames):
    arrays = (attributes_from_csvfile(csv) for csv in filenames)
    arrays = [a for a in arrays if a is not None]  # Filter empty values out
    return np.array(arrays)

if __name__ == '__main__':
    csvpath = sys.argv[1]
    csvpaths = find_csv_files(csvpath)

    for csvfile in csvpaths:
        attrs = attributes_from_csvfile(csvfile)
        if attrs is not None:
            print(arr_to_csv(attrs))

