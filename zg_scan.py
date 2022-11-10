import socket
import time

t = 0

HOST = "127.0.0.1" #ip loopback สำหรับให้โปรแกรมเชื่อมต่อ
PORT = 6099
# HOST_UR = "192.168.100.11"
# PORT_UR = 29999

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM) #เรียกใช้ socket
s.bind((HOST, PORT))
s.listen()
conn, addr = s.accept()
with conn:
    print(f"Connect by {addr}")

    while True:
        conn.send("ZGSCAN_MSG510001".encode())
        time.sleep(2)
        conn.send("ZGSCAN_MSG510002".encode())
        time.sleep(2)
        conn.send("ZGSCAN_MSG54".encode())
        time.sleep(10)
        conn.send("ZGSCAN_MSG52".encode())
        time.sleep(5)

# with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
#     s.bind((HOST, PORT))
#     s.listen()
#     conn, addr = s.accept()
#     with conn:
#         print(f"Connected by {addr}")

#         while True:
#             conn.send("ZGSCAN_MSG510001".encode())
#             time.sleep(5)
#             conn.send("ZGSCAN_MSG510002".encode())
#             time.sleep(7)
#             conn.send("ZGSCAN_MSG54".encode())
#             time.sleep(100)
#             conn.send("ZGSCAN_MSG52".encode())
#             time.sleep(5)