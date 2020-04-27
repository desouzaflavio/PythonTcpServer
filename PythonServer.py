import socket
import _thread

HOST = "localhost"
PORT = 5000

def conected(Conection, Client):
    print 'Conectado por', Client

    while True:
        msg = Conection.recv(1024)
        if not msg: break
        print Client, msg
        print 'Terminando conexão', Client
        
    Conection.close()
    _thread.exit()

tcp = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

origin = (HOST,PORT)
tcp.bind(origin)
tcp.listen(1)

while True:
    Conection, Client = tcp.accept()
    _thread.start_new_thread(conected, tuple([Conection, Client]))

tcp.close()


