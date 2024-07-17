from socket import *
import time
import ctypes

server_port = 9955 
valid_studID=["1202057","1200467"] # valid student id list

# function to lock windows screen
def lock_screen_windows():
    ctypes.windll.user32.LockWorkStation()


# code of TCP server
serverSocket = socket(AF_INET,SOCK_STREAM)
serverSocket.bind(('127.0.0.1',server_port))
serverSocket.listen(1)

print("The server is listen on port",server_port,",and it wait a message from client...")

while True:
    connectionSocket, addr = serverSocket.accept()
    data = connectionSocket.recv(1024).decode()
    if data in valid_studID: # in case the student id is valid
        print("Student id: ",data)

        print("Windows will lock screen after 10 seconds") #1

        message="The sever will lock screen after 10 seconds" #2
        connectionSocket.send(message.encode()) 

        time.sleep(10) #3
        
        lock_screen_windows() #4    
    else: # in case the student id is invalid
        print("Invalid Student id !!!")    

    connectionSocket.close()