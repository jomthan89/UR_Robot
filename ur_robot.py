import socket
import time

HOST = "192.168.100.11"
PORT = 29999

print ("Starting Program")

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM) #เรียกใช้ socket
s.connect((HOST, PORT)) #เชื่อมต่อด้วย tcp

#เริ่มโปรแกรมตรงนี้
s.send ("play\n".encode('utf8')) #เริ่มทำงาน
time.sleep(3) #ดีเลย์ 3 วินาที
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
time.sleep(50) #ดีเลย์ 10 วินาที
s.send ("stop\n".encode('utf8')) #หยุดทำงาน
#--------------------------

data = s.recv(1024) #อ่านค่า feedback จาก robot
s.close() #ปิดการเชื่อมต่อ

print ("Received", repr(data)) #แสดงค่าที่อ่านมาจาก robot