from ._base import BaseImage


class Kafka(BaseImage):
    label = 'kafka'
    name = 'kafka'
    port = 9092

    def check(self):
        from kafka import KafkaClient
        try:
            KafkaClient(bootstrap_servers=f"{self.host}:{self.get_port()}")
            return True
        except ValueError:
            pass
        return False


kafka_image = Kafka()
