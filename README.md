# Forest fire area prediction - Group 2

Team members:

1. Gautham Pughazhendhi
2. Margot Vore
3. Anahita Einolghozati
4. Hatef Rahmani

# Introduction

In this project, we aim to predict the burned area of forest fires in the northeast region of Portugal, using some meteorological and environmental data. Forest fires are major environmental concerns with the potential of endangering humane lives (Cortez and Morais, 2007). Particularly, here in BC, millions acres of forests are burned annualy, damaging the environment and posing significant financial challenges. Fast-detection of the wildfire and predictions of the burned area are crucial elements for a successfull fire monitoring. For this purpose, one can use the information hidden in themeteorological data (such as trends and patterns for the wildfire) and develop a predictive model. 

The data set used in this projcet consists of some meteorological observations (such as temperature, wind, relative humidity etc) and several fire indexes . The data set was sourced from the UCI Machine Learnign Repository and the details of the data set can be found `here`??. Each row in the data set represents one obersvation for the fire monitoring, with the column `area` as our target (showing the burned area), and 12 other meaurements and indexes as features (including `month`, `day`, `RH`, `rain`, `DC`, `ISI` etc). For a detailed definition of the indexes, please refer to the following paper: 

*P. Cortez and A. Morais. A Data Mining Approach to Predict Forest Fires using Meteorological Data. In J. Neves, M. F. Santos and J. Machado Eds., New Trends in Artificial Intelligence, Proceedings of the 13th EPIA 2007 - Portuguese Conference on Artificial Intelligence*.

To answer this question and predict the output area, we build a predictive regression model. First, we split our data set into train and test splits by 20:80 ratio. Then, we conduct some EDA analysis to better understand the data, detect errors or outliers or anomalous events, find the patterns within the data and see if there is class imbalance. Depending on the outcome of this analysis, we choose the several features which are most relavant and informative t predict the burned area. For column transfer, We use `StandardScaler` for numerical features and `OneHotEncoder` for categorical features and there is no missing values in the data set. 

