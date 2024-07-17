from socket import *

server_port = 9966

serverSocket = socket(AF_INET,SOCK_STREAM)
serverSocket.bind(('',server_port))
serverSocket.listen(1)

print("The server is listen on port",server_port)

while True:
    connectionSocket, addr = serverSocket.accept()
    sentence = connectionSocket.recv(2048).decode()  
    print(addr)
    print(sentence)
    ip = addr[0]
    port = addr[1]
    
    request= sentence.split('/')
    R=request[1]
    print (R)

    

    ss = R.split(' ')
    print ("*******************")
    rec = ss[0]
    print ("The Request")
    print (rec)
    print ("*******************")
    

    # handle css file and photo
    if rec.endswith('.css'):
        connectionSocket.send("HTTP/1.1 200 OK\r\n".encode())   
        connectionSocket.send("Content-Type: text/css\r\n".encode())
        connectionSocket.send("\r\n".encode())
        cssFile = open("styles.css",'rb')
        connectionSocket.send(cssFile.read()) 

    if rec.endswith('yousef.jpg'):
        connectionSocket.send("HTTP/1.1 200 OK\r\n".encode())
        connectionSocket.send("Content-Type: image/jpeg \r\n".encode())
        connectionSocket.send("\r\n".encode())
        yousefImage = open("yousef.jpg",'rb')
        connectionSocket.send(yousefImage.read())

    if rec.endswith('anas.jpg'):
        connectionSocket.send("HTTP/1.1 200 OK\r\n".encode())
        connectionSocket.send("Content-Type: image/jpeg \r\n".encode())
        connectionSocket.send("\r\n".encode())
        anasImage = open("anas.jpg",'rb')
        connectionSocket.send(anasImage.read())

    if rec.endswith('details_background_Eng.png'):
        connectionSocket.send("HTTP/1.1 200 OK\r\n".encode())
        connectionSocket.send("Content-Type: image/png \r\n".encode())
        connectionSocket.send("\r\n".encode())
        details_background_Eng_Image = open("details_background_Eng.png",'rb')    
        connectionSocket.send(details_background_Eng_Image.read())

    if rec.endswith('details_background_Ar.png'):
        connectionSocket.send("HTTP/1.1 200 OK\r\n".encode())
        connectionSocket.send("Content-Type: image/png \r\n".encode())
        connectionSocket.send("\r\n".encode())
        details_background_Ar_Image = open("details_background_Ar.png",'rb')    
        connectionSocket.send(details_background_Ar_Image.read())    

    if rec.endswith('groupMember_background.png'):
        connectionSocket.send("HTTP/1.1 200 OK\r\n".encode())
        connectionSocket.send("Content-Type: image/png \r\n".encode())
        connectionSocket.send("\r\n".encode())
        groupMember_background_Image = open("groupMember_background.png",'rb')    
        connectionSocket.send(groupMember_background_Image.read())
        

    # handle redirects 
    if rec == '' or rec =='index.html' or rec =="main_en.html" or rec =="en":
        connectionSocket.send("HTTP/1.1 200 OK\r\n".encode())
        connectionSocket.send("Content-Type: text/html\r\n".encode())
        connectionSocket.send("\r\n".encode())
        htmlFile = open("main_en.html",'rb')
        connectionSocket.send(htmlFile.read())
        

    elif rec=='ar':
        # Send one HTTP header line into socket
        connectionSocket.send("HTTP/1.1 200 OK\r\n".encode())
        connectionSocket.send("Content-Type: text/html \r\n".encode())
        connectionSocket.send("\r\n".encode())
        htmlFile = open("main_ar.html",'rb')
        connectionSocket.send(htmlFile.read())    

    elif rec=='.html' or rec=='sample_html.html':
        connectionSocket.send("HTTP/1.1 200 OK\r\n".encode())
        connectionSocket.send("Content-Type: text/html \r\n".encode())
        connectionSocket.send("\r\n".encode())
        htmlFile = open("sample_html.html",'rb')
        connectionSocket.send(htmlFile.read()) 
    
    elif rec=='.css':
        connectionSocket.send("HTTP/1.1 200 OK\r\n".encode())
        connectionSocket.send("Content-Type: text/css \r\n".encode())
        connectionSocket.send("\r\n".encode())
        cssFile = open("styles.css",'rb')
        connectionSocket.send(cssFile.read()) 
    
    elif rec=='.png':
        connectionSocket.send("HTTP/1.1 200 OK\r\n".encode())
        connectionSocket.send("Content-Type: image/png \r\n".encode())
        connectionSocket.send("\r\n".encode())
        pngImage = open("groupMember_background.png",'rb')
        connectionSocket.send(pngImage.read()) 

    elif rec=='.jpg':
        connectionSocket.send("HTTP/1.1 200 OK\r\n".encode())
        connectionSocket.send("Content-Type: image/jpeg \r\n".encode())
        connectionSocket.send("\r\n".encode())
        jpgImage = open("yousef.jpg",'rb')
        connectionSocket.send(jpgImage.read())

    elif rec== 'cr':
        connectionSocket.send("HTTP/1.1 307 Temporary Redirect\r\n".encode())
        connectionSocket.send("Location: https://www.cornell.edu \r\n".encode())
        connectionSocket.send("Content-Type: text/html\r\n".encode())
        connectionSocket.send("\r\n".encode())
        connectionSocket.send("<html><body>Redirecting to Cornell...</body></html>".encode())
        connectionSocket.close()

    elif rec== 'so':
        connectionSocket.send("HTTP/1.1 307 Temporary Redirect\r\n".encode())
        connectionSocket.send("Location: https://stackoverflow.com \r\n".encode())
        connectionSocket.send("Content-Type: text/html\r\n".encode())
        connectionSocket.send("\r\n".encode())
        connectionSocket.send("<html><body>Redirecting to Stack OverFlow...</body></html>".encode())
        connectionSocket.close()

    elif rec== 'rt':
        connectionSocket.send("HTTP/1.1 307 Temporary Redirect\r\n".encode())
        connectionSocket.send("Location: https://ritaj.birzeit.edu \r\n".encode())
        connectionSocket.send("Content-Type: text/html\r\n".encode())
        connectionSocket.send("\r\n".encode())
        connectionSocket.send("<html><body>Redirecting to Ritaj...</body></html>".encode())
        connectionSocket.close()

    else:
        connectionSocket.send("HTTP/1.1 404 Not Found\r\n".encode())
        connectionSocket.send("Content-Type: text/html \r\n".encode())
        connectionSocket.send("\r\n".encode())
        s="<html> <head> <title>Error 404</title> </head> <body> <h1>Error 404</h1> <p style='color: red;'> The file is not found</p> <br> <p>Name: <strong><bold>Yousef Sharbi</bold></strong></p> <p>ID: <strong><bold>1202057</bold></strong></p> <br> <p>Name: <strong><bold>Anas Karakra</bold></strong></p> <p>ID: <strong><bold>1200467</bold></strong></p> <br> <p>Client IP Address: "+str(ip)+"<p>Client Port: "+str(port)+"</body> </html>"
        connectionSocket.send(s.encode())

    