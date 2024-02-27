# Describe: Function to create a univariate and bivariate analysis on dataset.
import pandas as pd
import seaborn as sns

def analyze_data():
    # Load the dataset
    data = pd.read_csv('/Users/mickknutson/Documents/workspace/BASELOGIC/github_copilot_master_class/chapter02/02.03.1/solution/HousingData.csv')

    # Univariate analysis
    # Example: Histogram of a numerical variable
    #sns.histplot(data['SalePrice'])
    sns.displot(data);

    # Bivariate analysis
    # Example: Scatter plot of two numerical variables
    #sns.scatterplot(x='GrLivArea', y='SalePrice', data=data)

    # Show the plots
    #sns.plt.show()

# Call the function to perform the analysis
analyze_data()
