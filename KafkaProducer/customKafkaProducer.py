from confluent_kafka import Producer
import json

class CustomKafkaProducer:
    def __init__(self, brokers = ['localhost']):
        self.brokers = brokers
        self.conf = {
            'bootstrap.servers': self.brokers
        }
        self.customProducer = Producer(self.conf)

        
    def customProduce(self, topic, key, value, callback = :
        try:
            self.customProducer.produce(topic, )
        except Exception as e:
            print(e)