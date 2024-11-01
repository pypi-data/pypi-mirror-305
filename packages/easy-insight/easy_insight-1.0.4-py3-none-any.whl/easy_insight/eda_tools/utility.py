import pandas as pd

from easy_insight.eda_tools.basic_data_inspection import (
    DataInspector,
    DataTypeInspectionStrategy,
    SummaryStatisticsInspectionStrategy,
)
from easy_insight.eda_tools.bivariate_analysis import (
    BivariateAnalyzer,
    CategoricalVsNumericalAnalysisStrategy,
)
from easy_insight.eda_tools.missing_values_analysis import SimpleMissingValuesAnalysis
from easy_insight.eda_tools.multivariate_analysis import SimpleMultivariateAnalysis
from easy_insight.eda_tools.univariate_analysis import (
    CategoricalUnivariateAnalysis,
    NumericalUnivariateAnalysis,
    UnivariateAnalyzer,
)


def auto_select_columns(df):
    """Automatically selects numerical and categorical columns from the DataFrame."""
    numerical_columns = df.select_dtypes(include=[int, float]).columns.tolist()
    categorical_columns = df.select_dtypes(
        include=[object, "category"]
    ).columns.tolist()
    return numerical_columns, categorical_columns


def quick_eda(df, perform_data_inspection=True, perform_missing_values_analysis=True,
              perform_univariate_analysis=True, perform_bivariate_analysis=True, perform_multivariate_analysis=True):
    """Performs a quick exploratory data analysis on the provided DataFrame based on user preferences."""
    
    numerical_cols, categorical_cols = auto_select_columns(df)

    if perform_data_inspection:
        # Data Inspection
        data_inspector = DataInspector(DataTypeInspectionStrategy())
        data_inspector.evaluate_inspection(df)

        # Summary Statistics
        data_inspector.set_strategy(SummaryStatisticsInspectionStrategy())
        data_inspector.evaluate_inspection(df)

    if perform_missing_values_analysis:
        # Missing Values Analysis
        missing_values_analysis = SimpleMissingValuesAnalysis()
        missing_values_analysis.analyze(df)

    if perform_univariate_analysis:
        # Univariate Analysis for Numerical Columns
        univariate_analyzer = UnivariateAnalyzer(NumericalUnivariateAnalysis())
        for feature in numerical_cols:
            univariate_analyzer.execute_analysis(df, feature=feature)

        # Univariate Analysis for Categorical Columns
        univariate_analyzer.set_strategy(CategoricalUnivariateAnalysis())
        for feature in categorical_cols:
            univariate_analyzer.execute_analysis(df, feature=feature)

    if perform_bivariate_analysis and categorical_cols and numerical_cols:
        # Bivariate Analysis
        bivariate_analysis = BivariateAnalyzer(CategoricalVsNumericalAnalysisStrategy())
        for cat_col in categorical_cols:
            for num_col in numerical_cols:
                bivariate_analysis.execute_analysis(df, cat_col, num_col)

    if perform_multivariate_analysis:
        # Multivariate Analysis
        multivariate_analysis = SimpleMultivariateAnalysis()
        multivariate_analysis.generate_correlation_heatmap(df)
