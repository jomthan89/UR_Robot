import socket
import time
from colorama import Fore, Back, Style
# import cv2


Status_start = False
Status_Auto = False
Loop_start = True

Server_HOST = input("IP Server_HOST.: ")
Server_PORT = input("(6099) Server_POST.: ")
Robot_UR_HOST = input("(192.168.100.11) IP UR.: ")
Robot_UR_PORT = input("(29999) POST UR.: ")

HOST = str(Server_HOST)#"192.168.100.40"  # Standard loopback interface address (localhost)
PORT = int(Server_PORT)#6099  # Port to listen on (non-privileged ports are > 1023)
HOST_UR = str(Robot_UR_HOST)#"192.168.100.11"  # The server's hostname or IP address
PORT_UR = int(Robot_UR_PORT)#29999  # The port used by the server

try:
    while True:

        val_status = input("start or auto or stopProgram >>\nPlease enter the command.: ")
        print("")
        Status_start = False
        Status_Auto = False

        if val_status == 'start':
            Status_start = True
            Status_Auto = False
            
        elif val_status == 'auto':
            Status_start = False
            Status_Auto = True
            
        elif val_status == 'stopprogram':
            Status_start = False
            Status_Auto = False
            break
        else :
            print(f"{Fore.RED} >>> Please select follow the menu <<< {Style.RESET_ALL}")

        if Status_start :
            with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as cam:
                cam.bind((HOST, PORT))
                cam.listen()
                conn, addr = cam.accept()
                with conn:
                    print(f"Connected by {addr}")
                    while True:
                        #data = conn.recv()
                        #if not data:
                        #    break
                        conn.send("ZGSCAN_MSG53001".encode())
                        print(f"{Fore.GREEN} >>> Reset camera ...{Style.RESET_ALL}")
                        time.sleep(10)
                        conn.send("ZGSCAN_MSG510002".encode())
                        print(f"{Fore.GREEN} >>> Select mode ...{Style.RESET_ALL}")
                        time.sleep(5)
                        conn.send("ZGSCAN_MSG54".encode())
                        print(f"{Fore.GREEN} >>> Start camera ...{Style.RESET_ALL}")
                        time.sleep(5)
                        
                        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
                            s.connect((HOST_UR, PORT_UR))
                            s.sendall(b"play")
                            data = s.recv(1024)
                            print(f" >>> Received from Robot: {data!r} <<< ")
                            
                            print(f"{Fore.GREEN} >>> Start Robot {Style.RESET_ALL}")
                            print(f"{Fore.YELLOW} >>> Stop Program Ctrl + c ... {Style.RESET_ALL}")

                        time.sleep(35)    
                        conn.send("ZGSCAN_MSG52".encode())
                        print(f"{Fore.GREEN} >>> Stop camera ...{Style.RESET_ALL}")
                        time.sleep(15)
                        conn.send("ZGSCAN_MSG690003C:\\Users\EN-RB02\Desktop\CX Automation\Monitoring\mesh.stl".encode())
                        print(f"{Fore.GREEN} >>> Export mesh Plz ...{Style.RESET_ALL}")
                        time.sleep(10)
                        
                        print(f"{Fore.CYAN} >>> Complete 1 Time <<< {Style.RESET_ALL}")
                        break
        
        elif Status_Auto :
            with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as cam:
                cam.bind((HOST, PORT))
                cam.listen()
                conn, addr = cam.accept()
                with conn:
                    print(f"Connected by {addr}")

                    Loop_start = True
                    while True:
                        #data = conn.recv()
                        #if not data:
                        #    break
                        if Loop_start :
                            conn.send("ZGSCAN_MSG53001".encode())
                            print(f"{Fore.GREEN} >>> Reset camera Plz wait 10s...{Style.RESET_ALL}")
                            time.sleep(10)
                            conn.send("ZGSCAN_MSG510002".encode())
                            print(f"{Fore.GREEN} >>> Select camera Plz wait 5s...{Style.RESET_ALL}")
                            time.sleep(5)
                            conn.send("ZGSCAN_MSG54".encode())
                            print(f"{Fore.GREEN} >>> Start camera Plz wait 5s...{Style.RESET_ALL}")
                            time.sleep(5)

                        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
                            s.connect((HOST_UR, PORT_UR))
                            s.sendall(b"play")
                            data = s.recv(1024)
                            print(f" >>> Received {data!r} <<< ")
                            print(f"{Fore.GREEN} >>> Robot is Running... {Style.RESET_ALL}")
                            print(f"{Fore.YELLOW} >>> Stop Program Ctrl + c ... {Style.RESET_ALL}")
                            
                            Loop_start = False
                        time.sleep(35)

    print(f"{Fore.CYAN} >>> The program has stopped. <<< {Style.RESET_ALL}")
    print('')

except KeyboardInterrupt :
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect((HOST_UR, PORT_UR))
        s.sendall(b"stop")
        data = s.recv(1024)
        print(f" >>> Received {data!r} <<< ")
        
        print(f"{Fore.GREEN} >>> Robot Stopping... {Style.RESET_ALL}")
        print(f"{Fore.CYAN} >>> Complete.... <<< {Style.RESET_ALL}")
        
    

