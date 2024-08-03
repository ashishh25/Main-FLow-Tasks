import pandas as pd

# Load a CSV file
df = pd.read_csv('BigBasket Products.csv')

# Display the first few rows of the dataset
print("First few rows of the dataset:")
print(df.head())

# Check the structure of the dataset (number of rows and columns)
print("\nDataset structure (rows, columns):")
print(df.shape)

# Check the data types of each column
print("\nData types of each column:")
print(df.dtypes)

# Check for missing values
print("\nMissing values:")
print(df.isnull().sum())

# Impute missing values in the 'rating' column with the mean rating
df['rating'] = df['rating'].fillna(df['rating'].mean())

# Remove rows with missing values in 'product' and 'brand' columns
df = df.dropna(subset=['product', 'brand'])

# Fill missing 'description' with a placeholder like 'Not available'
df['description'] = df['description'].fillna('Not available')

# Confirming that missing values are handled
print(df.isnull().sum())

# Calculate summary statistics for numeric columns
summary_stats_numeric = df.describe()
print("Summary statistics for numeric columns:")
print(summary_stats_numeric)

# Calculate summary statistics for categorical columns
summary_stats_categorical = df.describe(include='O')  # include='O' specifies object (categorical) columns
print("\nSummary statistics for categorical columns:")
print(summary_stats_categorical)

C:\Users\Ashish\MainFLow_internship\pythonProject1\.venv\Scripts\python.exe C:\Users\Ashish\MainFLow_internship\pythonProject1\task2.py
First few rows of the dataset:
   index  ...                                        description
0      1  ...  This Product contains Garlic Oil that is known...
1      2  ...  Each product is microwave safe (without lid), ...
2      3  ...  A perfect gift for all occasions, be it your m...
3      4  ...  Multipurpose container with an attractive desi...
4      5  ...  Nivea Creme Soft Soap gives your skin the best...

[5 rows x 10 columns]

Dataset structure (rows, columns):
(27555, 10)

Data types of each column:
index             int64
product          object
category         object
sub_category     object
brand            object
sale_price      float64
market_price    float64
type             object
rating          float64
description      object
dtype: object

Missing values:
index              0
product            1
category           0
sub_category       0
brand              1
sale_price         0
market_price       0
type               0
rating          8626
description      115
dtype: int64
index           0
product         0
category        0
sub_category    0
brand           0
sale_price      0
market_price    0
type            0
rating          0
description     0
dtype: int64
Summary statistics for numeric columns:
              index    sale_price  market_price       rating
count  27553.000000  27553.000000  27553.000000  27553.00000
mean   13778.124342    322.529145    382.073872      3.94340
std     7954.838872    486.277432    581.747762      0.61257
min        1.000000      2.450000      3.000000      1.00000
25%     6889.000000     95.000000    100.000000      3.94341
50%    13778.000000    190.000000    220.000000      3.94341
75%    20667.000000    359.000000    425.000000      4.20000
max    27555.000000  12500.000000  12500.000000      5.00000

Summary statistics for categorical columns:
                             product  ...    description
count                          27553  ...          27553
unique                         23539  ...          21944
top     Turmeric Powder/Arisina Pudi  ...  Not available
freq                              26  ...            114

[4 rows x 6 columns]

Process finished with exit code 0
