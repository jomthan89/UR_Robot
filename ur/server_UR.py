import socket
import time

HOST = "127.0.0.1"
PORT = 6099
# HOST_UR = "192.168.100.11"
# PORT_UR = 29999

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((HOST, PORT))
    s.listen()
    conn, addr = s.accept()
    with conn:
        print(f"Connected by {addr}")

        while True:
            conn.send("ZGSCAN_MSG510001".encode())
            time.sleep(5)
            conn.send("ZGSCAN_MSG510002".encode())
            time.sleep(7)
            conn.send("ZGSCAN_MSG54".encode())
            time.sleep(100)
            conn.send("ZGSCAN_MSG52".encode())
            time.sleep(5)

        # conn.close()
        # break

# def ZG_Scan():
#     with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
#         s.bind((HOST, PORT))
#         s.listen()
#         conn, addr = s.accept()
#         with conn:
#             print(f"Connected by {addr}")

#             conn.send("ZGSCAN_MSG510001".encode())
#             time.sleep(3)
#             conn.send("ZGSCAN_MSG54".encode())
#             # conn.close()
#             # break

# def UR():
#     with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
#         s.connect((HOST_UR, PORT_UR))
#         s.sendall(b"play")
#         data = s.recv(1024)

#     print (f"Recieved {data!r}")
#     # s.close