#!/usr/bin/python

import subprocess
import sys, getopt

def main(argv):
    ip_address = ''
    try:
        opts, args = getopt.getopt(argv,"hi:",["ip_address="])
    except getopt.GetoptError:
        print('test.py -i <ip_address>')
        sys.exit(2)
    for opt, arg in opts:
        if opt == '-h':
            print('test.py -i <ip_address>')
            sys.exit()
        elif opt in ("-i", "--ip_address"):
            ip_address = arg
    print('Ip address is ' + ip_address)
    command = "coap get "
    coap_server = "coap://["+ip_address+"]"
    port = ":5683"
    output1 = "/sensor/accel"
    string = command + coap_server + port + output1
    #result = subprocess.check_output(string, shell=True)
    print(string)

if __name__ == "__main__":
   main(sys.argv[1:])
