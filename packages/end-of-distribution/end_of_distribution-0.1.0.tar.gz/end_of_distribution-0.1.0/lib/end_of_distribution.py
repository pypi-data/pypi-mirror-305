import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

class EndOfDistribution:
    def __init__(self, data):
        self.data = np.array(data)
    
    def z_score_outliers(self, threshold=3):
        mean = np.mean(self.data)
        std_dev = np.std(self.data)
        z_scores = (self.data - mean) / std_dev
        outliers = self.data[np.abs(z_scores) > threshold]
        return outliers
    
    def iqr_outliers(self):
        Q1 = np.percentile(self.data, 25)
        Q3 = np.percentile(self.data, 75)
        IQR = Q3 - Q1
        lower_bound = Q1 - 1.5 * IQR
        upper_bound = Q3 + 1.5 * IQR
        outliers = self.data[(self.data < lower_bound) | (self.data > upper_bound)]
        return outliers
    
    def plot_distribution(self):
        plt.figure(figsize=(10, 5))
        plt.hist(self.data, bins=30, alpha=0.6, color='g')
        plt.title('Data Distribution')
        plt.xlabel('Value')
        plt.ylabel('Frequency')
        plt.axvline(np.mean(self.data), color='r', linestyle='dashed', linewidth=1, label='Mean')
        plt.axvline(np.percentile(self.data, 25), color='b', linestyle='dashed', linewidth=1, label='Q1')
        plt.axvline(np.percentile(self.data, 75), color='y', linestyle='dashed', linewidth=1, label='Q3')
        plt.legend()
        plt.show()
