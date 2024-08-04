# QUESTION
What machine learning technique(s) were employed in the study? (List all)

# Research 1

* **Traditional Learners (Base Classifiers):**
    * C4.5 (Decision Tree)
    * RF (Random Forest)
    * SVM (Support Vector Machine, using SMO implementation)
    * Ripper (Rule-based)
    * IBk (Instance-based k-Nearest Neighbor)
    * LR (Logistic Regression)
    * NB (Naïve Bayes)
* **Imbalanced Learning Methods:** 
    * Bag (Bagging)
    * Bst (Boosting) 
    * US (Under-Sampling)
    * OS (Over-Sampling)
    * UOS (UnderOver-Sampling)
    * SMOTE (Synthetic Minority Oversampling Technique)
    * COS (Cost-Sensitive Learning)
    * EM1v1 (Ensemble method with splitting and coding techniques)
    * UBag (UnderBagging)
    * OBag (OverBagging)
    * UOBag (UnderOverBagging)
    * SBag (SMOTEBagging)
    * UBst (UnderBoosting)
    * OBst (OverBoosting)
    * UOBst (UnderoverBoosting)
    * SBst (SMOTEBoosting)
    * Plus a "Null" imbalanced method (doing nothing) as a benchmark

# Research 2

Logistic Regression (LogR)
k-Nearest Neighbor (KNN)
C4.5 Decision Tree
Standard Support Vector Machine (SVM)
Least Squares Support Vector Machine (LSSVM)
Asymmetric Weighted LSSVM (AW-LSSVM)
Ensemble methods:
Majority Voting
Total Accuracy (TA)-based Weighted Averaging
Evolutionary Programming (EP) based ensemble (proposed)

# Research 3

* **Logistic Regression:** Used to analyze the relationship between bad smells and fault proneness.
* **Bayesian Inference:**  Employed to combine prior knowledge (prior distributions on metrics) with observed data (likelihood from the Eclipse dataset) to build posterior distributions for fault prediction.

# Research 4

 - Naive Bayes (NB)
   - Weighted Naive Bayes (WNB) with various feature weighting techniques:
     - Chi-square (CS)
     - Information Gain (IG)
     - Gain Ratio (GR)
     - Symmetrical Uncertainty (SU)
     - ReliefF (RF)
     - Information Flow (IF)
   - Naive Bayes with Information Diffusion (NB-ID)
   - Proposed method: Weighted Naive Bayes with Information Diffusion (WNB-ID)
   - Support Vector Machine (SVM)
   - Logistic Regression (LR)
   - Random Tree (RT)
   - State-of-the-art ensemble method (STSE) - details not fully provided in the excerpt. 

# Research 5

Least Squares Support Vector Machine (LSSVM) with three different kernel functions:
   * Linear kernel
   * Polynomial kernel
   * Radial Basis Function (RBF) kernel

# Research 6

Convolutional Neural Network (CNN) - proposed improved model
Deep Belief Network (DBN) - used as baseline
CNN -  Li's CNN model used as a baseline
Traditional machine learning models - used as baselines for the PSC dataset:
    * Decision Tree (DT)
    * Logistic Regression (LR)
    * Naïve Bayes (NB)
    * Random Forest (RF)
    * RBF Network (NET)
RANDOM model - predicts buggy at a probability of 0.5
FIX model - predicts all files as buggy

# Research 7

["Average Probability Ensemble (APE)", "Weighted Support Vector Machines (W-SVMs)", "Random Forests"]

# Research 8

Naïve Bayes (NB), Support Vector Machine (SVM), Logistic Regression (LR), Random Tree (RT), Diffused Bayes (DB) - Proposed novel technique

# Research 9

Support Vector Machine (SVM)
Bagged Ensemble of Support Vector Machines (Bagged SVM)

# Research 10

* Decision Tree (DT)
* Random Forest (RF)
* Naïve Bayes (NB)
* Support Vector Machine (SVM)
* Artificial Neural Network (ANN)
* Adaboost

# Research 11

* K-means clustering: Used as a preprocessing technique.
* Decision Tree (C4.5 algorithm): Used for fault prediction.

# Research 12

