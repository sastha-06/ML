import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

my_filepath=r"C:\Users\sasth\OneDrive - Kumaraguru College of Technology\ML\data.csv"
my_data=pd.read_csv(my_filepath,encoding="latin1")
print(my_data.head())
print(my_data.tail())
print(my_data.info())
print(my_data.describe())
print(my_data.isnull())
print(my_data.columns)
top_products = my_data.groupby('Description')['Quantity'].sum().sort_values(ascending=False).head(10)
plt.figure(figsize=(10,8))
sns.lineplot(x=top_products.values,y=top_products.index)
plt.title("Top 10 Products by Sales Quantity")
plt.xlabel("Total Quantity Sold")
plt.ylabel("Product Name")
plt.show()
plt.figure(figsize=(10,8))
sns.barplot(x=top_products.values,y=top_products.index)
plt.title("Top 10 Products by Sales Quantity")
plt.xlabel("Total Quantity Sold")
plt.ylabel("Product Name")
plt.show()


