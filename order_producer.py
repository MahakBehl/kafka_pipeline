import json
import time

from kafka import KafkaProducer, producer

ORDER_KAFKA_TOPIC = "delhaize-store"
ORDER_LIMIT = 100

producer = KafkaProducer(bootstrap_servers="localhost:9092")

print("Going to generating order after 10 seconds")
print("will generate one unique order every 10 seconds")

for i in range(1,ORDER_LIMIT):
    data = ()

