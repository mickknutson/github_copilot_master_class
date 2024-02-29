# Describe: Function to create a univariate and bivariate analysis on dataset.
import os
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

def analyze_data():
    # Load the dataset
    data = pd.read_csv('./iris.csv')

    # Create .tmp directory if it does not exist
    if not os.path.exists('./tmp'):
        os.makedirs('./tmp')

    for i, feature in enumerate(data.columns[:-1], 1):
        sns.histplot(data[feature], kde=True)
        plt.savefig(f'./tmp/iris-histplot_{i}.png')
    
    sns.displot(data);
    plt.savefig('./tmp/iris-displot.png')

# Call the function to perform the analysis
analyze_data()
