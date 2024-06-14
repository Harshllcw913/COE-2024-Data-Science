import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load the dataset
file_path = 'Titanic.csv'
titanic_df = pd.read_csv(file_path)

#Shape
titanic_df.shape

#describing the dataset 
titanic_df.descibe()

#info about the dataset
titanic_df.info()

#finding the null values 
titanic_df.isnull().sum()

# Drop rows with missing 'Embarked' values
titanic_df.dropna(subset=['Embarked'], inplace=True)

# Impute missing 'Age' values with the median
titanic_df['Age'].fillna(titanic_df['Age'].median(), inplace=True)

# Drop the 'Cabin' column
titanic_df.drop(columns=['Cabin'], inplace=True)

# Set up the matplotlib figure
plt.figure(figsize=(14, 8))

# Plot box plots for numerical columns
numerical_cols = ['Age', 'Fare', 'SibSp', 'Parch']
for i, col in enumerate(numerical_cols, 1):
    plt.subplot(2, 2, i)
    sns.boxplot(x=titanic_df[col])
    plt.title(f'Box plot of {col}')

plt.tight_layout()
plt.show()

# Define a function to remove outliers based on IQR
def remove_outliers(df, column):
    Q1 = df[column].quantile(0.25)
    Q3 = df[column].quantile(0.75)
    IQR = Q3 - Q1
    lower_bound = Q1 - 1.5 * IQR
    upper_bound = Q3 + 1.5 * IQR
    return df[(df[column] >= lower_bound) & (df[column] <= upper_bound)]

# Apply the function to each numerical column
for col in numerical_cols:
    titanic_df = remove_outliers(titanic_df, col)

# Check the shape of the dataframe after removing outliers
titanic_df.shape
