# Forest fire area prediction - Group 2

Team members:

1. Gautham Pughazhendhi
2. Margot Vore
3. Anahita Einolghozati
4. Hatef Rahmani

# Introduction

In this project, we aim to predict the burned area of forest fires in the northeast region of Portugal, using some meteorological and environmental data. Forest fires are major environmental concerns with the potential of endangering humane lives (Cortez and Morais, 2007). Particularly, here in BC, millions acres of forests are burned annualy, damaging the environment and posing significant financial challenges. Fast-detection of the wildfire and predictions of the burned area are crucial elements for a successfull fire monitoring. For this purpose, one can use the information hidden in themeteorological data (such as trends and patterns for the wildfire) and develop a predictive model. 

The data set used in this projcet consists of some meteorological observations (such as temperature, wind, relative humidity etc) and several fire indexes . The data set was sourced from the UCI Machine Learnign Repository. Each row in the data set represents one obersvation for the fire monitoring, with the column `area` as our target (showing the burned area), and 12 other meaurements and indexes as features (including `month`, `day`, `RH`, `rain`, `DC`, `ISI` etc). For a detailed definition of the indexes, please refer to the following paper: 

*P. Cortez and A. Morais. A Data Mining Approach to Predict Forest Fires using Meteorological Data. In J. Neves, M. F. Santos and J. Machado Eds., New Trends in Artificial Intelligence, Proceedings of the 13th EPIA 2007 - Portuguese Conference on Artificial Intelligence*.

To answer this question and predict the output area, we build a predictive regression model. First, we split our data set into train and test splits by 20:80 ratio. Then, we conduct EDA analysis to better understand the data, detect errors or outliers or anomalous events, find the patterns within the data and see if there is class imbalance. Depending on the outcome of this analysis, we choose the several features which are most relavant and informative t predict the burned area. For column transfer, We use `StandardScaler` for numerical features and `OneHotEncoder` for categorical features. Note that there is no missing values in the data set. We explore several regression models such as SVM, k-NN etc to find the berst-performing model. We use RMSE as a score metri and perform cross-validation with 20 folds to tune the hyperparameter (note that the data set is quite small with 517 observations). 

Once we find our best model, we evaluate that on the test set and report the scores and confusion matrix. The results will be reported in a graph in the format of predicted burned area versus the real burned area, and in ideal case, all data points should collapse onto $y=x$ line. 

