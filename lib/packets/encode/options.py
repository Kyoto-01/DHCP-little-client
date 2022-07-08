from ..constants import *
import lib.dhcp.format.addr4_handler as addr4
import socket


def get_options(msg_type):
    return dhcp_msg_type(msg_type) + req_addr() + hostname() + request_list() + end()


def dhcp_msg_type(msg_type):
    name = OPT_DHCP_MESSAGE_TYPE
    length = bytes([0x01])
    dhcp = msg_type

    all = name + length + dhcp

    return all


def hostname():
    name = OPT_HOST_NAME
    length = bytes([0x07])
    hostname = bytes([0x62, 0x61, 0x74, 0x6C, 0x65, 0x6F, 0x0A])

    all = name + length + hostname

    return all


def req_addr():
    name = OPT_DHCP_REQUESTED_ADDRESS
    length = bytes([0x04])

    hostname = socket.gethostname()
    addr = socket.gethostbyname(hostname)
    addr = addr4.get_hex_addr(addr)

    all = name + length + addr

    return all


def request_list():
    name = OPT_DHCP_PARAMETER_REQUEST_LIST
    length = OPT_BOOT_SIZE
    mask = OPT_SUBNET_MASK
    brd_addr = OPT_BROADCAST_ADDRESS
    time_offset = OPT_TIME_OFFSET
    router = OPT_ROUTERS
    domain_name = OPT_DOMAIN_NAME
    dname_server = OPT_DOMAIN_NAME_SERVERS
    domain_search = OPT_DOMAIN_SEARCH
    hostname = OPT_HOST_NAME
    netbios_ns = OPT_NETBIOS_NAME_SERVERS
    netbios_scope = OPT_NETBIOS_SCOPE
    int_mtu = OPT_INTERFACE_MTU
    classless_static_route = OPT_CLASSLESS_STATIC_ROUTE
    ntp_servers = OPT_NTP_SERVERS

    all = (
        name + length + mask + brd_addr + time_offset
        + router + domain_name + dname_server + domain_search + hostname
        + netbios_ns + netbios_scope + int_mtu + classless_static_route + ntp_servers
    )

    return all


def end():
    name = OPT_END
    
    all = name

    return all
