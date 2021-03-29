import socket

import json
HOST = '127.0.0.1'
PORT = 7000


s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((HOST, PORT))

while True:
    outdata = input('please input message: ')
    print('send: ' + outdata)

    message = [{"src":"src1", "outdata":outdata}]
    jmsg1 = json.dumps(message)
    s.sendall(jmsg1.encode())
    #s.send(outdata.encode())
    
    indata = s.recv(1024)

    #jresp = json.loads(indata.decode())
    #print ("Recv: ",jresp)
    
    if len(indata) == 0: # connection closed
        s.close()
        print('server closed connection.')
        break
    print('recv: ' + indata.decode())







