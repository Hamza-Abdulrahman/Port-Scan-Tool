#!/usr/bin/python3

import socket
import sys
import time
import enumeration
from optparse import *

parser = OptionParser("""
\033[1;33m This is a simple tool that enables you to check the activated services

\033[1;32mAuthored by Hamza-Abdulrahman
    github: https://github.com/Hamza-Abdulrahman/

Use -h to ask for help
""",version="ScanManPort 1.0")

parser.add_option("-i","--target",dest="target",type="string",help="Enter your target")
parser.add_option("-p","--ports",dest="ports",default="1-1024",help="Enter the Range of Ports that you want to check it Ex(1-1024)")
parser.add_option("-t","--timeout",dest="timeout",default=0.5,help="Enter the Time Out that you want")
parser.add_option("-v","--services-version",action="store_true",dest="services_version",default=False,help="Get Services version")
parser.add_option("-o","--output",dest="output",help="Enter a FileName for save output")

(options,args) = parser.parse_args()

if not options.target :
    print(parser.usage)
else:
    print("Starting ScanManPort 2021 ......")
    time.sleep(2)
    target = str(options.target)
    if '-' in options.ports:
        start_range , end_range = str(options.ports).split("-")
    else:
        start_range = end_range = options.ports

    if options.output:
        file = open(options.output,'a')
    
    print(f"Host: {target}\n")
    
    for p in range(int(start_range),int(end_range)+1):
        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            timeout = float(options.timeout)
            s.settimeout(timeout)
            request = s.connect_ex((target,p))

            if request == 0 :
                service = enumeration.get_service_name(p)
                print(f"\033[0;34mPORT  \033[0;37m{p}  \033[0;34mSTATE  \033[0;37mopen  \033[0;34m",end='')
                print(f"SERVICE  \033[0;37m{service}",end = '')
                if options.output:
                    file.write(f"{service}:{target}:{p}")

                if options.services_version:
                    version = enumeration.get_service_version(s,target,p)
                    print(f"  \033[0;34mVERSION  \033[0;37m{version}",end='')
                    if options.output: 
                        file.write(f":{version}")

                if options.output:
                    file.write("\n")

                print()
        
        except KeyboardInterrupt:
            print("Stop the Scanning")
            sys.exit(1)

        except:
            continue

        finally:
            s.close()

    if options.output: file.close()

print("\nScan completed successfully")

