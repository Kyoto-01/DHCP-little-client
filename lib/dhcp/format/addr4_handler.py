def get_hex_addr(addr: str):
    hex_octects = bytes(map(
        lambda octect: int(octect),
        addr.split('.')
    ))

    return hex_octects