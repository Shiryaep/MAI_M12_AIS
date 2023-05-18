'''Kafka Consumer'''

import json

from kafka import KafkaConsumer, KafkaProducer


print("starting the consumer")
producer = KafkaProducer(bootstrap_servers=['kafka0:9092', 'kafka1:9093', 'kafka2:9094',],
                         value_serializer=lambda x:
                         json.dumps(x).encode('utf-8'))

consumer = KafkaConsumer(
    "main_topic",
    bootstrap_servers=['kafka0:9092', 'kafka1:9093', 'kafka2:9094',],
    auto_offset_reset='earliest', group_id="0")

for msg in consumer:
    try:
        # print(msg)
        print(msg.value)
        if msg.value.decode() != json.dumps({"type": "message"}):
            ack = producer.send(
                "dead_letter", json.loads(msg.value.decode()))
            metadata = ack.get()
            print(
                f"Send: '{metadata.topic}' partition: {metadata.partition} offset: {metadata.offset}")
            producer.flush()
            continue
        print("Done!")
    except Exception as e:
        print(e)
