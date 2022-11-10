import socket
import time

HOST_UR = "192.168.100.11"
PORT_UR = 29999

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST_UR, PORT_UR))
    # s.sendall(b"play")
    # time.sleep(3)
    s.sendall(b"stop")
    data = s.recv(1024)
    print (f"Recieved {data!r}")
    # s.close