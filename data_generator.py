import random
import datetime
import uuid

# Sample data
store_locations = ['Brussels','Gent','vilvoorde','Turnhout','Tienen','Morstel','Jodoigne','Hasselt','Halen','Bruges','Antwerp','Aalst']

product_catalog = [
    {"id": random.randint(1000, 9999), "name": "Apple", "price": 1.5},
    {"id": random.randint(1000, 9999), "name": "Banana", "price": 1.0},
    {"id": random.randint(1000, 9999), "name": "orange", "price": 2.5},
    {"id": random.randint(1000, 9999), "name": "pear", "price": 0.5},
    {"id": random.randint(1000, 9999), "name": "kiwi", "price": 2.0},
    {"id": random.randint(1000, 9999), "name": "Bread", "price": 2.0},
    {"id": random.randint(1000, 9999), "name": "croissant", "price": 1.4},
    {"id": random.randint(1000, 9999), "name": "baguette", "price": 2.9},
    {"id": random.randint(1000, 9999), "name": "cake", "price": 12.0},
    {"id": random.randint(1000, 9999), "name": "Water", "price": 1.0},
    {"id": random.randint(1000, 9999), "name": "Milk", "price": 1.2},
    {"id": random.randint(1000, 9999), "name": "soda", "price": 2.2},
    {"id": random.randint(1000, 9999), "name": "beer", "price": 3.5},
    {"id": random.randint(1000, 9999), "name": "wine", "price": 8.0},
    {"id": random.randint(1000, 9999), "name": "Eggs", "price": 2.5},
    {"id": random.randint(1000, 9999), "name": "Cheese", "price": 3.0},
    {"id": random.randint(1000, 9999), "name": "Tomato", "price": 0.8},
    {"id": random.randint(1000, 9999), "name": "Chicken", "price": 5.0}
]

def generate_random_date(start_date, end_date):
    """Generate a random date between start_date and end_date."""
    delta = end_date - start_date
    random_days = random.randint(0, delta.days)
    random_date = start_date + datetime.timedelta(days=random_days)
    return random_date

def generate_random_purchase_data():
    """Generate random purchase data for stores."""
    
    purchase_id = random.randint(100000, 999999)
    store_location = random.choice(store_locations)
    purchase_date = str(generate_random_date(datetime.date(2022, 1, 1), datetime.date(2023, 12, 31)))
        
    # Generate multiple products for a single purchase
    num_products = random.randint(1, 10)
    products = random.sample(product_catalog, num_products)
         
    record = {
        "purchase_id": purchase_id,
        "store": store_location,
        "date": purchase_date,
        "products": products
    }
       
    return record

# Generate 10 random purchase records
#purchase_data = generate_random_purchase_data(10)

# Print the generated data
#for record in purchase_data:
#    print(record)