SDNN (Siamese Dense Neural Network), SDNN¯ (SDNN without cosine-proximity in the metering function), DNN (Deep Neural Network), LSTM (Long Short-Term Memory network), DBN (Deep Belief Network), LR (Logistic Regression), BAG (Bagging), NB (Naive Bayes), TNB (Transfer Naive Bayes), DTB (Double Transfer Boosting)

# Research 13

The study employed a variety of machine learning techniques:

**Bayesian Network Classifiers:**
* Naive Bayes (with kernel density estimate and with variable discretization)
* Tree Augmented Naive Bayes (TAN)
* Forest Augmented Naive Bayes (FAN)
* Selective Tree Augmented Naive Bayes (STAN)
* Selective Tree Augmented Naive Bayes with Discarding (STAND)
* Selective Forest Augmented Naive Bayes (SFAN)
* Selective Forest Augmented Naive Bayes with Discarding (SFAND)
* K2
* Max-Min Hill-Climbing (MMHC)

**Benchmark Classifiers:**
* Random Forests (RndFor)
* Logistic Regression (Log. Reg.)

# Research 14

Logistic Regression (for classification)
Linear Regression (for ranking)

# Research 15

The study evaluated these machine learning algorithms:

* Bayesian Net
* Logistic Regression
* Multilayer Perceptron 
* Ruler Zero-R (or Rule ZeroR)
* J48 (a decision tree algorithm)
* Lazy IBK (k-nearest neighbors)
* Support Vector Machine (SVM)
* Neural Networks (mentioned briefly, but not extensively evaluated)
* Random Forest 
* Decision Stump

# Research 16

- Decision Tree (DT)
- Naive Bayes (NB)
- Random Forest (RF)
- Logistic Regression (LR)

# Research 17

k-Nearest Neighbors (KNN)
Decision Tree (DT)
Naive Bayes (NB)
Support Vector Machine (SVM)
Artificial Neural Network (ANN)

# Research 18

Naïve Bayes (NB), BayesNet (BN) with K2 search algorithm, Logitboost (LB), Adaboost (AB)

# Research 19

J48 (Decision Tree), K Nearest Neighbor (KNN), Logistic Regression (LR), Naive Bayes (NB)

# Research 20

* Adaptive Neuro Fuzzy Inference System (ANFIS)
* Artificial Neural Network (ANN)
* Support Vector Machine (SVM)

# Research 21

* Artificial Neural Network (ANN)
* Artificial Bee Colony (ABC) algorithm (for optimizing ANN weights)

# Research 22

Bayesian Network (BN) classifiers, including:
* Naive Bayes (NB) classifier
* Augmented Naive Bayes classifiers (various types like SAN, SAND with different augmenting operators - Tree and Forest)

# Research 23

* Random Forest (RF)
* Multilayer Perceptron (MLP)
* J48 (a decision tree algorithm)
* GFS-Adaboost-c (a hybrid algorithm)
* GFS-logitboost-c (a hybrid algorithm)

# Research 24

Artificial Neural Networks (ANN)
Naive Bayes (NB)
Voting Feature Intervals (VFI)
Ensemble of classifiers (Ens1 and Ens2)

# Research 25

Random Forest (RF)
C4.5 Decision Tree (C4.5)
Support Vector Machines (SVM)
Neural Networks (NNET) - 3-layer model
K-Nearest Neighbor (KNN)

# Research 26

OneR, RIPPER (JRip), C4.5 (J48), NBTree, Ridge Logistic Regression (RLR), Support Vector Machines (SVM), Multilayer Perceptron (MLP), Gaussian Naive Bayes (NBc), Discrete Naive Bayes (NBd), Tree-augmented Naive Bayes (TAN), Averaged One-Dependence Estimators (AODE), Hidden Naive Bayes (HNB), AdaBoost (AdaBst), Random Forest (RF), Discrete Naive Bayes (NBd2), Naive Bayes Ensemble (NBE), Superposed Naive Bayes (SNB), Tree-augmented Naive Bayes (TAN2), Naive Bayes Ensemble + TAN (NBE2), Superposed Naive Bayes + TAN (SNB2)

# Research 27

Bayesian Networks

# Research 28

Support Vector Machine (SVM)

# Research 29

Adaptive Artificial Jelly Optimization (A2JO) - for feature selection 
Long Short-Term Memory (LSTM) - for bug prediction (classification)

# Research 30

Decision Tree (DT)
Artificial Neural Network (ANN)

