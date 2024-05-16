from fastapi import FastAPI
from kafka import KafkaProducer
import json

app = FastAPI()

# Kafka producer setup
KAFKA_BROKER_URL = 'localhost:9092'
TOPIC_NAME = 'delhaize-store'

# Initialize Kafka producer
producer = KafkaProducer(bootstrap_servers='localhost:9092',value_serializer=lambda v: json.dumps(v).encode('utf-8'))
print(producer, producer.bootstrap_connected())

# API endpoint to receive shop data
@app.post("/shop_data")
async def data(shop_data:dict):
    producer.send('delhaize-store', shop_data)
    producer.flush()
    return {"status": "ok"}
    """
    if producer.bootstrap_connected() is True:
        producer.send('delhaize-store', shop_data)
        producer.flush()
        return {"status": "ok"}
    else:
        print("Bootstrap not connected")
    """