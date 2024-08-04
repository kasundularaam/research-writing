# QUESTION
For each software metric used:
a. What was its individual predictive power (if reported)?
b. Was it ranked or weighted in terms of importance? If so, what was its rank or weight?

# Research 1

The paper does not report on the individual predictive power of each metric. It focuses on the overall impact of using different classes of metrics.

# Research 2

The study doesn't report on the individual predictive power of each metric.
It uses a Chi-squared (x²) based feature selection method to rank and select the most relevant metrics for each dataset.

# Research 3

The paper primarily analyzes CBO and NOC using Bayesian inference and doesn't quantify the individual predictive power or ranking of metrics.
It mentions that LOC (Lines of Code) seemed to perform well for quick fault prediction in another study.

# Research 4

  - Individual predictive power is not explicitly reported for each metric. 
  - The paper emphasizes the *unequal* importance of features, motivating the use of weighted NB.
  - Feature weighting using IG is a core part of the proposed WNB-ID method. 
  - Table 18 and Table 19 show the average feature weights calculated by IG for Java and C/C++ projects respectively.

# Research 5

   * The paper does not report individual predictive power for each metric.
   * Metrics are ranked and selected using feature selection techniques. See questions 9 and 14 for details.

# Research 6

Not applicable as traditional software metrics weren't used. The focus was on automatically learning features from ASTs using deep learning.

# Research 7

Individual metric predictive power and ranking are not explicitly provided. The paper focuses on feature selection methods for selecting relevant subsets.

# Research 8

Not individually reported in the excerpt.

# Research 9

a. Not reported.
b. Not reported.

# Research 10

The paper doesn't report the individual predictive power or ranking/weighting of each specific metric. This level of detail is often omitted in such studies.

# Research 11

a. Not reported individually.
b. No explicit ranking or weighting is provided. However, the resulting decision tree (Figure 4) indicates that RISK_LEVEL was the most important feature in this specific dataset.

# Research 12

This information is NOT provided in the paper.

# Research 13

The paper does not report individual predictive power for each metric. 

The study used the Markov Blanket feature selection method, which does not explicitly rank or weight features, but selects a subset of relevant features. The average number of selected attributes per dataset and feature group is visualized in Fig. 7.

# Research 14

Individual predictive power of most metrics is analyzed through Spearman correlation with defect counts (Table 3).
No specific ranking or weighting of metrics is applied. All metrics are used as features in the models.

# Research 15

* a. What was its individual predictive power (if reported)? Not reported.
* b. Was it ranked or weighted in terms of importance? If so, what was its rank or weight? Not reported. The paper mentions feature selection, but it doesn't provide details about the ranking or weighting of individual metrics.

# Research 16

The paper does not provide information on individual predictive power or ranking/weighting of software metrics.

# Research 17

Not explicitly analyzed in this study.

# Research 18

The paper doesn't explicitly report individual predictive power for each metric. However, it uses correlation analysis (Spearman's Rho) to analyze relationships between metrics and change proneness. It also uses Correlation-based Feature Selection (CFS) which identifies WMC, RFC, and SLOC for Rave, and RFC, LCOM, and SLOC for Math as the most important features. No explicit ranking or weighting is provided beyond this selection.

# Research 19

The paper doesn't explicitly report individual predictive power for each metric. The analysis focuses on the frequency of feature selection by MOFES, grouping metrics by categories. See Tables 11 and 12 in the paper. It infers that features in different categories might have varying performance impacts.

# Research 20

The paper doesn't provide individual predictive power or rankings for each metric. However, they analyze the importance of `ev(g)` and find it less influential than other metrics, leading to its exclusion in some experiments.

# Research 21

{'a': 'Not explicitly reported.', 'b': 'Metrics were not explicitly ranked. CFS was used for feature selection, implicitly giving higher importance to selected features.'}

# Research 22

This information (individual predictive power, ranking/weighting) is **not provided** in the excerpt.

# Research 23

a. The paper **does not report** the individual predictive power of each metric.
b. The paper **does not rank or weight** the metrics in terms of importance.

# Research 24

The study doesn't provide analysis on the individual predictive power, ranking, or weighting of specific software metrics.

# Research 25

The study doesn't focus on the individual predictive power of each metric. The emphasis is on the impact of resampling techniques on the overall model performance.

# Research 26

The paper doesn't provide individual predictive power for each metric. Ranking: Importance rankings for the top metrics are provided for RLR, SNB, and RF+PDP models for both Bugzilla and Columba datasets. (See Table 9) Additional ranking information is available for the MDP datasets in Tables 10, 11, 12, 13, 14, and 15.

# Research 27

The paper primarily focuses on ranking metrics based on their influence on defect proneness within Bayesian Networks rather than individual predictive power.
The study uses a combination of expert knowledge and Bayesian Network structure to derive importance (see Section 4.2).
General Ranking:
   - Most Effective: LOC, CBO, LOCQ, RFC, WMC 
   - Less Effective:  LCOM, LCOM3
   - Least Effective: DIT, NOC

# Research 28

* a. Individual predictive power was not explicitly quantified for each metric. However, sensitivity, specificity, precision, and completeness values are presented for each metric individually and in the combined model.
* b.  Metrics were not explicitly ranked or weighted.

# Research 29

Not reported in detail for each metric.

# Research 30

* The paper analyzes the individual predictive power through univariate logistic regression and presents R² values for each metric across different severity levels (See Tables 5, 6, 7, 8).
* While not explicitly ranked, the study identifies SLOC and CBO as the strongest predictors based on their consistently high R² values.
* The study doesn't explicitly assign weights to the metrics.

