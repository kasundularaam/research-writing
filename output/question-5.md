# QUESTION
For each machine learning technique used:
a. What was the overall prediction accuracy?
b. What was the precision?
c. What was the recall?
d. What was the F1-score?
e. What was the AUC-ROC value (if reported)?

# Research 1

The paper does *not* report individual accuracy, precision, recall, F1, or AUC for each combination of learner and imbalanced method. It focuses on the *relative difference* in performance between using an imbalanced learning technique vs. not using one.

# Research 2

The paper focuses on comparing techniques rather than reporting individual precision, recall, and F1-score. The table below summarizes accuracy and AUC-ROC.

| Technique            | KC1 Total Accuracy (%) | KC1 AUC-ROC | PC4 Total Accuracy (%) | PC4 AUC-ROC |
|---------------------|-----------------------|-------------|-----------------------|-------------|
| LogR                | 79.45                 | 0.7913      | 88.86                 | 0.8812      |
| KNN                 | 55.93                 | 0.5525      | 84.65                 | 0.8429      |
| C4.5                | 79.87                 | 0.7914      | 86.39                 | 0.8598      |
| SVM                 | 79.24                 | 0.7889      | 88.15                 | 0.8785      |
| LSSVM               | 80.20                 | 0.7976      | 88.66                 | 0.8823      |
| AW-LSSVM            | 80.68                 | 0.8011      | 89.11                 | 0.8885      |
| LSSVM (Voting)      | 78.56                 | 0.7803      | 88.35                 | 0.8813      |
| LSSVM (TA)          | 80.85                 | 0.8025      | 90.09                 | 0.8989      |
| LSSVM (EP)          | 81.25                 | 0.8107      | 90.21                 | 0.8991      |
| AW-LSSVM (Voting)     | 79.19                 | 0.7882      | 88.61                 | 0.8819      |
| AW-LSSVM (TA)         | 81.32                 | 0.8116      | 90.35                 | 0.8994      |
| AW-LSSVM (EP)         | **83.86**                | **0.8328**     | **91.34**                | **0.9101**     |

# Research 3

The paper does not provide accuracy, precision, recall, F1-score, or AUC-ROC values for either technique. It focuses on visualizing the posterior distributions of CBO and NOC to show their potential as predictors.

# Research 4

 - The paper primarily focuses on F-measure as the key performance metric. 
   - Precision and Recall are also reported.
   - AUC-ROC is not mentioned in the excerpt.

# Research 5

   * **Accuracy and F-Measure:** Values for each dataset, feature selection method, and kernel function are reported in Table 9a-c.
   * **Precision, Recall, AUC-ROC:** These values are not explicitly reported in the paper.

# Research 6

Improved CNN: Outperformed traditional baselines and was comparable to DBN and Li's CNN on SPSC dataset. Achieved best average performance on PSC dataset across all metrics.
DBN, Li's CNN: Comparable performance to the proposed CNN model, outperforming traditional methods.
Traditional models (DT, LR, NB, RF, NET):  Outperformed by deep learning models on average, with RF being the closest competitor in MCC.
RANDOM, FIX:  Performed poorly, indicating the effectiveness of other models.

# Research 7

The paper primarily focuses on AUC-ROC and G-Mean due to imbalanced datasets. Individual precision, recall, and F1-score are not reported. Refer to Table 3, Table 5, and Table 6 in the paper for specific AUC and G-Mean values.

# Research 8

See table in response.

# Research 9

a. Not explicitly reported.
b. Not reported.
c. Not reported.
d. Not reported.
e. SVM:
  * Class level metrics: 0.798
  * Package level metrics: 0.721
  Bagged SVM:
  * Class level metrics: 0.832
  * Package level metrics: 0.78

# Research 10

This information is best extracted directly from Table 2 in the paper, as the values vary across datasets and with/without feature selection. Here's a general summary:

* **Random Forest** generally had the highest accuracy, F1-score, and AUC-ROC values across most datasets and feature selection scenarios.
* **ANN** often performed well, sometimes second to Random Forest.
* **SVM** had highly variable performance, struggling particularly when dimensionality reduction was applied.
* **Naïve Bayes** consistently had the lowest accuracy.
* The paper doesn't explicitly list AUC-ROC for all individual classifier/dataset combinations.

# Research 11

a. Not explicitly stated.
b. 100% for both classes (faulty and non-faulty).
c. 100% for both classes (faulty and non-faulty). 
d. Not explicitly calculated, but it would be 1.0 given the precision and recall values.
e. Not explicitly calculated, but implied to be 1.0 based on the ROC curve reaching the top-left corner (0,1).

# Research 12

This information is NOT directly provided for all the methods. The paper focuses on comparing:

* **PD (Probability of Detection):** This is equivalent to Recall.
* **PF (Probability of False):** Related to Specificity, not Precision.
* **F-measure:** This combines Precision and Recall.
* **MCC (Matthews Correlation Coefficient):** A balanced measure. 
* **AUC (Area Under the ROC Curve):** Used for stability analysis.

