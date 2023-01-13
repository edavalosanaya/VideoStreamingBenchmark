import time
import zmq
import random

context = zmq.Context()
consumer_receiver = context.socket(zmq.SUB)    

consumer_receiver.setsockopt(zmq.CONFLATE, 1)

consumer_receiver.connect("tcp://localhost:5555") 
consumer_receiver.subscribe(b'')


while 1:

    d=random.randint(1,10)

    work = consumer_receiver.recv_pyobj()

    print(work,"  :",d)

    time.sleep(d)
