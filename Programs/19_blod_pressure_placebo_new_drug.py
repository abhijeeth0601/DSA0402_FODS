import scipy.stats as stats
import numpy as np
import pandas as pd

data = pd.read_csv("CSV_FILES/bp.csv")

mean_drug = np.mean(data['drug'])
std_drug = np.std(data['drug'], ddof=1)
n_drug = len(data['drug'])

mean_placebo = np.mean(data['placebo'])
std_placebo = np.std(data['placebo'], ddof=1)
n_placebo = len(data['placebo'])

# Calculate t-score for 95% confidence level
t_score = stats.t.ppf(0.975, df=min(n_drug - 1, n_placebo - 1))

# Calculate margin of error
margin_of_error_drug = t_score * (std_drug / np.sqrt(n_drug))
margin_of_error_placebo = t_score * (std_placebo / np.sqrt(n_placebo))

# Calculate confidence intervals
confidence_interval_drug = (
    mean_drug - margin_of_error_drug, mean_drug + margin_of_error_drug)
confidence_interval_placebo = (
    mean_placebo - margin_of_error_placebo, mean_placebo + margin_of_error_placebo)

# Print results
print("(Drug Group): ",
      confidence_interval_drug)
print("(Placebo Group): ",
      confidence_interval_placebo)
