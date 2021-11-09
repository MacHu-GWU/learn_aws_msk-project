from kafka import KafkaProducer, KafkaConsumer

topic = "AWSKafkaExample"
consumer = KafkaConsumer(
    topic,
    # group_id='my-group',
    bootstrap_servers=[
        "b-1.sanhe-dev.8htiks.c17.kafka.us-east-1.amazonaws.com:9094",
        "b-2.sanhe-dev.8htiks.c17.kafka.us-east-1.amazonaws.com:9094",
        "b-3.sanhe-dev.8htiks.c17.kafka.us-east-1.amazonaws.com:9094",
    ],
    security_protocol="SSL",
)

for message in consumer:
    print(message)