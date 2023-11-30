import matplotlib.pyplot as plt
import numpy as np
import statsmodels.api as sm

# Given data
X1 = np.array([50, 36, 40, 45, 37, 28])
X2 = np.array([51, 46, 48, 51, 53, 46])
X3 = np.array([2.3, 2.3, 2.2, 2.2, 2.1, 1.8])
Y = np.array([48, 57, 66, 68, 59, 92])

# Scatter plots
plt.figure(figsize=(15, 5))

plt.subplot(131)
plt.scatter(X1, Y)
plt.title('Scatter Plot: X1 vs. Y')
plt.xlabel('X1')
plt.ylabel('Y')

plt.subplot(132)
plt.scatter(X2, Y)
plt.title('Scatter Plot: X2 vs. Y')
plt.xlabel('X2')
plt.ylabel('Y')

plt.subplot(133)
plt.scatter(X3, Y)
plt.title('Scatter Plot: X3 vs. Y')
plt.xlabel('X3')
plt.ylabel('Y')

plt.tight_layout()
plt.show()

# Create design matrix X
X = sm.add_constant(np.column_stack((X1, X2, X3)))

# Fit the OLS model
model = sm.OLS(Y, X).fit()

# Print coefficients
print("Coefficients:")
print(model.params)

# Confidence intervals
ci = model.conf_int(alpha=0.05)
print("\n95% Confidence Intervals:")
print(ci)

# R-squared
r_squared = model.rsquared
print(f"\nR-squared: {r_squared:.4f}")

# Residuals vs. Ŷ plots
plt.figure(figsize=(15, 5))

plt.subplot(131)
plt.scatter(model.fittedvalues, model.resid)
plt.title('Residuals vs. Ŷ')
plt.xlabel('Ŷ')
plt.ylabel('Residuals')

plt.subplot(132)
plt.scatter(X1, model.resid)
plt.title('Residuals vs. X1')
plt.xlabel('X1')
plt.ylabel('Residuals')

plt.subplot(133)
plt.scatter(X2, model.resid)
plt.title('Residuals vs. X2')
plt.xlabel('X2')
plt.ylabel('Residuals')

plt.tight_layout()
plt.show()
