# QUESTION
Was feature selection performed? If so, what method was used?

# Research 1

Yes, attribute selection was performed, but the exact method is not specified.

# Research 2

Yes, a Chi-squared (x²) based filter approach was used.

# Research 3

No formal feature selection method is described.

# Research 4

   - Feature selection is not the primary focus of this study.
   - The paper focuses on feature *weighting* using IG within WNB-ID.

# Research 5

Ten different feature selection techniques are used:
    * **Feature Ranking:**
        * Chi Squared test
        * Gain Ratio Feature Evaluation
        * Information Gain Feature Evaluation
        * OneR Feature Evaluation
        * Logistic Regression Analysis
        * Principal Component Analysis (PCA)
    * **Feature Subset Selection:**
        * Correlation Based Feature Selection (CFS)
        * Classifier Subset Evaluation
        * Filtered Subset Evaluation
        * Rough Set Analysis (RSA)

# Research 6

Performed implicitly by selecting 29 specific AST node types based on prior research and practical considerations.

# Research 7

Yes, feature selection methods evaluated include:
- Pearson's correlation
- Fisher's criterion
- Greedy Forward Selection (GFS) - performed best

# Research 8

Yes, a general feature subset was created using the top 5 most occurring software metrics.

# Research 9

No specific feature selection method is mentioned in this study.

# Research 10

Yes, two feature selection methods were used with different search strategies:

* **Correlation-based Feature Subset Selection (CFS)** with **GreedyStepwise** search
* **Principal Component Analysis (PCA)** with **Ranker** search method

# Research 11

No explicit feature selection method is described. The decision tree algorithm itself inherently performs feature selection by choosing the most discriminative features at each node.

# Research 12

No, feature selection is not mentioned in the paper.

# Research 13

Yes, the Markov Blanket feature selection method was used with two significance levels:

* MB.05 (5% significance level)
* MB.15 (15% significance level)

# Research 14

No

# Research 15

Yes, feature selection was performed. However, the paper doesn't specify the exact feature selection method used.  Common methods include filter methods (e.g., correlation-based), wrapper methods (e.g., recursive feature elimination), and embedded methods (e.g., LASSO regularization).

# Research 16

No specific feature selection method is mentioned in the paper.

# Research 17

While mentioned as important, the specific method used wasn't explicitly stated. It seems likely that feature selection was implicitly done through the use of established software metrics like McCabe and Halstead.

# Research 18

Yes, Correlation-based Feature Selection (CFS) was used.

# Research 19

MOFES (Multi-Objective FEature Selection): The paper's novel approach, which treats feature selection as a multi-objective optimization problem. It uses Pareto based multi-objective optimization algorithms (PMAs), specifically NSGA-II, based on their analysis in RQ1. The paper compares MOFES with 22 state-of-the-art filter and wrapper based feature selection methods.

# Research 20

Yes, feature selection was performed based on an analysis of the influence of the `ev(g)` metric on fault prediction.  They removed `ev(g)` in later experiments as it seemed less influential.

# Research 21

Yes, Correlation-based Feature Selection (CFS) was used.

# Research 22

The paper mentions feature selection as a point of consideration for the experiments but **doesn't specify** which method would be used.

# Research 23

No explicit feature selection method is mentioned. However, the hybrid algorithms (GFS-Adaboost-c and GFS-logitboost-c) inherently incorporate feature selection as part of their optimization process.

# Research 24

Yes, Information Gain was used to select the top eleven most relevant attributes.

# Research 25

The paper doesn't mention any specific feature selection techniques.

# Research 26

No dedicated feature selection method is described. Implicit Selection: Discretization based on AIC or BIC allowed for concurrent calculation of independent variable importance, which could be used for variable selection.

# Research 27

Yes, two methods were used for comparison:
   - CFS (Correlation-based Feature Selection)
   - ReliefF (Relief Feature Selection)

# Research 28

No formal feature selection method was applied. All seven metrics were used in the models.

# Research 29

Yes, using the A²JO algorithm.

# Research 30

Forward stepwise selection was used for logistic regression. All features selected in univariate analysis were included for the backward elimination method in ANN.

