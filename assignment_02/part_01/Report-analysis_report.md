
# JADBio Description of Performed Analysis



## Setup
JADBio version <b>1.4.118</b> ran on dataset <b>Obesity_among_children_and_adolescents_aged_2_19_years__by_selected_characteristics__United_States</b>
with
<b>633</b> samples
and <b>14</b> features to create a predictive model for outcome named <b>STUB_LABEL_NUM</b>.
The outcome was continuous leading to a <b>regression</b> modeling.

The preferences of the analysis were set to <b>true</b> for feature selection and <b>false</b> for full feature models tried.<br>
The <b>R2</b> metric was used to optimize for the best model.<br>
The maximum number of features to select was set to <b>25</b>. <br>
The effort to spend on tuning the algorithms were set to <b>Quick</b>.<br>
The number of CPU cores to use for the analysis was set to <b>6</b>.<br>
The execution time was <b>00:00:05</b>.<br>


## Configuration Space
JADBio’s AI decide to try the following algorithms and tuning hyper-parameter values:


Algorithm Type | Algorithm | Hyper-parameter | Set of Values
--- | --- | --- | ---
Preprocessing |Mean Imputation | |
&nbsp; |Mode Imputation | |
&nbsp; |Constant Removal | |
&nbsp; |Variable Normalization | |
Feature Selection |Test-Budgeted Statistically Equivalent Signature (SES) |maxK | 2.0
&nbsp; |&nbsp; |alpha | 0.05
&nbsp; |LASSO |penalty | 1.0
Modeling |Regression Decision Tree with Mean Squared Error splitting criterion |alpha | 0.05
&nbsp; |&nbsp; |minLeafSize | 5
&nbsp; |Ridge Linear Regression |lambda | 1.0
&nbsp; |Regression Random Forest with Mean Squared Error splitting criterion |nTrees | 100
&nbsp; |&nbsp; |minLeafSize | 5.0
<br><br>


Leading to <b>7</b> combinations and corresponding configurations (machine learning pipelines) to try.
For the full configurations tested see the Appendix.
<br><br>


## Configuration Estimation Protocol
JADBio’s AI system decided to estimate the out-of-sample performance of the models produced by each configuration
  using <b>Incomplete 10-fold CV with dropping.</b>
Overall, 36 models were set out to train.

Eventually, 36 had their estimation protocol completed.


# JADBio Results Summary

## Overview

A result summary is presented for analysis optimized for Aggressive Feature Selection.
The model is produced by applying the algorithms in sequence (configuration) on the training data:

Preprocessing | Feature Selection | Predictive algorithm
--- | --- | ---
Mean Imputation, Mode Imputation, Constant Removal, Standardization | Test-Budgeted Statistically Equivalent Signature (SES) algorithm with hyper-parameters: maxK = 2, alpha = 0.05 and budget = 3 * nvars | Regression Decision Tree with Mean Squared Error splitting criterion and hyper-parameters: minimum leaf size = 5, and pruning parameter alpha = 0.05

<br>



The R-squared is shown in the figure below:
<br>


   <br><br>
   
Metric | Mean estimate | CI
--- | --- | ---
  R-squared | 0.997 | [0.996, 0.998]
 Mean Absolute Error | 0.062 | [0.056, 0.068]
 Mean Squared Error | 0.005 | [0.004, 0.006]
 Relative Absolute Error | 0.064 | [0.053, 0.077]
 Relative Squared Error | 0.003 | [0.002, 0.005]
 Correlation Coefficient | 0.998 | [0.998, 0.999]
 Mean Squared Logarithmic Error | 0.000 | [0.000, 0.000]

   <br><br>







## Feature Selection


There were <b>2</b> features selected
out of the <b>14</b> available.


The selected features consist of the following subset called a signature.
<b>There were multiple signatures identified.</b>
The first signature identified by the system is the set:
<b>STUB_NAME, SE</b> in order of importance.
The following features cannot be substituted with others and still obtain
an equal predictive performance: <b>STUB_NAME, SE</b>.

Alternatively, in the following table, the features that could substitute for some selected feature are listed and still
  obtain a statistically indistinguishable predictive performance:<br><br>
  
Feature | Could be substituted with
--- | ---
 STUB_NAME | STUB_NAME_NUM,STUB_LABEL 
SE |  


<br>
The performance achieved by adding each feature in sequence to the model relative to the performance of the final model with all selected features is shown below.
The features are added in order of importance:
<br>



<br><br>
Some features may not seem to add predictive performance to the model; however, the feature selection algorithms include
them as an effort to make the final model more robust to noise.
The performances achieved by a model that contains all features except one, relative to the performance achieved when the feature is removed is shown below:
<br>



<br><br>
For some features there is no noticeable drop in performance when they are removed because they carry predictive information that is shared by other
features selected.
<br><br>





## Appendix
<br><br>


Configuration | Preprocessing | Name | Hyperparams | Name | Hyperparams | Performance (unadjusted) | Time (miliseconds) | Dropped
--- |--- |--- |--- |--- |--- |--- |--- |--- |
1 | Mean Imputation, Mode Imputation, Constant Removal, Standardization | Test-Budgeted Statistically Equivalent Signature (SES) | maxK = 2, alpha = 0.05, budget = 3 * nvars | Regression Decision Tree with Mean Squared Error splitting criterion | minimum leaf size = 5, alpha = 0.05 | 0.996971321222108 | 00:00:00.027 | false
2 | Mean Imputation, Mode Imputation, Constant Removal, Standardization | LASSO | penalty = 1.0 | Ridge Linear Regression | lambda = 1.0 | 0.9963280881576398 | 00:00:00.310 | false
3 | Mean Imputation, Mode Imputation, Constant Removal, Standardization | LASSO | penalty = 1.0 | Regression Random Forest with Mean Squared Error splitting criterion | ntrees = 100, minimum leaf size = 5 | 0.9970040268789256 | 00:00:00.323 | false
4 | IdentityFactory | FullSelector | - | Trivial model | - | 1.132164191119725e-16 | 00:00:00.000 | false
5 | Mean Imputation, Mode Imputation, Constant Removal, Standardization | LASSO | penalty = 1.0 | Regression Random Forest with Mean Squared Error splitting criterion | ntrees = 100, minimum leaf size = 5 | 0.9970040268789256 | 00:00:00.322 | false
6 | Mean Imputation, Mode Imputation, Constant Removal, Standardization | LASSO | penalty = 1.0 | Regression Decision Tree with Mean Squared Error splitting criterion | minimum leaf size = 5, alpha = 0.05 | 0.9970459783721677 | 00:00:00.312 | false
7 | Mean Imputation, Mode Imputation, Constant Removal, Standardization | LASSO | penalty = 1.0 | Regression Random Forest with Mean Squared Error splitting criterion | ntrees = 100, minimum leaf size = 5 | 0.9970040268789256 | 00:00:00.322 | false

