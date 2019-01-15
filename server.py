#import socket module
from socket import *

#Assign a port number
myserverPort=12000
myServer = socket(AF_INET, SOCK_STREAM)

#Bind the socket to server port and server address
myServer.bind(('',myserverPort))

#Listen to one connection at a time
myServer.listen(1)
print('The server is ready to connect and available on port:',myserverPort)


while True:
    #Establish the connection
    print('Ready to serve...')

    #Set up new connection 
    socketConn, addr = myServer.accept()
    try:
        #Receives request from the client
        message = socketConn.recv(1024)
        filename = message.split()[1]
        print(filename,'||',filename[1:])
        fl = open(filename[1:], 'rb')
        #Store the entire content in a temporary file
        outputdata = fl.read()
        socketConn.send(bytes('\nHTTP/1.1 200 OK\n\n', "UTF-8"))
        socketConn.send(outputdata)
        socketConn.close()
        fl.close()

    except IOError:
        print("File not found!!")
        socketConn.send(bytes('\nHTTP/1.1 404 Not Found\n\n', "UTF-8"))
        fl = open('invalid.html', 'rb')
        outputdata = fl.read()
        socketConn.send(outputdata)
        fl.close()
    #except FileNotFoundError:
       # print("Invalid file, file not found")
    except IndexError:
        print("Index out of range")
        pass
              
