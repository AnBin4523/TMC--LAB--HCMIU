import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score
import statsmodels.api as sm

# Given data
X = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9])
y = np.array([1, 1.5, 2, 3, 4, 5, 8, 10, 13])

# Reshape X for sklearn
X_reshaped = X.reshape(-1, 1)

# (a) Least-squares regression for a straight line
model = LinearRegression()
model.fit(X_reshaped, y)

# Slope and intercept
slope = model.coef_[0]
intercept = model.intercept_

# Predicted values
y_pred = model.predict(X_reshaped)

# Standard error of the estimate (Sy/x)
syx = np.sqrt(mean_squared_error(y, y_pred))

# Coefficient of determination (R-square)
r_square = r2_score(y, y_pred)

# Correlation coefficient
correlation_coefficient = np.corrcoef(X, y)[0, 1]

# Plotting
plt.scatter(X, y, label='Data')
plt.plot(X, y_pred, color='red', label=f'Regression Line (y = {slope:.2f}x + {intercept:.2f})')
plt.title('Least-Squares Regression: Straight Line')
plt.xlabel('X')
plt.ylabel('y')
plt.legend()
plt.show()

# (b) Polynomial regression for a parabola
poly_degree = 2
X_poly = np.column_stack([X**i for i in range(poly_degree + 1)])

# Add a constant term to the design matrix
X_poly = sm.add_constant(X_poly)

model_poly = sm.OLS(y, X_poly).fit()

# Predicted values
y_pred_poly = model_poly.predict(X_poly)

# Plotting
plt.scatter(X, y, label='Data')
plt.plot(X, y_pred_poly, color='green', label=f'Polynomial Regression (Degree {poly_degree})')
plt.title('Polynomial Regression: Parabola')
plt.xlabel('X')
plt.ylabel('y')
plt.legend()
plt.show()

# (c) Compare with statsmodels OLS
X_statsmodels = sm.add_constant(X)  
model_ols = sm.OLS(y, X_statsmodels).fit()

# Print results
print(f"(a) Results for Straight Line:")
print(f"    Slope: {slope}")
print(f"    Intercept: {intercept}")
print(f"    Standard Error of the Estimate (Sy/x): {syx}")
print(f"    Coefficient of Determination (R-square): {r_square}")
print(f"    Correlation Coefficient: {correlation_coefficient}")
print(f"(b) Results for Polynomial Regression:")
print(f"    Coefficients: {model_poly.params}")
print(f"    Intercept: {model_poly.params[0]}")
print(f"(c) Results from statsmodels OLS:")
print(model_ols.summary())