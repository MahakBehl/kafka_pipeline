from kafka import KafkaConsumer

# Define the consumer configuration
consumer = KafkaConsumer(
    'delhaize-store',                        # Topic to subscribe to
    bootstrap_servers=['localhost:9092'],    # Kafka broker address
    auto_offset_reset='earliest',            # Start reading at the earliest offset
    enable_auto_commit=True,                 # Automatically commit offsets
    value_deserializer=lambda x: x.decode('utf-8')  # Deserialize message values
)

# Poll for new messages and process them
try:
    for message in consumer:
        print(f"Received message: {message.value} from partition: {message.partition} at offset: {message.offset}")
except KeyboardInterrupt:
    print("Consumer interrupted by user")
finally:
    consumer.close()
    print("Consumer closed")