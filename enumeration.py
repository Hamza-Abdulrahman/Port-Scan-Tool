
import socket

def get_service_name(p):
    try:
        return socket.getservbyport(p)
    except:
        return "UNKNOWN"