The exact values for Precision and Recall (except PD) are not provided. You can find the reported results in Tables 3, 4, 7, and in Appendix A.

# Research 13

The paper does not report overall accuracy, precision, recall, or F1-score.

AUC-ROC values are reported in Table 6 for each dataset and classifier.

# Research 14

Logistic Regression:
Accuracy: Ranges from 0.682 to 0.789 for files, 0.612 to 0.757 for packages.
Precision: Ranges from 0.578 to 0.687 for files, 0.641 to 0.785 for packages.
Recall: Ranges from 0.185 to 0.379 for files, 0.617 to 0.789 for packages.
F1-score: Not reported.
AUC-ROC: Not reported.
Linear Regression:
Accuracy: Not applicable (regression task).
Precision: Not applicable (regression task).
Recall: Not applicable (regression task).
F1-score: Not applicable (regression task).
AUC-ROC: Not applicable (regression task).
Spearman Correlation: Ranges from 0.331 to 0.640 for files, 0.368 to 0.901 for packages.

# Research 15

The paper mainly focuses on comparing accuracy with and without feature selection.  It does not provide detailed results like precision, recall, F1-score, or AUC-ROC for each individual classifier. This is a limitation of the paper.

* a. What was the overall prediction accuracy?
    * Accuracies vary significantly between datasets and with/without feature selection. See Tables 4 and 5 in the paper for the specific accuracy values.  
    * Logistic Regression generally performed well, achieving over 90% accuracy on most datasets with feature selection.
* b. What was the precision? Not reported.
* c. What was the recall? Not reported.
* d. What was the F1-score? Not reported.
* e. What was the AUC-ROC value (if reported)? Not reported.

# Research 16

|| Dataset | Technique | Accuracy | Precision | Recall | F1-score | AUC-ROC |
|---|---|---|---|---|---|---|
| JM1   | DT        | 0.99      | 0.99      | 1.00   | 0.99     | 0.973    |
|       | NB        | 0.80      | 0.81      | 0.97   | 0.89     | 0.523    | 
|       | RF        | 0.99      | 0.99      | 1.00   | 0.99     | 0.975    |
|       | LR        | 0.81      | 0.82      | 0.99   | 0.89     | 0.528    |
| PC1   | DT        | 0.99      | 0.99      | 1.00   | 1.00     | 0.961    |
|       | NB        | 0.91      | 0.94      | 0.96   | 0.95     | 0.541    |
|       | RF        | 0.99      | 0.99      | 1.00   | 1.00     | 0.961    |
|       | LR        | 0.93      | 0.94      | 0.99   | 0.96     | 0.578    |
| KC1   | DT        | 0.99      | 0.99      | 1.00   | 0.99     | 0.964    |
|       | NB        | 0.85      | 0.88      | 0.96   | 0.92     | 0.609    |
|       | RF        | 0.99      | 0.99      | 1.00   | 0.99     | 0.967    |
|       | LR        | 0.85      | 0.87      | 0.96   | 0.92     | 0.596    |
| KC2   | DT        | 0.98      | 0.98      | 1.00   | 0.99     | 0.963    |
|       | NB        | 0.83      | 0.83      | 0.98   | 0.90     | 0.603    |
|       | RF        | 0.98      | 0.98      | 1.00   | 0.99     | 0.963    |
|       | LR        | 0.84      | 0.86      | 0.96   | 0.91     | 0.680    |

# Research 17

Accuracy, Precision, Recall, F1-score, AUC-ROC (not explicitly reported)

# Research 18

NB: g-mean (Rave) 0.55, Accuracy (Rave) 0.59, g-mean (Math) 0.55, Accuracy (Math) 0.65, BN: g-mean (Rave) 0.58, Accuracy (Rave) 0.60, g-mean (Math) 0.58, Accuracy (Math) 0.67, LB: g-mean (Rave) 0.57, Accuracy (Rave) 0.60, g-mean (Math) 0.56, Accuracy (Math) 0.65, AB: g-mean (Rave) 0.57, Accuracy (Rave) 0.60, g-mean (Math) 0.57, Accuracy (Math) 0.66

# Research 19

AUC-ROC, F1 score, Precision, Recall (not used)

# Research 20

Unfortunately, the paper focuses primarily on AUC-ROC and doesn't explicitly report accuracy, precision, recall, or F1-score.

# Research 21

{'a': '68.4%', 'b': 'Not directly reported. Can be calculated from the confusion matrix using Precision = TP / (TP + FP).', 'c': '78.6%', 'd': 'Not directly reported.', 'e': '0.79'}

# Research 22

This information is **not provided** in the excerpt. The paper outlines the experimental design but doesn't include specific results like accuracy, precision, recall, F1-score, or AUC-ROC values.

# Research 23

This information can be found in Tables 3 and 5. Unfortunately, the paper doesn't provide accuracy or F1-score, and AUC-ROC isn't mentioned.

