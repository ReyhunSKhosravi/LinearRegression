# -*- coding: utf-8 -*-
"""LinearRegression.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1BPOETKfI8Wy7kraW7bKae6djwM-CZ2Ty
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import os

data = pd.read_csv('Admission_Predict0.6.csv')
data.head()

#Visualize data:
#Independent: CGPA
#Dependent: Chance
plt.scatter(data['CGPA'], data['Chance'])
plt.show()

#Visualize data:
#Independent: GRE_Score
#Dependent: Chance
plt.scatter(data['GRE_Score'], data['Chance'])
plt.show()

#Visualize data:
#Independent: TOEFL_Score
#Dependent: Chance
plt.scatter(data['TOEFL_Score'], data['Chance'])
plt.show()

#Visualize data:
#Independent: University_Rating
#Dependent: Chance
plt.scatter(data['University_Rating'], data['Chance'])
plt.show()

# Assuming our DataFrame is named 'data' and has columns 'CGPA' and 'chance'

# Select features and target variable
X = data['CGPA']
y = data['Chance']

# Calculate the mean of X and y
mean_X = np.mean(X)
mean_y = np.mean(y)

# Calculate the slope (beta1) and intercept (beta0)
numerator = np.sum((X - mean_X) * (y - mean_y))
denominator = np.sum((X - mean_X) ** 2)
beta1 = numerator / denominator
beta0 = mean_y - beta1 * mean_X

# Make predictions
y_pred = beta0 + beta1 * X

# Plot the regression line
plt.scatter(X, y, color='black')
plt.plot(X, y_pred, color='blue', linewidth=3)
plt.xlabel('CGPA')
plt.ylabel('Chance of Acceptance')
plt.title('Manual Linear Regression: CGPA vs. Chance')
plt.show()

# Print the coefficients
print(f'Intercept (beta0): {beta0}')
print(f'Slope (beta1): {beta1}')

# Assuming our DataFrame is named 'data' and has columns 'GRE_Score' and 'chance'

# Select features and target variable
X = data['GRE_Score']
y = data['Chance']

# Calculate the mean of X and y
mean_X = np.mean(X)
mean_y = np.mean(y)

# Calculate the slope (beta1) and intercept (beta0)
numerator = np.sum((X - mean_X) * (y - mean_y))
denominator = np.sum((X - mean_X) ** 2)
beta1 = numerator / denominator
beta0 = mean_y - beta1 * mean_X

# Make predictions
y_pred = beta0 + beta1 * X

# Plot the regression line
plt.scatter(X, y, color='black')
plt.plot(X, y_pred, color='blue', linewidth=3)
plt.xlabel('GRE_Score')
plt.ylabel('Chance of Acceptance')
plt.title('Manual Linear Regression: GRE_Score vs. Chance')
plt.show()

# Print the coefficients
print(f'Intercept (beta0): {beta0}')
print(f'Slope (beta1): {beta1}')

# Assuming our DataFrame is named 'data' and has columns 'TOEFL_Score' and 'chance'

# Select features and target variable
X = data['TOEFL_Score']
y = data['Chance']

# Calculate the mean of X and y
mean_X = np.mean(X)
mean_y = np.mean(y)

# Calculate the slope (beta1) and intercept (beta0)
numerator = np.sum((X - mean_X) * (y - mean_y))
denominator = np.sum((X - mean_X) ** 2)
beta1 = numerator / denominator
beta0 = mean_y - beta1 * mean_X

# Make predictions
y_pred = beta0 + beta1 * X

# Plot the regression line
plt.scatter(X, y, color='black')
plt.plot(X, y_pred, color='blue', linewidth=3)
plt.xlabel('TOEFL_Score')
plt.ylabel('Chance of Acceptance')
plt.title('Manual Linear Regression: TOEFL_Score vs. Chance')
plt.show()

# Print the coefficients
print(f'Intercept (beta0): {beta0}')
print(f'Slope (beta1): {beta1}')

# Assuming our DataFrame is named 'data' and has columns 'University_Rating' and 'chance'

# Select features and target variable
X = data['University_Rating']
y = data['Chance']

# Calculate the mean of X and y
mean_X = np.mean(X)
mean_y = np.mean(y)

# Calculate the slope (beta1) and intercept (beta0)
numerator = np.sum((X - mean_X) * (y - mean_y))
denominator = np.sum((X - mean_X) ** 2)
beta1 = numerator / denominator
beta0 = mean_y - beta1 * mean_X

# Make predictions
y_pred = beta0 + beta1 * X

# Plot the regression line
plt.scatter(X, y, color='black')
plt.plot(X, y_pred, color='blue', linewidth=3)
plt.xlabel('University_Rating')
plt.ylabel('Chance of Acceptance')
plt.title('Manual Linear Regression: University_Rating vs. Chance')
plt.show()

# Print the coefficients
print(f'Intercept (beta0): {beta0}')
print(f'Slope (beta1): {beta1}')

