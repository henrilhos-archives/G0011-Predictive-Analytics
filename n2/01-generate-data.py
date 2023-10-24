import random
from datetime import datetime, timedelta

import pymongo
from faker import Faker

client = pymongo.MongoClient(
    "mongodb://username:password@localhost:27017/?authSource=admin"
)
db = client["ecommerce"]

fake = Faker()


def date_to_datetime(date_obj):
    return datetime.combine(date_obj, datetime.min.time())


products_count = 10000
categories = ("Electronics", "Clothes", "Food", "Toys")

# Create a list of products with fictitious attributes
products = []
for _ in range(products_count):
    product = {
        "name": fake.unique.catch_phrase(),
        "category": fake.random_element(elements=categories),
        "supplier": fake.company(),
        "price": round(random.uniform(5.0, 200.0), 2),
    }
    products.append(product)

products_collection = db["products"]
product_ids = products_collection.insert_many(products).inserted_ids

inventory = []
sales = []
for product_id in product_ids:
    product = products_collection.find_one({"_id": product_id})
    initial_inventory = random.randint(0, 200)
    sales_per_day = random.randint(0, 5)
    current_inventory = initial_inventory

    for _ in range(30):
        sale_date = date_to_datetime(
            fake.date_between(start_date="-1y", end_date="today")
        )
        sold_amount = random.randint(0, min(current_inventory, sales_per_day))
        recipe = sold_amount * product["price"]

        current_inventory -= sold_amount

        if sold_amount > 0:
            sales.append(
                {
                    "product": product,
                    "sale_date": sale_date,
                    "sold_amount": sold_amount,
                    "recipe": round(recipe, 2),
                }
            )

    inventory.append(
        {
            "product": product,
            "initial_inventory": initial_inventory,
            "current_inventory": current_inventory,
        }
    )

inventory_collection = db["inventory"]
sales_collection = db["sales"]

inventory_collection.insert_many(inventory)
sales_collection.insert_many(sales)
