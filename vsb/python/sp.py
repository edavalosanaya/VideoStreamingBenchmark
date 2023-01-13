import time
import zmq

context = zmq.Context()
zmq_socket = context.socket(zmq.PUB)
zmq_socket.bind("tcp://127.0.0.1:5555")

for x in range(1000):

    # zmq_socket.send_string("", zmq.SNDMORE)
    zmq_socket.send_pyobj(x,zmq.NOBLOCK)
    time.sleep(1)
    print(x)
