'''Kafka Producer'''

import random
from json import dumps

from kafka import KafkaProducer

MAX_RETRY = 5
producer = KafkaProducer(bootstrap_servers=['kafka0:9092', 'kafka1:9093', 'kafka2:9094',],
                         value_serializer=lambda x:
                         dumps(x).encode('utf-8'))

for _ in range(10):
    message = random.choice([{"type": "message"}, {"type": "error"}])

    print(message)
    ack = producer.send("main_topic", message)
    metadata = ack.get()
    print(
        f"Send to topic: '{metadata.topic}' partition: {metadata.partition} offset: {metadata.offset}")
producer.flush()
producer.close()
