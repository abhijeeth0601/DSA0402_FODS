import pandas as pd
import numpy as np

house_data = pd.read_csv("CSV_FILES/house.csv")

b = house_data[house_data['no_of_bed'] > 4]
print(f"The houses which have more than 4 bedrooms :\n {b}")

sales_prices = b['sale_price']

avg_sales_price = np.mean(list(sales_prices))

print(
    f"The Average Sale Price of house with more than four bedrooms in the neighborhood : {avg_sales_price}")
