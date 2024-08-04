# QUESTION
Was cross-validation used? If so, what type and how many folds?

# Research 1

Yes, 10 x 10-fold cross-validation was used. This means that each dataset was divided into 10 folds, and the process was repeated 10 times with different random fold assignments.

# Research 2

Yes, k-fold cross-validation is used in the EP-based ensemble approach to estimate classification accuracy and optimize ensemble weights (Section 3.4). The specific value of *k* (number of folds) is not explicitly stated.

# Research 3

Not mentioned.

# Research 4

   - Yes, **10 × 10-fold cross-validation** is used for all experiments.

# Research 5

20-fold cross-validation was used to evaluate and compare the models.

# Research 6

SPSC dataset: 30-holdout repeated experiments
PSC dataset: 10 x 10 cross-validation

# Research 7

Yes, stratified 10-fold cross-validation was used.

# Research 8

Not explicitly mentioned. Experiments were repeated 50 times with different data subsets for robustness.

# Research 9

Yes, 10-fold cross-validation was used.

# Research 10

Yes, 10-fold cross-validation was used.

# Research 11

Yes, 10-fold cross-validation was used.

# Research 12

The paper mentions that each dataset was divided into ten sub-datasets (with the same imbalance rate of 10%). This could be interpreted as a form of 10-fold cross-validation, but it's not explicitly stated.

# Research 13

* Yes, the paper mentions using 5-fold stratified cross-validation for tuning the MMHC algorithm.
* For evaluating the classifiers, the datasets were randomly partitioned into training (2/3) and test (1/3) sets 10 times using stratified sampling to account for potential sampling bias.

# Research 14

Yes, across different releases of Eclipse (training on one release and testing on another).

# Research 15

Yes, the paper mentions using 10-fold cross-validation for experiments without feature selection.  For experiments with feature selection, it uses 30-fold cross-validation.

# Research 16

The paper doesn't explicitly mention the use of cross-validation.

# Research 17

Yes, 10-fold cross-validation

# Research 18

Yes, 10-fold cross-validation was used.

# Research 19

Yes, 3-fold cross-validation is used during the training process of MOFES. 10-fold cross-validation is used to evaluate the performance of MOFES and baseline methods.

# Research 20

Yes, they used **5-fold cross-validation**.

# Research 21

Yes, N-fold cross-validation was used.
* 5 folds for datasets with defect rate < 10%
* 7 folds for datasets with defect rate between 10% and 15%
* 10 folds for datasets with defect rate ≥ 15%

# Research 22

Yes, the paper mentions partitioning data into training (2/3) and testing (1/3) sets and iterating this 10 to 15 times to avoid sampling bias. This suggests a form of **repeated holdout cross-validation**.

# Research 23

Yes, 10-fold cross-validation was used.

# Research 24

Yes, 10 * 10-fold stratified cross-validation was employed.

# Research 25

10-fold cross-validation was used during model construction for parameter optimization.

# Research 26

5-fold cross-validation, repeated 5 times (25 total iterations) with different random data partitions.

# Research 27

Yes, 10-fold cross-validation was used, and the experiments were repeated on 20 different 2/3rd subsets of each dataset to mitigate conclusion instability (see Section 5.3).

# Research 28

Yes, 10-fold cross-validation was used.

# Research 29

Not mentioned, likely not used.

# Research 30

Yes, 10-fold cross-validation was used.

