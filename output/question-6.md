# QUESTION
What software metrics were used as features for prediction? (List all)

# Research 1

* **Source Code Metrics (CK):** The Chidamber-Kemerer metrics suite (6 metrics) plus LOC (Lines of Code). Details in Appendix A.1
* **Network Metrics (NET):** Social Network Analysis (SNA) metrics based on software dependency graphs (25 metrics). Details in Appendix A.2.
* **Process Metrics (PROC):** 11 metrics related to the development process (e.g., number of revisions, authors). Details in Appendix A.3.
* **Combinations:** The study also explored combinations of the above metric classes: CK+NET, CK+PROC, NET+PROC, CK+NET+PROC

# Research 2

Refer to Table 1 in the paper for the 10 metrics selected for KC1.
The 13 metrics used for PC4 are listed in Section 4.2 of the paper.
- Examples include:
LOC total
Halstead metrics (Error Est, Volume, Length, Difficulty)
Number of operators, operands
Cyclomatic complexity
Call pairs

# Research 3

* CBO (Coupling Between Object classes)
* WMC (Weighted Methods per Class)
* RFC (Response For a Class)
* NOC (Number Of Children)
* LCOM (Lack of Cohesion on Methods)
* DIT (Depth of Inheritance Tree)

# Research 4

  - **Java Projects (Table 5):** 
      - WMC, DIT, NOC, CBO, RFC, LCOM, CA, CE, NPM, LCOM3, LOC, DAM, MOA, MFA, CAM, IC, CBM, AMC, MAX_CC, AVG_CC, BUG. 
  - **C and C++ Projects (Table 6):** (See Table 6 for the full list of 38 features). 
       - Features used for CM1 are highlighted in bold. 

# Research 5

20 Object-Oriented metrics are used, including:
   * Weighted Methods per Class (WMC)
   * Depth of Inheritance Tree (DIT)
   * Number of Children (NOC)
   * Coupling Between Objects (CBO)
   * Response for a Class (RFC)
   * Lack of Cohesion in Methods (LCOM)
   * Afferent Coupling (Ca)
   * Efferent Coupling (Ce)
   * Number of Public Methods (NPM)
   * LCOM3
   * Lines of Code (LOC)
   * Data Access Metric (DAM)
   * Measure of Aggregation (MOA)
   * Measure of Functional Abstraction (MFA)
   * Cohesion Among Methods of Class (CAM)
   * Inheritance Coupling (IC)
   * Coupling Between Methods (CBM)
   * Average Method Complexity (AMC)
   * Maximum McCabe's Cyclomatic Complexity (Max-CC)
   * Average McCabe's Cyclomatic Complexity (Avg-CC)

# Research 6

The study did not use traditional hand-crafted software metrics. Instead, it extracted features from Abstract Syntax Trees (ASTs) of source code.

# Research 7

51 software metrics were used. Refer to Table 2 in the paper for the complete list. Examples include:
- Decision count (M_1)
- Cyclomatic complexity (M_2)
- Global data density (M_3)
- Halstead difficulty (M_4)

# Research 8

20 static code metrics were used, top 5 used in general feature subset: CE, LCOM, LOC, RFC, CBO

# Research 9

The paper doesn't provide a specific list. It mentions:
* General: size, coupling, cohesion, inheritance, and complexity metrics.
* Eclipse dataset:  pre-release defects, post-release defects, complexity metrics (aggregated at package level using average, maximum, and sum), and size of the abstract syntax tree.

# Research 10

The paper mentions these types of metrics were used:

* Chidamber and Kemerer (CK) metrics
* McCabe metrics
* HalStead metrics
* It also mentions LOC (Lines of Code) and Miscellaneous metrics for jEdit

The exact metrics within these categories aren't explicitly listed in the paper.

# Research 11

The study used a fusion of requirement metrics and code metrics. Refer to Table II in the paper for the complete list of 31 metrics. This includes:
    * Requirement metrics (e.g., ACTION, CONDITIONAL, RISK_LEVEL)
    * Code metrics (e.g., Halstead metrics, Cyclomatic Complexity, LOC_BLANK)

