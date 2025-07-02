import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

df=pd.read_excel(r"project\titan dt.xlsx")
print(df.head())

print(df.columns)

df.info()

print(df.isnull().sum())
mean_age = df['Age'].mean()
df['Age'].fillna(mean_age, inplace=True)
df.drop(columns=['Cabin'], inplace=True)
df = df.dropna(subset=['Embarked'])
print(df.isnull().sum())


# Heatmap of Correlations
numeric_df = df.select_dtypes(include='number')
sns.heatmap(numeric_df.corr(), annot=True, cmap='coolwarm')
plt.title('Correlation Heatmap')
plt.show()


# Age Distribution
sns.histplot(df['Age'], bins=30, kde=True)
plt.title('Age Distribution')
plt.xlabel('Age')
plt.ylabel('Count')
plt.show()

# Survival Count
sns.countplot(x='Sex', hue='Survived', data=df)
plt.title('Survival by Sex')
plt.show()


# age vs fare
sns.scatterplot(x='Age', y='Fare', hue='Survived', data=df)
plt.title('Age vs Fare colored by Survival')
plt.show()

# pclass vs fare  
sns.boxplot(x='Pclass', y='Fare', data=df)
plt.title('Fare by Passenger Class')
plt.show()