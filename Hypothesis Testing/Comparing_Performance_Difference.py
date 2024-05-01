from scipy import stats

"""

Assuming,

mu1 = Performance of Decision Tree (J48)
mu2 = Performance of Neural Network (Multilayer Perception)

H0 : mu1 = mu2
H1:  mu1 != mu2

alpha = 0.05

"""

# Decision Tree (J48)
mean_DT = 71.13 # mean accuracy
std_dev_DT = 3.46 # standard deviation
n_DT = 30 # sample size

# Neural Network (Multilayer Perception)
mean_NN = 67.56 # mean accuracy
std_dev_NN = 3.53 # standard deviation
n_NN = 30 # sample size

# Independent t-test
# Calculating the t-statistic and p-value
t_statistic, p_value = stats.ttest_ind_from_stats(mean_DT, std_dev_DT, n_DT, mean_NN, std_dev_NN, n_NN)

print("t-statistic:", t_statistic)
print("p-value:", p_value)

# Checking if the p-value falls in the rejection region or not
if p_value < 0.05:
    print("The p-value is less than 0.05, \n"
          "This suggests we reject the null hypothesis.\n"
          "We have sufficient evidence to claim that there is a significant difference in the performance of the two "
          "algorithms.")
else:
    print("The p-value is greater than 0.05, \n"
          "This suggests we fail to reject the null hypothesis.\n"
          "We have insufficient evidence to claim that there is no significant difference in the "
          "performance of the two algorithms.")