| Technique | Dataset | Precision (P) | Recall (R) |
|---|---|---|---||
| Random Forest (RF) | v4-v5 | 0.616 | 0.618 |
|  | v2-v5 | 0.820 | 0.836 |
| Multilayer Perceptron (MLP) | v4-v5 | 0.413 | 0.624 | 
|  | v2-v5 | 0.616 | 0.618 |
| J48 | v4-v5 | 0.524 | 0.624 |
|  | v2-v5 | 0.822 | 0.840 |
| GFS-Adaboost-c (GFS-AB-c) | v4-v5 | 0.646 | 0.963 |
|  | v2-v5 | 0.815 | 0.992 |
| GFS-logitboost-c (GFS-LB-c) | v4-v5 | 0.646 | 0.963 |
|  | v2-v5 | 0.822 | 0.992 |

# Research 24

The study primarily focuses on comparing ensembles (Ens1, Ens2) with a benchmark study (Menzies et al. 2007a) and doesn't provide separate results (precision, recall, F1, AUC-ROC) for individual ANN, NB, and VFI on all datasets.

# Research 25

This paper focuses on comparing performance when applying sampling methods, not individual performance. They did not report specific values for accuracy, precision, recall, F1-score for each technique individually. However, they use these metrics comparatively.

# Research 26

The paper primarily focuses on AUC-ROC values for evaluating accuracy. See Table 6 for the AUC-ROC values of all tested techniques. Precision, Recall, and F1-score are not reported.

# Research 27

a. Overall Accuracy: Not explicitly reported.
b. Precision: Not explicitly reported.
c. Recall: Not explicitly reported.
d. F1-score: Not explicitly reported.
e. AUC-ROC: Reported for each dataset (see Table 3 in the paper):
   - Ant: 0.820
   - Tomcat: 0.766
   - Poi: 0.845
   - Jedit: 0.658
   - Velocity: 0.678
   - Synapse: 0.660
   - Lucene: 0.633
   - Xalan: 0.624
   - Ivy: 0.846

# Research 28

Note: Multiple models were trained for different fault severity levels.
    * **HSF (High Severity Fault) Model:**
       * a. Accuracy: Not explicitly reported, derived as 70.09% ((86+16)/(102+48))
       * b. Precision: 70.34% 
       * c. Recall (Sensitivity): 69.56% 
       * d. F1-score: Not reported
       * e. AUC-ROC: 0.728
    * **MSF (Medium Severity Fault) Model:**
       * a. Accuracy: Not explicitly reported, derived as 83.37% ((77+47)/(87+58))
       * b. Precision: 82.75% 
       * c. Recall (Sensitivity): 81.03% 
       * d. F1-score: Not reported
       * e. AUC-ROC: 0.88
    * **LSF (Low Severity Fault) Model:**
       * a. Accuracy: Not explicitly reported, derived as 76.06% ((82+29)/(106+39))
       * b. Precision: 77.08% 
       * c. Recall (Sensitivity): 74.35% 
       * d. F1-score: Not reported
       * e. AUC-ROC: 0.84 
    * **USF (Ungraded Severity Fault) Model:**
       * a. Accuracy: Not explicitly reported, derived as 78.62% ((70+45)/(86+59))
       * b. Precision: 78.62%
       * c. Recall (Sensitivity): 76.27% 
       * d. F1-score: Not reported
       * e. AUC-ROC: 0.89

# Research 29

Accuracy:
PROMISE: Varies by project, highest is 93.41% (Prop 4)
NASA: Varies by project, highest is 92.8% (PC1)
Precision: Not reported individually for each project
Recall: Not reported individually for each project
F1-score:
PROMISE: Varies by project, highest is 0.883 (Prop 4)
NASA: Varies by project, highest is 0.962 (PC1)
AUC-ROC: Not reported

# Research 30

  | Metric | Model | Severity | Sensitivity | Specificity | Precision | Completeness | AUC-ROC |
  |---|---|---|---|---|---|---|---||
  | **DT** | Model I | High | 69.50 | 90.00 | 84.68 | 70.80 | 0.766 |
  | **DT** | Model II | Medium | 89.70 | 71.30 | 78.64 | 97.50 | 0.888 |
  | **DT** | Model III | Low | 90.30 | 81.10 | 83.40 | 94.30 | 0.875 |
  | **DT** | Model IV | Ungraded | 91.50 | 87.20 | 88.90 | 94.00 | 0.835 |
  | **ANN** | Model I | High | 73.90 | 71.31 | 71.70 | 87.50 | 0.722 |
  | **ANN** | Model II | Medium | 74.10 | 74.00 | 73.79 | 85.07 | 0.809 |
  | **ANN** | Model III | Low | 71.70 | 72.64 | 72.41 | 79.31 | 0.765 |
  | **ANN** | Model IV | Ungraded | 72.80 | 79.06 | 76.55 | 88.16 | 0.809 |

  **Note:** The F1-score is not explicitly reported in the paper.

