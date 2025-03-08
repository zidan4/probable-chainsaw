import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load dataset
df = pd.read_csv("customer_churn.csv")  # Replace with your dataset

# Show first few rows
print(df.head())

# Check missing values
print(df.isnull().sum())

# Basic stats
print(df.describe())
