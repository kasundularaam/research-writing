# QUESTION
Were any data preprocessing techniques applied? If so, which ones?

# Research 1

Attribute selection (feature selection) was performed on the *training* data for each base learner and within the imbalanced learning methods (see the pseudo-code in the "Algorithm Evaluation" section). The specific attribute selection method used is not specified.

# Research 2

- Input feature selection (Chi-squared based)
- Data normalization (linear scaling to [0, 1] range)
- Data division (70% training, 30% testing, with one-third of training used for validation)

# Research 3

The paper mentions using Analyst4j to collect CK metrics and identify "bad smells" in the Eclipse code, which can be considered a form of data preprocessing.

# Research 4

    - The "BUG" feature (number of bugs) is transformed into a binary classification (defective/non-defective). No other preprocessing is explicitly mentioned in the excerpt. 

# Research 5

   * Data is normalized using Min-Max normalization to the range [0,1].

# Research 6

Parsing source code into ASTs using javalang
Mapping string tokens to integers
Handling class imbalance using random over-sampling
Deleting infrequent tokens

# Research 7

Stratified sampling was used to maintain class distribution during cross-validation.

# Research 8

Transformation of the "bug" variable into a binary classification (buggy/non-buggy).

# Research 9

The paper mentions that the NASA dataset was "sanitized", which likely involves some preprocessing, but the specific techniques are not detailed. For the Eclipse dataset, they mention aggregating class-level metrics to the package level.

# Research 10

The paper doesn't explicitly mention specific data preprocessing steps beyond feature selection.

# Research 11

Yes, K-means clustering was used as a preprocessing step before applying the decision tree algorithm.

# Research 12

Yes, the following data preprocessing techniques were used:

* Deletion of repeated entities
* Replacement of missing values using the average of the corresponding metric
* Data normalization using min-max normalization
* Data oversampling using SMOTETomek to address class imbalance 

# Research 13

Yes, the following preprocessing steps were applied:

* **Feature Removal:** Removed features with zero variance and instances with logically incorrect values.
* **Discretization:** Used the Fayyad and Irani algorithm to discretize continuous features for Bayesian learners that could not handle them. 
* **Error Count Discretization:** Converted error count to a binary value (0 for no errors, 1 for errors).

# Research 14

No specific mention, but aggregation of class and method level metrics to file and package levels is performed.

# Research 15

The paper mentions preprocessing, but it doesn't provide specifics. Common preprocessing steps in defect prediction include:

* Data cleaning: Handling missing values, removing duplicates.
* Data transformation:  Normalization or standardization of data.

# Research 16

The study doesn't explicitly mention specific data preprocessing techniques.

# Research 17

Yes, PCA was used for dimensionality reduction.

# Research 18

The paper doesn't explicitly mention any data preprocessing techniques besides the calculation of OO metrics and the mapping of change records to Java classes.

# Research 19

Feature selection is the core preprocessing technique studied in the paper. Stratified sampling is used to split the data into training and testing sets.

# Research 20

The paper doesn't explicitly mention specific data preprocessing techniques apart from creating the 5 folds for cross-validation.

# Research 21

Yes, min-max normalization (scaling values between 0 and 1) was applied.

# Research 22

Yes, the paper describes several preprocessing steps:
* Removing observations with null variance or logically erroneous data (e.g., zero lines of code).
* Converting the "error count" to a binary variable (0 for no error, 1 for error).
* Discretizing continuous features using the algorithm by Irani and Faiyad.

# Research 23

No specific data preprocessing techniques are mentioned besides the computation of change metrics from the raw data.

# Research 24

Log filtering: Attribute values were replaced with their logarithms.
Normalization: Data was normalized to the range [0, 1] for ANN (after PCA).

# Research 25

Min-max normalization was applied to the training and testing datasets.
Resampling techniques (SMOTE, Borderline-SMOTE, Safe-level SMOTE, ADASYN, Random Over Sampling, Random Under Sampling) were applied to the training data at various percentage of fault-prone modules (Pfp) levels.

# Research 26

Cleaning: The NASA MDP datasets were used in their "cleaned" versions where problematic and irrelevant data were removed. Normalization:  In the JIT datasets, LAn, LDn, LTn, and NUCn were normalized to avoid high correlation among features. Discretization: Continuous variables were discretized for use with Naive Bayes models, using AIC or BIC as the criterion.

# Research 27

Stratified sampling was used when creating subsets for cross-validation.
Discretization was applied to defect proneness, creating three states: defect-free, less defective, and more defective (for analysis with NOD).

# Research 28

 Faults that were not bugs were removed (reducing faults from 669 to 642).

# Research 29

Removal of duplicate instances

# Research 30

* Removed faults classified as "not a fault".
* Min-max normalization was applied to normalize input metric values to the range [0, 1].

