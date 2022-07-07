def get_options():
    return msg_type() + hostname() + request_list() + end()


def msg_type():
    name = bytes([0x35])
    length = bytes([0x01])
    dhcp = bytes([0x01])

    all = name + length + dhcp

    return all


def hostname():
    name = bytes([0x0c])
    length = bytes([0x0c])
    hostname = bytes([0x62, 0x61, 0x74, 0x6C, 0x65, 0x6F, 0x0A])

    all = name + length + hostname

    return all


def request_list():
    name = bytes([0x37])
    length = bytes([0x0d])
    mask = bytes([0x01])
    brd_addr = bytes([0x1c])
    time_offset = bytes([0x02])
    router = bytes([0x03])
    domain_name = bytes([0x0f])
    dname_server = bytes([0x06])
    domain_search = bytes([0x77])
    hostname = bytes([0x0c])
    netbios_ns = bytes([0x2c])
    netbios_scope = bytes([0x2f])
    int_mtu = bytes([0x1a])
    classless_static_route = bytes([0x79])
    ntp_servers = bytes([0x2a])

    all = (
        name + length + mask + brd_addr + time_offset
        + router + domain_name + dname_server + domain_search + hostname
        + netbios_ns + netbios_scope + int_mtu + classless_static_route + ntp_servers
    )

    return all


def end():
    name = bytes([0xff])
    padding = bytes([
        0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00
    ])
    
    all = name + padding

    return all
