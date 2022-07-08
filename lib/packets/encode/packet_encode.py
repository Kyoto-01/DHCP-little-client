import lib.packets.encode.options as options
from ..constants import *


def build(msg_type):
    op = OP_REQUEST
    htype = bytes([0x01])
    hlen = bytes([0x06])
    hops = bytes([0x00])
    xid = bytes([0xcd, 0x29, 0xaf, 0x6a])
    secs = bytes([0x00, 0x00])
    flags = bytes([0x00, 0x00])
    ciaddr = bytes([0x00, 0x00, 0x00, 0x00])
    yiaddr = bytes([0x00, 0x00, 0x00, 0x00])
    siaddr = bytes([0x00, 0x00, 0x00, 0x00])
    giaddr = bytes([0x00, 0x00, 0x00, 0x00])
    chaddr = bytes([0x04, 0x0e, 0x3c, 0xfc, 0x91, 0x35])
    chaddr_pad = bytes(padding_generator(16 - len(chaddr)))
    sname = bytes(padding_generator(64))
    file = bytes(padding_generator(128))
    magic = bytes([0x63, 0x82, 0x53, 0x63])
    opts = options.get_options(msg_type)

    pkt = (
        op + htype + hlen + hops + xid + secs + flags +
        ciaddr + yiaddr + siaddr + giaddr + chaddr + chaddr_pad + sname +
        file + magic + opts
    )

    return pkt


def padding_generator(length, value=0x00):
    return [value for _ in range(length)]
