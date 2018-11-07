import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.neural_network import MLPRegressor
from sklearn.metrics import mean_squared_error
from sklearn.preprocessing import normalize
import math

print("Reading Input Files..")
product = pd.read_csv('Product.csv')
store = pd.read_csv('Store.csv')
prod_store = pd.read_csv('ProductStore.csv')
sales = pd.read_csv('Saleslog.txt')

print("Joining tables, preprocessing and normalizing data")
df = prod_store.merge(product, on='Product_id')
df = df.merge(store, on='Store_id')
df = df.merge(sales, on=['Product_id', 'Store_id'])

# free memory
del product
del store
del prod_store
del sales

# Remove Useless columns
df = df.drop(['Product_id', 'Store_id', 'Sale_date'], axis=1)
df = df.fillna(0)

y = df[['Sale_amount']].values.flatten()
df = df.drop(['Sale_amount'], axis=1)
x = df.values

print("Splitting into train and test sets 80-20")
x_train, x_test, y_train, y_test = train_test_split(x, y, train_size=0.8, test_size=0.2)

x_train = normalize(x_train)
x_test = normalize(x_test)
# free memory
del x
del y

model = MLPRegressor([32], max_iter=200, verbose=1)

print("Training model\n")
print(model)

model.fit(x_train, y_train)
y_pred = model.predict(x_test)
rmse = math.sqrt(mean_squared_error(y_test, y_pred))
print(rmse)
