#Server Chat
from threading import Thread
import socket

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
try:
    s.connect(('8.8.8.8', 1))
    local_ip_address = s.getsockname()[0]
    print "Server IP >>>>" + local_ip_address
    print "\n"
except:
    print "Server IP >>>> Localhost , 127.0.0.1"

ThreadCount = 0
ip = raw_input("IP SERVER : ")
port = raw_input("Port : ")
name = raw_input("Nama/Nickname : ")

print('Waiting for a Connection...')

class SendingThread(Thread):
    def __init__(self, mySocket):
        Thread.__init__(self)
        self.mySocket=mySocket

    def run(self):
        while True:
            data = raw_input("Reply : ")
            if data == "" :
                msg = ""
            else:
                print("\n")
                self.mySocket.send(name +" :" + data.encode())
            if data == "[e]":
                self.mySocket.close()
                break
class ReceivingThread(Thread):
    def __init__(self, mySocket):
        Thread.__init__(self)
        self.mySocket = mySocket
    def run(self):
        while True:
            try:
                msg = self.mySocket.recv(1024)
                if msg.decode() == "":
                    msg = ""
                else:
                    print "\n"
                    print(str(msg.decode()))
            except:
                print "Server Shutdown! Off"
                self.mySocket.close()
                break

s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.bind((ip, int(port)))
s.listen(10)
while True:
    mySocket, address = s.accept()
    print "\n Connected :" + address[0] + "-" + str(address[1])
    sendThread = SendingThread(mySocket)
    receiveThread = ReceivingThread(mySocket)
    sendThread.start()
    receiveThread.start()
    ThreadCount += 1
    print ('Thread Number : ' + str(ThreadCount))
s.close()
           
