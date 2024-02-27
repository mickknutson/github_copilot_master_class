# Describe: Function to create a univariate and bivariate analysis on dataset.
import os
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

def analyze_data():
    # Load the dataset
    data = pd.read_csv('./HousingData.csv')

    # Create .tmp directory if it does not exist
    if not os.path.exists('./tmp'):
        os.makedirs('./tmp')

    # Univariate analysis
    # Example: Histogram of a numerical variable
    sns.histplot(data['MEDV'])

    plt.savefig('./tmp/housing-histplot.png')

    sns.displot(data);
    plt.savefig('./tmp/housing-displot.png')

    # TODO: Add this in the future...
    # Bivariate analysis
    # Example: Scatter plot of two numerical variables
    #sns.scatterplot(x='GrLivArea', y='SalePrice', data=data)
    #plt.savefig('./tmp/scatterplot.png')


# Call the function to perform the analysis
analyze_data()
