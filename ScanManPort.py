#!/usr/bin/python3

import socket
from optparse import *
def banner():
    print("""""")

parser = OptionParser("""
\033[1;33m This is a simple tool that enables you to check the activated services

\033[1;32mAuthored by Hamza-Abdulrahman
    github: https://github.com/Hamza-Abdulrahman/

Use -h to ask for help
""")
parser.add_option("-i","--target",dest="target",type="string",help="Enter your target")
parser.add_option("-p","--ports",dest="ports",type="int",help="Enter the last IP you want to check")
parser.add_option("-t","--outtime",dest="out_time",type="int",help="Enter the Out Time you want")

(options,args) = parser.parse_args()

if options.target == None or options.ports == None or options.out_time == None or options.help :
    print(parser.usage)
else:
    target = str(options.target)
    ports = int(options.ports)
    
    for p in range(1,ports):
        
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        out_time = int(options.out_time)
        s.settimeout(out_time)
        requist = s.connect_ex((target,p))
        try:
            if requist == 0 :
                service = socket.getservbyport(p)
                print(f"\033[0;35m {p}\033[0;33m is open ------>\033[0;35m {service}")
            else:
                False
        except:
            continue