# Research 12

The paper states that 21 commonly used method-level metrics are used, but the specific metrics are not listed. It refers to [3] for more details.

# Research 13

The study used various static code features:

* **LOC-based metrics:** LOC_Total, LOC_Blank, LOC_Executable, LOC_Comments, LOC_Code_and_Comment, Number_of_Lines, Percent_Comments
* **McCabe complexity metrics:** Cyclomatic_Complexity, Cyclomatic_Density, Decision_Density, Design_Complexity, Design_Density, Essential_Complexity, Essential_Density, Global_Data_Complexity, Global_Data_Density, Norm_Cyclomatic_Compl, Maintenance Severity
* **Halstead metrics:** Num_Operators, Num_Operands, Num_Uniq_Operators, Num_Uniq_Operands, Length, Difficulty, Level, Volume, Programming_Effort, Programming_Time, Error_Estimate, Content
* **Miscellaneous metrics:** Branch_Count, Call_Pairs, Condition_Count, Decision_Count, Edge_Count, Node_Count, Parameter_Count, Multiple_Condition_Count, Modified_Condition_Count
* **Object-Oriented Metrics** (for Eclipse datasets): Fan out, Method lines of code, Nested block depth, Number of parameters, Cyclomatic complexity, Number of fields, Number of methods, Number of static fields, Number of static methods, Number of anonymous type declarations, Number of interfaces, Number of classes, Total lines of code

# Research 14

FOUT (Number of method calls)
MLOC (Method lines of code)
NBD (Nested block depth)
PAR (Number of parameters)
VG (McCabe cyclomatic complexity)
NOF (Number of fields)
NOM (Number of methods)
NSF (Number of static fields)
NSM (Number of static methods)
ACD (Number of anonymous type declarations)
NOI (Number of interfaces)
NOT (Number of classes)
TLOC (Total lines of code)
NOCU (Number of files/compilation units)

# Research 15

The paper doesn't explicitly list the software metrics used as features. This is another limitation. It mentions that the datasets are from the NASA Metrics Data Program (MDP), which typically include metrics like:

* McCabe's Cyclomatic Complexity
* Lines of Code
* Number of Functions/Methods
* Number of Variables
* Coupling Measures
* Cohesion Measures

# Research 16

- McCabe metrics (Cyclomatic Complexity `v(g)`, Essential Complexity `ev(g)`, Design Complexity `iv(g)`)
- Halstead metrics (number of operators and operands `N`, volume `V`, program length `L`, difficulty `D`, intelligence `I`, effort `E`, time estimator `T`, effort estimate `B`)
- Lines of Code (LOC)
- Number of comments (`Locomment`)
- Number of blank lines (`Loblank`)
- Number of code and comments (`Locodeandcomment`)
- Unique operators (`uniq_op`)
- Unique operands (`uniq_opnd`)
- Total operators (`total_op`)
- Total operands (`total_opnd`)
- Total number of branch count (`BranchCount`)

# Research 17

McCabe, Halstead, Line Count, Operator, Branch Count

# Research 18

Coupling Between Objects (CBO), Number Of Children (NOC), Response For a Class (RFC), Depth of Inheritance Tree (DIT), Lack of Cohesion Among Methods (LCOM), Weighted Methods of a class (WMC), Source Lines of Code (SLOC)

# Research 19

{'RELINK': '26 metrics based on code complexity, categorized as Complexity Metrics (CPM) and Count Metrics (CTM). See Table 3 in the paper.', 'PROMISE': '20 metrics, including object-oriented metrics (OOM) and complexity metrics (CPM). OOM is further divided into 5 metric suites (CK, HS, HD, ECK, Martin). See Table 3 in the paper.'}

# Research 20

They used McCabe metrics:

* `loc`: McCabe number of code lines
* `v(g)`: Cyclomatic complexity
* `ev(g)`: Essential complexity 
* `iv(g)`: Design complexity

# Research 21

