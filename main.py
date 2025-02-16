import numpy as np
from scipy.stats import norm

exercise_minutes = np.array([132, 136, 101, 218, 50, 132, 151, 244, 117, 129, 181, 160, 179, 287, 221, 190, 
                             51, 282, 265, 78, 88, 199, 217, 219, 204, 80, 84, 273, 160, 164, 50, 196, 
                             118, 43, 271, 294, 82, 121, 293, 64, 235, 110, 79, 31, 83, 135, 289, 220, 
                             247, 73, 280, 0])

gpa = np.array([2.84, 2.79, 2.69, 2.91, 2.5, 2.69, 2.76, 3.09, 2.77, 2.58, 2.89, 2.78, 2.79, 3.14, 3.05, 
                2.97, 2.52, 3.03, 3.06, 2.75, 2.63, 2.88, 2.82, 2.82, 2.99, 2.8, 2.66, 3.15, 2.86, 2.76, 
                2.64, 3.05, 2.73, 2.74, 2.78, 3.17, 2.67, 2.71, 3.1, 2.5, 2.95, 2.76, 2.81, 2.51, 2.59, 
                2.72, 3.17, 2.97, 2.94, 2.7, 2.1, 2.4])

exercise_150_gpa = gpa[exercise_minutes >= 150]

mu_0 = 2.8 
sample_mean = np.mean(exercise_150_gpa)
sample_std = np.std(exercise_150_gpa, ddof=0) 
n = len(exercise_150_gpa)
z_score = (sample_mean - mu_0) / (sample_std / np.sqrt(n))
p_value = 1 - norm.cdf(z_score)
print(f"z_score: {z_score},p_value:{p_value}")
