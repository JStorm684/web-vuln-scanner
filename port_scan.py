import socket

def scan_ports(host):
    open_ports = []

    for port in [80, 443, 21, 22]:
        s = socket.socket()
        s.settimeout(1)
        try:
            s.connect((host, port))
            open_ports.append(port)
        except:
            pass
        s.close()

    return open_ports
