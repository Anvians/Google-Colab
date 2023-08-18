# -*- coding: utf-8 -*-
"""Copy of data_preprocessing_tools.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1w77vQT7fk-moejTOdL1rOL4vct4lkf8y

# Data Preprocessing Tools

## Importing the libraries
"""

import pandas as pd

"""## Importing the dataset

This code snippet is typically used in machine learning and data analysis tasks, where you're working with a dataset using the pandas library. Let's break down what each line of code is doing:

1. `x = dataset.iloc[:, :-1].values`
   - Here, `dataset` is presumably a pandas DataFrame that contains your data.
   - `iloc` is a method in pandas used for indexing by integer position. It allows you to select specific rows and columns using their numerical indices.
   - The syntax `[:, :-1]` specifies that you want to select all rows (`:` before the comma) and all columns except the last one (`:-1` after the comma). The `:-1` notation means "from the beginning up to but not including the last element".
   - `.values` is used to convert the selected portion of the DataFrame into a NumPy array. This is often done to prepare the data for further processing, such as machine learning algorithms, which often expect data in array format.
   - So, `x` will hold the feature data from your dataset, excluding the last column.

2. `y = dataset.iloc[:, -1].values`
   - Similar to the previous line, this line of code is again using the `iloc` method to select rows and columns by their integer positions.
   - `[:, -1]` selects all rows (`:` before the comma) but only the last column (`-1` after the comma), which is typically assumed to be the target or label column in machine learning tasks.
   - `.values` is used to convert this selected column into a NumPy array.
   - `y` will hold the target or label data from your dataset.

In summary, this code is splitting a given dataset into feature data (`x`) and target/label data (`y`) using pandas and preparing them as NumPy arrays for further processing, often in the context of machine learning or data analysis tasks.
"""

dataset =pd.read_csv('Data.csv')
x = dataset.iloc[: , :-1].values
y = dataset.iloc[:, -1].values
z = dataset.iloc[:,1:3]

print(x)

print(z)

print(z)

"""## Taking care of missing data

Dealing with missing data is an important step in data preprocessing before performing analysis or training machine learning models. In pandas, you can handle missing data using various techniques. Here's an overview of some common methods:

1. **Dropping Missing Values:**
   You can drop rows or columns containing missing values using the `dropna()` method. For example, to remove rows with missing values:
   
   ```python
   dataset.dropna(axis=0, inplace=True)  # Drop rows with missing values
   ```

2. **Imputation:**
   Imputation involves replacing missing values with estimated or calculated values. You can use the `fillna()` method to fill missing values using various strategies such as mean, median, mode, or custom values. For example, to fill missing values in a DataFrame with the mean of each column:
   
   ```python
   dataset.fillna(dataset.mean(), inplace=True)
   ```

3. **Forward or Backward Fill:**
   You can use the `ffill()` (forward fill) or `bfill()` (backward fill) methods to fill missing values with the preceding or following values in the same column, respectively.
   
   ```python
   dataset.ffill(inplace=True)  # Forward fill missing values
   ```

4. **Interpolation:**
   Pandas provides interpolation methods like `linear`, `quadratic`, and more, which can be used to estimate missing values based on neighboring data points.
   
   ```python
   dataset.interpolate(method='linear', inplace=True)
   ```

5. **Indicator Variables:**
   You can create indicator variables to track the presence of missing values. This can be useful in some scenarios to indicate whether a value was originally missing.
   
   ```python
   dataset['column_name_missing'] = dataset['column_name'].isnull()
   ```

Remember that the choice of method depends on your dataset, the nature of the missing data, and the goals of your analysis or modeling. It's essential to carefully consider which approach is most suitable for your specific case.

Also, keep in mind that preprocessing steps like handling missing data should be performed on both the feature data (`x`) and target/label data (`y`) if necessary. Always validate the impact of your chosen method on the quality and integrity of your data before proceeding with analysis or modeling.
"""

from sklearn.impute import SimpleImputer
import numpy as np

imputer = SimpleImputer(missing_values = np.nan , strategy = 'median')
imputer.fit(x[:, 1:3])
x[:,1:3] = imputer.transform(x[:, 1:3])

print(x)

print(x)

"""## Encoding categorical data"""



"""### Encoding the Independent Variable

### Encoding the Dependent Variable

## Splitting the dataset into the Training set and Test set

## Feature Scaling
"""