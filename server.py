import socket
import time

def server_program():
    # get the hostname
    # host = socket.gethostname()
    # host = "127.0.0.1"
    hostname = socket.gethostname()
    host = socket.gethostbyname(hostname)
    port = 6099  # initiate port no above 1024

    # host = "192.168.100.1" #ต่อ โปรแกรม 3D
    # port1 = 6099

    server_socket = socket.socket()  # get instance
    # look closely. The bind() function takes tuple as argument
    server_socket.bind((host, port))  # bind host address and port together

    print("Server IP: " + str(host)) #show ip server
    print("Port: " + str(port))
    # configure how many client the server can listen simultaneously
    server_socket.listen(2)
    conn, address = server_socket.accept()  # accept new connection
    print("Connection from: " + str(address))
    while True:
        # receive data stream. it won't accept data packet greater than 1024 bytes
        data = conn.recv(1024).decode()
        if not data:
            # if data is not received break
            break
        print("from connected user: " + str(data))
        # # data = input(' -> ')
        # data = "Server has recieve messange."
        # conn.send(data.encode())  # send data to the client
   
    conn.send("ZGSCAN_MSG510001".encode())
    time.sleep(3)
    conn.send("ZGSCAN_MSG510002".encode())

    # conn.close()  # close the connection


if __name__ == '__main__':
    server_program()