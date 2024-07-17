from socket import *

client_port=9955 

# code of TCP client
connectionSocket = socket(AF_INET,SOCK_STREAM)
connectionSocket.connect(('127.0.0.1',client_port))

example_student="1202057" 
connectionSocket.send(example_student.encode())

response = connectionSocket.recv(1024).decode()
print(response) 

connectionSocket.close()