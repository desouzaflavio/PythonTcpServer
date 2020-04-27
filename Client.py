#Cliente para conexão TCP

import socket

HOST = "localhost"
PORT = 5000

tcp = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
dest = (HOST, PORT)

tcp.connect(dest)

print ('Para Sair pressione CTRL+x\n')
msg = input()
msg_encoded = msg.encode()

while msg != "\x18":
    tcp.send(msg_encoded)
    msg = input()
    msg_encoded = msg.encode()

tcp.close()