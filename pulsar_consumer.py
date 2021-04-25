import pulsar
import time

class PulsarConsumer:

  def __init__(self, address, port):
    self.config = 'pulsar://' + address
    self.config = self.config.rstrip() + ':'
    self.config = self.config.rstrip() + str(port)
    self.config = self.config.rstrip()

    self.filename = "consumer_out.txt"
    self.write = open(self.filename, "w")
    
  def Setup(self):
    self.client = pulsar.Client(self.config)
    time.sleep(10)
    #persistent://sample/standalone/ns1/
    self.consumer = self.client.subscribe('my-topic', 'my-subscription')

  def Run(self):
    while True:
      msg = self.consumer.receive()
      print(msg)
      self.consumer.acknowledge(msg)
      ts = time.time()
      print(ts)
      self.write.write(str(ts) + "\n")

    self.client.close()
