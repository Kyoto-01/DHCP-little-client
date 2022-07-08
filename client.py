from lib.packets.encode.packet_encode import build
from lib.packets.decode.packet_decode import decode
from lib.packets.constants import *
import lib.packets.encode.options as options

import socket

      
data_payload = 16


def client(addr='0.0.0.0', port=68, server='255.255.255.255'):

    server_address = (server, 67) 

    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM) 
    sock.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)

    offer_data = discover(sock, server_address)

    if offer_data:
        ack_data = request(sock, server_address)
    
    return ack_data


def discover(sock, server_address):
    pkt = build(DHCP_DISCOVER)
    
    print ("Sending discover")

    sock.sendto(pkt, server_address)

    data = sock.recvfrom(data_payload)

    print ("Offer received")

    return data


def request(sock, server_address):
    pkt = build(DHCP_REQUEST)
    
    print ("Sending request")

    sock.sendto(pkt, server_address)

    data = sock.recvfrom(data_payload)

    print ("Ack received")

    return data


dhcp_data = client()

print(dhcp_data)