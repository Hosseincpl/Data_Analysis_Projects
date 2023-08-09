# Predicting Life Expectancy at Birth using World Population and GDP Data
## Quera Team - group 4 - Project Final
This part aims to predict life expectancy at birth for both sexes based on World Population Prospect 2022 and world country GDP data. The dataset used in this project was extracted from the WPP2022.xlsx file and stored in a cleaned and preprocessed WPP2022.csv file using cleaning.py. The scr.ipynb file contains the regression model written in Python.
## Methodology
To select the most relevant features for the model, we performed a correlation and p-value analysis, and removed features with feature leakage. We then used both Random Forest Regressor and Linear Regression models to train the data, as well as AutoML methods. The data was evaluated using cross-validation.
## Results
|Model	Mean Absolute Error|	Mean Squared Error	|R-squared Score|
|---|---|---|
|AutoML Method|	0.0718	|0.0139	|0.9859|
|Random Forest Regressor|	0.0940	|0.0251	|0.9746|

* Cross-validation results for Random Forest Regressor with k-fold=5:

|Fold|	R-squared Score|
|---|---|
|1|	0.9745|
|2|	0.9694|
|3|	0.9710|
|4|	0.9742|
|5|	0.9633|

## Conclusion
The results of this project suggest that both population and GDP data are significant predictors of life expectancy at birth for both sexes. The model's accuracy can be improved with more data or by including additional features.
