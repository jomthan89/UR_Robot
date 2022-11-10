import socket
import time
from colorama import Fore, Back, Style
# import cv2

# HOST = "127.0.0.1" #ip loopback สำหรับให้โปรแกรมแสกนเชื่อมต่อ
# PORT = 6099
# HOST_UR = "192.168.100.11"
# PORT_UR = 29999

Server_HOST = input("IP Server For ZG_Camera: ")
Server_PORT = input("Server Port (6099): ")
Robot_UR_HOST = input("IP UR_Robot (192.168.100.11): ")
Robot_UR_PORT = input("UR_Robot Port (29999): ")

HOST = str(Server_HOST)#"192.168.100.40"  # Standard loopback interface address (localhost)
PORT = int(Server_PORT)#6099  # Port to listen on (non-privileged ports are > 1023)
HOST_UR = str(Robot_UR_HOST)#"192.168.100.11"  # The server's hostname or IP address
PORT_UR = int(Robot_UR_PORT)#29999  # The port used by the server

try:
    cam = socket.socket(socket.AF_INET, socket.SOCK_STREAM) #เรียกใช้ socket
    cam.bind((HOST, PORT))
    cam.listen()
    print(f"{Fore.GREEN} >>> Connecting to ZG_Camera <<< {Style.RESET_ALL}")
    conn, addr = cam.accept()
    with conn:
        print(f"Connect by {addr}")

        while True:
            conn.send("ZGSCAN_MSG530001".encode())
            print(f"{Fore.GREEN} >>> Reset Camera <<< {Style.RESET_ALL}")
            time.sleep(10)
            print(f"{Fore.GREEN} >>> Select Camera Mode <<< {Style.RESET_ALL}")
            conn.send("ZGSCAN_MSG510001".encode())
            time.sleep(5)
            conn.send("ZGSCAN_MSG510002".encode())
            time.sleep(5)
            print(f"{Fore.GREEN} >>> Start Camera <<< {Style.RESET_ALL}")
            conn.send("ZGSCAN_MSG54".encode())
            time.sleep(5)
            
            print(f"{Fore.GREEN} >>> Connecting to UR_Robot <<< {Style.RESET_ALL}")
            with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s: #เรียกใช้ socket
                s.connect((HOST_UR, PORT_UR))
                print(f"{Fore.GREEN} >>> Start UR_Robot <<< {Style.RESET_ALL}")
                s.send ("play\n".encode('utf8')) #เริ่มทำงาน
                # time.sleep(3) #ดีเลย์ 3 วินาที
                # s.send ("set_digital_out(2,False)" + "\n".encode('utf8')) #ให้ digital 2 ดับ
                # #s.send ("set_digital_out(2,False)" + "\n".encode()) #เขียนได้เหมือนกัน
                # time.sleep(3) #ดีเลย์ 3 วินาที
                # scommand = "vgl0_grip(2,60)\n" #gripper จับ
                # s.send (str.encode(scommand))
                # time.sleep(3) #ดีเลย์ 3 วินาที
                # scommand = "movej ([1.537, -1.842, 1.768, -1.484, -1.484, -3.161], a=0.2, v=0.2, t=0, r=0)\n" #ขยับด้วย movej
                # s.send (str.encode(scommand))
                # time.sleep(3) #ดีเลย์ 3 วินาที
                # s.send (("movel([-0.540537125683036, -2.2018732555807086, -1.0986348160112505, -2. .6437150406384227, 3. 352864759694935, -1. .2294883935868013], a=1.3962634015954636, v=1.8471975511965976)" + "\n").encode('utf8')) #ขยับด้วย movel สั่งได้เหมือนกัน
                # time.sleep(3) #ดีเลย์ 3 วินาที
                # scommand = "vg10_release()\n" #gripper ปล่อย
                # s.send (str.encode(scommand))
                time.sleep(5) #ดีเลย์ 35 วินาที
                print(f"{Fore.GREEN} >>> Stop UR_Robot <<< {Style.RESET_ALL}")
                s.send ("stop\n".encode('utf8')) #หยุดทำงาน
                time.sleep(3)
                data = s.recv(1024) #อ่านค่า feedback จาก robot
                s.close() #ปิดการเชื่อมต่อ

            #--------------------------
            time.sleep(35)
            print(f"{Fore.GREEN} >>> Stop Camera <<< {Style.RESET_ALL}")    
            conn.send("ZGSCAN_MSG52".encode())
            time.sleep(15)
            print(f"{Fore.GREEN} >>> Export 3D Scan <<< {Style.RESET_ALL}")
            conn.send("ZGSCAN_MSG690003C:\\Users\EN-RB02\Desktop\CX Automation\Monitoring\mesh.stl".encode())
            time.sleep(10)
            
            print(f"{Fore.CYAN} >>> Done <<< {Style.RESET_ALL}")
            break
            # conn.send("ZGSCAN_MSG52".encode())
            # time.sleep(3)

        print ("Received messange from UR_Robot: ", repr(data)) #แสดงค่าที่อ่านมาจาก robot

except KeyboardInterrupt :
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect((HOST_UR, PORT_UR))
        print(f"{Fore.GREEN} >>> Stop UR_Robot <<< {Style.RESET_ALL}")
        s.send ("stop\n".encode('utf8')) #หยุดทำงาน
        
        data = s.recv(1024)
        print("Received messange from UR_Robot: ", repr(data))