from socket import *

msg = "\r\n I love computer networks!"
endmsg = "\r\n.\r\n"
server = "localhost"
port = 25
emailFrom = "mallroy@notexisting.org"
emailto = "ramanchumber1@gmail.com"

# Choose a mail server
mailserver = (server, port)

#Create socket called clientSocket and establish a TCP connection with mailserver

clientSocket = socket(AF_INET, SOCK_STREAM)
clientSocket.connect(mailserver)
recv = clientSocket.recv(1024)
print(recv)
if recv[:3] != '220':
    print('220 reply not received from server.')

# Send HELO command and print server response.

heloCommand = 'HELO Alice\r\n'
clientSocket.send(heloCommand)
recv1 = clientSocket.recv(1024)
print("Message after HELO command:" + recv1)
if recv1[:3] != '250':
    print('250 reply not received from server.')

# Send Mail From command and print server response.

mailFrom = "MAIL FROM:" + emailFrom + "\r\n"
clientSocket.send(mailFrom)
recv2 = clientSocket.recv(1024)
print("After MAIL FROM command: " +recv2)

# Send RCPT To command and print server response

rcptTo = "RCPT TO:" + emailto + "\r\n"
clientSocket.send(rcptTo)
recv3 = clientSocket.recv(1024)
print("After RCPT TO command: " +recv3)

# Send DATA command and print server response.

data = "DATA\r\n"
clientSocket.send(data)
recv4 = clientSocket.recv(1024))
print("After DATA command: " +recv4)

# Send message data

subject = "Subject: This is Email Spoofing demo for CSC 255 class.\r\n\r\n"
clientSocket.send(subject)
clientSocket.send(msg)
clientSocket.send(endmsg)

recv_msg = clientSocket.recv(1024)
print("Response after sending message body:"+recv_msg)

# Send Quit command and get server response.


clientSocket.send("QUIT\r\n")
recv5 = clientSocket.recv(1024)
print(recv5)
clientSocket.close()
