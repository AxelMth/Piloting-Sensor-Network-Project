#! /usr/bin/env python
#
# Do not modify

from optparse import OptionParser
import sys

parser = OptionParser()
parser.add_option("-i", "--ip_address",
                  help="set IPv6 address to the address passed as argument to estblish the connection with the CoAP server.",
                  action="store", type="string" , default=False, nargs=1,
                  dest="ip_address")
parser.usage = """%prog [options] [file]"""
parser.description = "Set "

(options, args) = parser.parse_args()

if not options.ip_address:
    print(parser.print_help())
    sys.exit()

else:
    command = "coap get "
    ip_address = options.ip_address
    coap_server = "coap://["+ip_address+"]"
    port = ":5683"
    output1 = "/sensor/accel"
    string = command + coap_server + port + output1
    #result = subprocess.check_output(string, shell=True)
    print(string)
