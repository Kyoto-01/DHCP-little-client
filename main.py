import socket
#import packet


port = 6700
      
def discover():

    host = '255.255.255.255'

    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM) 
    sock.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)
    server_address = (host, port) 
    print ("Connecting to %s port %s" % server_address)

    #message = packet.discover()
    message = bytes([0x01, 0x02, 0x03, 0xfe, 0xcc, 0xde, 0x3a])

    print ("Sending discover")
    sock.sendto(message, server_address)
    amount_received = 0
    amount_expected = len(message)

    while amount_received < amount_expected:
        data = sock.recvfrom(16)
        amount_received += len(data)
        print ("Received: ", data)

discover()