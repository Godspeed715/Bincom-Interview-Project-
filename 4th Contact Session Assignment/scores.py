import pandas
import numpy

# Read data from the CSV file
data = pandas.read_csv("student_scores.csv")

# Extract the hours and rows data
X = data["Hours"].values
Y = data["Scores"].values

# Fit the model to get slope and intercept
slope, intercept = numpy.polyfit(X, Y, 1)

# Calculate predicted values
Y_pred = slope * X + intercept

# Evaluate R-squared
ss_residual = numpy.sum((Y - Y_pred) ** 2)
ss_total = numpy.sum((Y - numpy.mean(Y)) ** 2)
r_squared = 1 - (ss_residual / ss_total)

print(f"R-squared: {r_squared:.4f}")
print(f"Slope: {slope:.2f}")
print(f"Intercept: {intercept:.2f}")

# Prediction example
fake_x = 20
fake_y = slope * fake_x + intercept
print(f"The Assumed value of {fake_x} hours will give a value of score of {fake_y:.2f}")



