# muvr-training-data

This repository is a collection of training datasets used for analysis and model training during model evaluation. 
Newly added datasets should be listed here including there format and a short description.

Some of the datasets might be zipped since they would be to big otherwise.

## (partial) List of available datasets

#### combined

| name                                         	| format                 	| zipped 	| split    	| comment                                                                	|
|----------------------------------------------	|------------------------	|:------:	|----------	|------------------------------------------------------------------------	|
| 09-09-15-activity-slacking.zip      	| combined-1200          	|    x   	| presplit 	| Collection of movement data (walking, still, other) vs. exercise data. 	|
| 18-09-15-triceps-biceps-lateral.zip 	| single-exercise-simple 	|    x   	|          	| Collection of three exercises.                                         	|
| combined-tbl-activity-slacking.zip  	| single-exercise-simple 	|    x   	| presplit 	| Combination of 09-09-15-activity-slacking.zip and                      	|

#### labelled
Jan's collected exercises. Contains `raw-acceleration` and `single-exercise-extended` data files. Not all `raw` files have been converted.

#### raw
Unlabeled data in `raw-acceleration` format.

## Format descriptions

#### raw-acceleration
The dataset is a collection of **unlabeled** acceleration data, one file per exercise. A file for an exercise contains dumped sensor data in an array like format

#### single-exercise-simple
The dataset is a collection of **labeled** data, one file per exercise. A file for an exercise is in CSV format and there is one row per measurement:
```
exercise group | exercise name | x | y | z |
```

#### single-exercise-extended
The dataset is a collection of **labeled** data, one file per exercise. A file for an exercise is in CSV format and there is one row per measurement:
```
exercise group | exercise name | <unknown> | intensity? | weight | x | y | z |
```

#### combined-1200
The dataset is a collection of **labeled** data in a single file. The file is in CSV and there is one row per example:
```
label | X1 | X2 | ... | X400  | Y1 | Y2 | ... | Y400   | Z1 | Z2 | ... | Z400 
```
