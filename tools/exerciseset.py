from __future__ import print_function
import sys
import glob
import numpy as np
import pylab as pl

moves = [
    'unknown',
    'alt-dumbbell-biceps-curl',
    'angle-chest-press',
    'barbel-biceps-curl',
    'barbell-biceps-curl',
    'barbell-press',
    'biceps-curl',
    'biceps-curl-hammer',
    'biceps-curl-happer',
    'cable-cross-overs',
    'cable-deltoid-cross-overs',
    'deltoid-row',
    'dumbbell-biceps-curl',
    'dumbbell-chest-fly',
    'dumbbell-chest-press',
    'dumbbell-front-rise',
    'dumbbell-press',
    'dumbbell-row',
    'dumbbell-side-rise',
    'dummbell-chest-press-twist',
    'lat-pulldown-angled',
    'lat-pulldown-straight',
    'leverage-high-row',
    'overhead-pull',
    'pulldown-crunch',
    'rope-biceps-curl',
    'rope-triceps-extension',
    'rowing',
    'side-dips',
    'squat',
    'straight-bar-biceps-curl',
    'straight-bar-triceps-extension',
    'tricep-dips',
    'triceps-dips',
    'twist',
]

# Mapping table for all the moves
moves_map = { m: i for i, m in enumerate(moves) }

def data_from_csv(filename):
    return np.genfromtxt(
            filename, delimiter=',', usecols=(1, -3, -2, -1),
            converters={1: lambda x: moves_map.get(x, 0)}, dtype=int)

def extract_classifiers(a):
    move = a[0][0]  # Assuming that the array contains only one kind of exercise move
    x_mean = a[:,1].mean()
    y_mean = a[:,2].mean()
    z_mean = a[:,3].mean()
    x_std = a[:,1].std()
    y_std = a[:,2].std()
    z_std = a[:,3].std()
    return (move, x_mean, y_mean, z_mean, x_std, y_std, z_std)

def classifiers_from_csv(filename):
    try:
        data = data_from_csv(csvfile)
        c = extract_classifiers(data)
        cs = ','.join([str(x) for x in c])
        yield cs
    except ValueError:
        print("Failed to process file %s: %s" % csvfile, file=sys.stderr)


# Scan the given directory for CSV files, generate classifiers, and print them to STDOUT in CSV format
if __name__ == '__main__':
    csvpaths = glob.glob(sys.argv[1] + '/**/*.csv')
    for csvfile in csvpaths:
        for cs in classifiers_from_csv(csvfile):
            print(cs)

