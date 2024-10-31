# Easy Insight (One Click - Easy Exploratory Data Analysis)

**Easy Insight** is a simple library designed for exploratory data analysis (EDA) 📊. It provides an easy way to inspect and analyze datasets, helping you to quickly understand the structure and contents of your data 📈.

## Features 

- 🔍 Basic data inspection
- ❓ Missing values analysis
- 📊 Univariate analysis for numerical and categorical features
- 🔗 Bivariate analysis for understanding relationships between variables
- 🌐 Multivariate analysis for comprehensive insights

## Installation ⚙️

You can install Easy Insight using [Poetry](https://python-poetry.org/) or `pip`.

### Using Poetry

1. Install Poetry if you haven't already:

   ```bash
   curl -sSL https://install.python-poetry.org | python3 -
   ```

2. Then run:

   ```bash
   poetry add easy-insight
   ```

### Using pip

```bash
pip install easy-insight
```

## Usage 🚀

Here's a quick example of how to use Easy Insight for exploratory data analysis on a DataFrame `df`:

```python
import pandas as pd

from easy_insight.eda_tools.basic_data_inspection import DataInspector, DataTypeInspectionStrategy, SummaryStatisticsInspectionStrategy

from easy_insight.eda_tools.missing_values_analysis import SimpleMissingValuesAnalysis

from easy_insight.eda_tools.univariate_analysis import UnivariateAnalyzer, NumericalUnivariateAnalysis, CategoricalUnivariateAnalysis

from easy_insight.eda_tools.bivariate_analysis import BivariateAnalyzer, NumericalVsNumericalAnalysisStrategy, CategoricalVsNumericalAnalysisStrategy

from easy_insight.eda_tools.multivariate_analysis import SimpleMultivariateAnalysis
```

## Load your DataFrame (example) 📂

```python
df = pd.read_csv('your_dataset.csv')
```

## Quick Automated EDA ⚡

### For Quick automated EDA

```python
from easy_insight.eda_tools.utility import quick_eda

quick_eda(df, perform_data_inspection=True, perform_missing_values_analysis=True,
          perform_univariate_analysis=True, perform_bivariate_analysis=True, perform_multivariate_analysis=True)
```

## For Quick but Customized EDA 🛠️

### Data Inspection

```python
data_inspector = DataInspector(DataTypeInspectionStrategy())
data_inspector.evaluate_inspection(df)
```

### Set strategy to Summary Statistics

```python
data_inspector.set_strategy(SummaryStatisticsInspectionStrategy())
data_inspector.evaluate_inspection(df)
```

### Missing Values Analysis❓

```python
missing_values_analysis = SimpleMissingValuesAnalysis()
missing_values_analysis.analyze(df)
```

### Univariate Analysis 📊

```python
univariate_analyzer = UnivariateAnalyzer(NumericalUnivariateAnalysis())
numerical_columns = df.select_dtypes(include=[int, float]).columns
for feature in numerical_columns:
    univariate_analyzer.execute_analysis(df, feature=feature)
```

### Bivariate Analysis 🔗

```python
bivariate_analysis = BivariateAnalyzer(CategoricalVsNumericalAnalysisStrategy())
bivariate_analysis.execute_analysis(df, "department", "annual_salary")
```

### Multivariate Analysis 🌐

```python
multivariate_analysis = SimpleMultivariateAnalysis()
multivariate_analysis.analyze(df)
```

## Contributing 🤝

Contributions are welcome! Please feel free to submit a pull request or open an issue for any suggestions or bugs you encounter.

## License 📝

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Author ✍️

Durgesh Rathod - [durgeshrathod.777@gmail.com](mailto:durgeshrathod.777@gmail.com) 
