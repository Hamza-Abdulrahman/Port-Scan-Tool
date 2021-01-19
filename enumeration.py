
import socket

def get_service_name(p):
    try:
        return socket.getservbyport(p)
    except:
        return "UNKNOWN"

def get_service_version(s,target,port):
    try :
        s.settimeout(5)
        s.connect((target,port))
        v = s.recv(1024).decode().strip()
        if v == '': raise ValueError 
    except :
        v = "UNKNOWN"
    
    return v
