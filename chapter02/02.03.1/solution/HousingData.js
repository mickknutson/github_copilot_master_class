const seaborn = require('seaborn');
const pandas = require('pandas');
// Describe: Function to create a univariate and bivariate analysis on dataset.
function performAnalysis(datasetPath) {
  // Load the dataset using pandas
  const dataset = pandas.read_csv(datasetPath);

  // Perform univariate analysis
  seaborn.displot(dataset);

  // Perform bivariate analysis
  //CRIM,ZN
  seaborn.jointplot(x='column1', y='column2', data=dataset);
}

performAnalysis('/Users/mickknutson/Documents/workspace/BASELOGIC/github_copilot_master_class/chapter02/02.03.1/solution/HousingData.csv');
