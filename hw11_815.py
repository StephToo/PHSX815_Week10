import numpy as np
import matplotlib.pyplot as plt

# Generate 10000 samples with 50 random exponential variables
samples = np.random.exponential(scale=1, size=(10000, 50)) #https://blog.quantinsti.com/central-limit-theorem/
                                                            #https://sparkbyexamples.com/numpy/how-to-use-numpy-exponential-function/
# Find means of each sample
sample_means = np.mean(samples, axis=1) #https://www.geeksforgeeks.org/numpy-mean-in-python/

# Plot a histogram of the sample means
plt.hist(sample_means, bins=50)
plt.title('Distribution of sample means (n=50)')
plt.xlabel('Sample mean')
plt.ylabel('Frequency')
plt.show()
