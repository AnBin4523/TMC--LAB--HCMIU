import numpy as np
from scipy import stats
import matplotlib.pyplot as plt

# Given data
data = np.array([28.65, 26.55, 26.65, 27.65, 27.35, 28.35, 26.85, 
                 28.65, 29.65, 27.85, 27.05, 28.25, 28.85, 26.75, 
                 27.65, 28.45, 28.65, 28.45, 31.65, 26.35, 27.75,
                 29.25, 27.65, 28.65, 27.65, 28.55, 27.65, 27.25])

# (a) Mean
mean_value = np.mean(data)

# (b) Standard Deviation
std_deviation = np.std(data)

# (c) Variance
variance = np.var(data)

# (d) Coefficient of Variation
coeff_of_variation = (std_deviation / mean_value) * 100

# (e) 90% Confidence Interval for the Mean
confidence_interval = stats.t.interval(0.9, len(data)-1, loc=mean_value, scale=stats.sem(data))

# (f) Histogram
plt.hist(data, bins=np.arange(26, 32.5, 0.5), edgecolor='black')
plt.title('Histogram of the Given Data')
plt.xlabel('Values')
plt.ylabel('Frequency')
plt.show()

# (g) Range Encompassing 68% of Readings (assuming normal distribution)
lower_range = mean_value - std_deviation
upper_range = mean_value + std_deviation

# Print results
print(f"(a) Mean: {mean_value}")
print(f"(b) Standard Deviation: {std_deviation}")
print(f"(c) Variance: {variance}")
print(f"(d) Coefficient of Variation: {coeff_of_variation}")
print(f"(e) 90% Confidence Interval: {confidence_interval}")
print(f"(g) Range Encompassing 68% of Readings: ({lower_range}, {upper_range})")