"""
"""

from kafka import KafkaProducer, KafkaConsumer
from kafka.errors import KafkaError

topic = "AWSKafkaExample"
producer = KafkaProducer(
    bootstrap_servers=[
        "b-1.sanhe-dev.8htiks.c17.kafka.us-east-1.amazonaws.com:9094",
        "b-2.sanhe-dev.8htiks.c17.kafka.us-east-1.amazonaws.com:9094",
        "b-3.sanhe-dev.8htiks.c17.kafka.us-east-1.amazonaws.com:9094",
    ],
    security_protocol="SSL",
)
message = "goodjob".encode("utf-8")
future = producer.send(topic, key=message, value=message)
# producer.flush()
# Block for 'synchronous' sends
try:
    record_metadata = future.get(timeout=10)
except KafkaError:
    # Decide what to do if produce request failed...
    print(KafkaError)
    pass

print(record_metadata.topic)
print(record_metadata.partition)
print(record_metadata.offset)