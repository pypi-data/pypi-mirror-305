from abc import ABC, abstractmethod

import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns


class MultivariateAnalysisTemplate(ABC):

    def analyze(self, df: pd.DataFrame):
        self.generate_correlation_heatmap(df)
        self.generate_pairplot(df)

    @abstractmethod
    def generate_correlation_heatmap(self, df: pd.DataFrame):
        pass

    @abstractmethod
    def generate_pairplot(self, df: pd.DataFrame):
        pass


class SimpleMultivariateAnalysis(MultivariateAnalysisTemplate):

    def generate_correlation_heatmap(self, df: pd.DataFrame):
        _df = df.select_dtypes(include=[int, float])
        _df = _df.dropna(how="all", axis=1)
        plt.figure(figsize=(12, 8))
        sns.heatmap(_df.corr(), annot=True, fmt=".2f", cmap="coolwarm", linewidths=0.5)
        plt.title("Correlation Heatmap")
        plt.show()

    def generate_pairplot(self, df: pd.DataFrame):
        _df = df.dropna(how="all", axis=1)
        sns.pairplot(_df)
        plt.suptitle("Pairplot of Selected Features", y=1.02)
        plt.show()
