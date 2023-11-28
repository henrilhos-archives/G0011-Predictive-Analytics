import pymongo
import pandas as pd

client = pymongo.MongoClient(
    "mongodb://username:password@localhost:27017/?authSource=admin"
)
db = client["ecommerce"]

products_data = list(db.products.find())
sales_data = list(db.sales.find())

# Convert do DataFrames
products_df = pd.DataFrame(products_data)
sales_df = pd.DataFrame(sales_data)

# Extract _id from the product field in inventory_df and sales_df
sales_df["product"] = sales_df["product"].apply(lambda x: x["_id"])

sales_df.to_csv("sales_data.csv", index=False)

# Merge data from different collections based on relationships
merged_df = pd.merge(
    sales_df,
    products_df,
    left_on="product",
    right_on="_id",
    suffixes=("_sales", "_product"),
)

# Drop unnecessary columns
merged_df = merged_df.drop(columns=["_id_sales", "product", "_id_product"])

# Save the merged data to a CSV file
merged_df.to_csv("merged_data.csv", index=False)

# Close MongoDB connection
client.close()
