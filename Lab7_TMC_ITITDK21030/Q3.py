import numpy as np
import statsmodels.api as sm
from scipy.stats import t

# Given data
X1 = np.array([0, 0, 1, 2, 0, 1, 2, 2, 1])
X2 = np.array([0, 2, 2, 4, 4, 6, 6, 2, 1])
Y = np.array([14, 21, 11, 12, 23, 23, 14, 6, 11])

# Create design matrix X with a constant term
X = sm.add_constant(np.column_stack((X1, X2)))

# Fit the OLS model
model = sm.OLS(Y, X).fit()

# Print coefficients
print("(a) Coefficients:")
print(model.params)

# Print standard error of the estimate (Sy/x)
syx = np.sqrt(model.mse_resid)
print(f"(a) Standard Error of the Estimate (Sy/x): {syx:.4f}")

# Confidence Intervals
alpha = 0.05  # 95% confidence interval
t_critical = t.ppf(1 - alpha/2, model.df_resid)

# Confidence Interval for Intercept (beta_0)
ci_intercept = model.conf_int(alpha=alpha)[0]
print(f"(a) 95% Confidence Interval for Intercept (beta_0): {ci_intercept[0]:.4f} - {ci_intercept[1]:.4f}")

# Confidence Interval for Coefficient of X1 (beta_1)
ci_x1 = model.conf_int(alpha=alpha)[1]
print(f"(a) 95% Confidence Interval for Coefficient of X1 (beta_1): {ci_x1[0]:.4f} - {ci_x1[1]:.4f}")

# Confidence Interval for Coefficient of X2 (beta_2)
ci_x2 = model.conf_int(alpha=alpha)[2]
print(f"(a) 95% Confidence Interval for Coefficient of X2 (beta_2): {ci_x2[0]:.4f} - {ci_x2[1]:.4f}")

# Print R-squared
print(f"(a) Coefficient of Determination (R-squared): {model.rsquared:.4f}")

# Print Correlation Coefficient
correlation_coefficient = np.corrcoef(Y, model.fittedvalues)[0, 1]
print(f"(a) Correlation Coefficient: {correlation_coefficient:.4f}")
print(" ")

# Polynomial regression for a parabola (degree 2)
poly_degree = 2
X_poly = np.column_stack([X1, X2, X1**2, X2**2, X1*X2])

# Fit the OLS model for polynomial regression
model_poly = sm.OLS(Y, sm.add_constant(X_poly)).fit()

# Print coefficients for polynomial regression
print("(b) Coefficients for Polynomial Regression:")
print(model_poly.params)

# Print standard error of the estimate (Sy/x) for polynomial regression
syx_poly = np.sqrt(model_poly.mse_resid)
print(f"(b) Standard Error of the Estimate (Sy/x) for Polynomial Regression: {syx_poly:.4f}")

# Confidence Intervals for polynomial regression
ci_poly = model_poly.conf_int(alpha=alpha)

# Confidence Interval for Intercept (beta_0)
print(f"(b) 95% Confidence Interval for Intercept (beta_0) for Polynomial Regression: {ci_poly[0, 0]:.4f} - {ci_poly[0, 1]:.4f}")

# Confidence Interval for Coefficient of X1 (beta_1)
print(f"(b) 95% Confidence Interval for Coefficient of X1 (beta_1) for Polynomial Regression: {ci_poly[1, 0]:.4f} - {ci_poly[1, 1]:.4f}")

# Confidence Interval for Coefficient of X2 (beta_2)
print(f"(b) 95% Confidence Interval for Coefficient of X2 (beta_2) for Polynomial Regression: {ci_poly[2, 0]:.4f} - {ci_poly[2, 1]:.4f}")

# Confidence Interval for Coefficient of X1^2 (beta_3)
print(f"(b) 95% Confidence Interval for Coefficient of X1^2 (beta_3) for Polynomial Regression: {ci_poly[3, 0]:.4f} - {ci_poly[3, 1]:.4f}")

# Confidence Interval for Coefficient of X2^2 (beta_4)
print(f"(b) 95% Confidence Interval for Coefficient of X2^2 (beta_4) for Polynomial Regression: {ci_poly[4, 0]:.4f} - {ci_poly[4, 1]:.4f}")

# Print R-squared for polynomial regression
print(f"(b) Coefficient of Determination (R-squared) for Polynomial Regression: {model_poly.rsquared:.4f}")

# Print Correlation Coefficient for polynomial regression
correlation_coefficient_poly = np.corrcoef(Y, model_poly.fittedvalues)[0, 1]
print(f"(b) Correlation Coefficient for Polynomial Regression: {correlation_coefficient_poly:.4f}")

