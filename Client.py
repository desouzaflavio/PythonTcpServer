import socket

HOST = "localhost"
PORT = 5000

tcp = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
dest = (HOST, PORT)

tcp.connect(dest)

print 'Para Sair pressione CTRL+x\n'
msg = raw_input()

while msg <> '\x18':
    tcp.send(msg)
    msg = raw_input()

tcp.close()