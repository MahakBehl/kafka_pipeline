
from data_generator import generate_random_purchase_data

if __name__ == "__main__":
    from requests import Session
    with Session() as sess:
        for i in range(10):
            data = generate_random_purchase_data()
            print(data)
            sess.post("http://localhost:8000/shop_data", json=data)