* loc (lines of code)
* v(g) (cyclomatic complexity)
* ev(g) (essential complexity)
* iv(g) (design complexity)
* lOCode (count of statement lines)
* lOComment (count of comment lines)
* lOBlank (count of blank lines)
* lOCodeAndComment (count of code and comment lines)
* uniqOp (number of unique operators)
* uniqOpnd (number of unique operands)
* branchCount (total number of branch count)
* v (Halstead Volume)
* l (Halstead Program length)
* d (Halstead Difficulty)
* i (Halstead Intelligence)
* b (Halstead Effort estimate)

# Research 22

* Object-Oriented (OO) metrics
* Halstead metrics
* Lines of Code (LOC)
* McCabe complexity

# Research 23

* LOC-ADDED
* LOC-DELETED
* LOC-CHANGED
* MAX-LOC-ADDED
* MAX_LOC-CHANGED
* MAX_LOC-DELETED
* CODE CHURN
* MAX CODE CHURN
* AVERAGE CODE CHURN

# Research 24

The study doesn't explicitly list all the static code attributes used. It mentions using the top eleven attributes from the Promise repository based on Information Gain and prior research.

# Research 25

20 static code metrics (listed in Table 1) including WMC, DIT, NOC, etc. 
8 process metrics (listed in Table 1) including CodeChurn, LOCAdded, LOCDeleted, etc.

# Research 26

**MDP Datasets:** LOC counts (total, blank, code and comment, comments, executable), Halstead metrics (content, difficulty, effort, error est, length, level, prog_time, volume, num_operands, num_operators, num_unique_operands, num_unique_operators), McCabe metrics (cyclomatic_complexity, cyclomatic_density, design_complexity, essential_complexity), and miscellaneous metrics (branch count, call_pairs, condition count, decision_count, decision_density, design_density, edge_count, essential_density, global_data_complexity, global_data_density, maintenance_severity, modified_condition_count, multiple_condition_count, node count, normalized_cyclomatic_compl., parameter count, percent comments). (See Table 2)
**JIT Datasets:** Diffusion metrics (NS, ND, NF, and Entropy), Size metrics (LAn, LDn, and LTn), Purpose metric (FIX), History metrics (NDEV, AGE, and NUCn), and Experience metrics (EXP, REXP, and SEXP). (See Table 3)

# Research 27

LOC (Lines of Code)
CBO (Coupling Between Objects)
WMC (Weighted Methods per Class)
RFC (Response for Class)
LCOM (Lack of Cohesion of Methods)
LCOM3 (Lack of Cohesion in Methods - Henderson-Sellers definition)
DIT (Depth of Inheritance Tree)
NOC (Number of Children)
LOCQ (Lack of Coding Quality) - *Novel metric introduced in this paper*
NOD (Number of Developers) - *Extracted for a subset of datasets*

# Research 28

* Coupling Between Objects (CBO)
* Lack of Cohesion (LCOM)
* Number of Children (NOC)
* Depth of Inheritance Tree (DIT)
* Weighted Methods per Class (WMC)
* Response for a Class (RFC)
* Source Lines of Code (SLOC)

# Research 29

PROMISE: Wmc, Dit, Noc, Cbo, Rfc, Lcom, Ca, Ce, Npm, lcom3, Loc, Dam, Moa, Mfa, Cam, Ic, Cbm, Amc, Max_cc, Avg_cc  (See Table 1 for descriptions)
NASA: Line count of code, Count of blank lines, Count of code and comments, Count of comments, Line count of executable code, Number of operators, Number of operands, Number of unique operators, Number of unique operands, Halstead metrics (Length, Volume, Level, Difficulty, Content, Effort, Error Estimate, Programming_Time), Cyclomatic_Complexity, Design_Complexity, Essential_Complexity. (See Table 2)

# Research 30

* Coupling Between Objects (CBO)
* Weighted Methods per Class (WMC)
* Response for a Class (RFC)
* Source Lines of Code (SLOC)
* Lack of Cohesion (LCOM)
* Number of Children (NOC)
* Depth of Inheritance (DIT)

