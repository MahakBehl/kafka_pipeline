from kafka import KafkaProducer


KAFKA_BROKER_URL = 'localhost:9092'

producer = KafkaProducer(bootstrap_servers=KAFKA_BROKER_URL)
producer.send('get-message', b'Hello')
producer.flush()