import numpy as np
import statsmodels.api as sm
from scipy.stats import t

# Given data
X_data = np.array([3, 4, 5, 7, 8, 9, 11, 12])
Y_data = np.array([1.6, 3.6, 4.4, 3.4, 2.2, 2.8, 3.8, 4.6])

# Create design matrix X with a constant term and cubic term
X_poly = np.column_stack([np.ones_like(X_data), X_data, X_data**2, X_data**3])

# Fit the OLS model for polynomial regression
model_poly = sm.OLS(Y_data, X_poly).fit()

# Print coefficients
print("Coefficients for Cubic Equation:")
print(model_poly.params)

# Print R-squared
r_squared = model_poly.rsquared
print(f"R-squared: {r_squared:.4f}")

# Print standard error of the estimate (Sy/x)
syx_poly = np.sqrt(model_poly.mse_resid)
print(f"Standard Error of the Estimate (Sy/x) for Cubic Equation: {syx_poly:.4f}")

# Confidence Intervals for polynomial regression
alpha = 0.05  # 95% confidence interval
t_critical = t.ppf(1 - alpha/2, model_poly.df_resid)

# Confidence Intervals for Coefficients
ci_poly = model_poly.conf_int(alpha=alpha)

# Print Confidence Intervals for Coefficients
for i, coeff in enumerate(model_poly.params):
    print(f"95% Confidence Interval for Coefficient {i}: {ci_poly[i, 0]:.4f} - {ci_poly[i, 1]:.4f}")
