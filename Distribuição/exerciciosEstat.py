from scipy.stats import binom

p = 1 - 0.3314 - 0.1252

print(binom.cdf(5,20,p))

