# Problem: https://www.hackerrank.com/challenges/battery/problem
# Score: 10
# By @Rsc2414

import pandas as pd
from sklearn.linear_model import LinearRegression

# Read the input time charged
time_charged = float(input())

# Load the training data from the file
data = pd.read_csv('trainingdata.txt', names=['charged', 'lasted'])

# Use only data points where battery lasted less than 8 hours (as per problem note)
filtered_data = data[data['lasted'] < 8]

# Prepare the training input (X) and output (y)
X = filtered_data['charged'].values.reshape(-1, 1)
y = filtered_data['lasted'].values.reshape(-1, 1)

# Create and train the linear regression model
model = LinearRegression()
model.fit(X, y)

# Predict battery life for the given charging time
predicted = model.predict([[time_charged]])

# Print the predicted time, but cap it at 8 hours
print(min(predicted[0][0], 8))
