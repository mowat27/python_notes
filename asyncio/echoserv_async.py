from socket import *
import asyncio

'''
Starts an echo server that uses asyncio to handle 
multiple connections
'''


async def echo_server(address, loop):
    sock = socket(AF_INET, SOCK_STREAM)
    sock.bind(address)
    sock.listen(1)
    sock.setblocking(False)
    print('Starting server')
    while(True):
        client, addr = await loop.sock_accept(sock)
        print('Connection from', addr)
        loop.create_task(echo_handler(client, loop))


async def echo_handler(client, loop):
    while True:
        data = await loop.sock_recv(client, 100000)
        if not data:
            break
        await loop.sock_sendall(client, b'Got: ' + data)
    print('Connection closed')
    client.close()


if __name__ == '__main__':
    # you can connect to server in the shell using
    # `nc localhost 26000`
    loop = asyncio.get_event_loop()
    loop.run_until_complete(echo_server(('', 26000), loop))
