from socket import *

'''
Starts an echo server with a problem; the first connection
blocks requests from the second connection until it has 
closed
'''


def echo_server(address):
    sock = socket(AF_INET, SOCK_STREAM)
    sock.bind(address)
    sock.listen(1)
    print('Starting server')
    print('Socket is a', type(sock))
    while(True):
        client, addr = sock.accept()
        print('Connection from', addr)
        print('Client is a', type(client))
        echo_handler(client)


def echo_handler(client):
    while True:
        data = client.recv(100000)
        if not data:
            break
        client.sendall(b'Got: ' + data)
    print('Connection closed')
    client.close()


if __name__ == '__main__':
    echo_server(('', 25000))
    # connect to server in the shell using
    # `nc localhost 25000`
