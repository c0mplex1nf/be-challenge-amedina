from abc import ABC

class QueueClientInterface(ABC):

    def consume(self, loop):
        raise NotImplemented()

    def process_incoming_message(self, message):
        raise NotImplemented()

    def send_message(self, message):
        raise NotImplemented()
    
