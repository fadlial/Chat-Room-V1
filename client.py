#Client
from threading import Thread
import socket

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
try:
    s.connect(('8.8.8.8', 1))
    local_ip_address = s.getsockname()[0]
    print "Server IP >>>>" + local_ip_address
    print "\n"
except:
    print "Server IP >>>> Localhost, 127.0.0.1"

ThreadCount = 0
ip = raw_input("IP SERVER : ")
port = raw_input("Port : ")
name = raw_input("NAMA/NICKNAME : ")
class MySendingThread(Thread):
    def __init__(self, mySocket):
        Thread.__init__(self)
        self.mySocket = mySocket

    def run(self):
        while True:
            data = raw_input("Reply : ")
            if data == "" :
                msg = ""
            else:
                print "\n"
                self.mySocket.send(name+" : " +data.encode())
            if data == "[e]":
                message = name + " Left chat room! Off"
                self.mySocket.send(message.encode())
                print "\n"
                self.mySocket.close()
                break

class MyReceivingThread(Thread):
    def __init__(self, mySocket):
        Thread.__init__(self)
        self.mySocket = mySocket

    def run(self):
        while True:
            try:
                msg = self.mySocket.recv(1024)
                if msg.decode() == "" :
                    msg =""
                else:
                    print "\n"
                    print str(msg.decode())
            except:
                self.mySocket.close()
                break

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((ip, int(port)))
print "Connected Succesfully..!"
mySendingThread = MySendingThread(s)
myReceiveThread = MyReceivingThread(s)
mySendingThread.start()
myReceiveThread.start()
