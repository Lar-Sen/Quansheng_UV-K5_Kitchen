#!/usr/bin/env python3
##BK4819 RF chip register reader/writer
#Original idea and libuvk5 lib addon by @FAGCI
#Courtesy of LarSeN

import libuvk5
import sys,os

if len(sys.argv)<3: print(f'Usage: {os.path.basename(sys.argv[0])} <COMx> <read | write  regNum hexdata>') ; sys.exit(1)
arg_port = sys.argv[1]
action   = sys.argv[2]

with libuvk5.uvk5(arg_port) as radio:
    radio.debug=False
    if radio.connect():
        #print(radio.get_fw_version(), 'firmware')
        reply = radio.get_reg(int(sys.argv[3]))
        if action == 'read':
            print('\nregNum:', reply["reg"], '[', hex(reply["reg"]), ']', 'is now =', hex(reply["val"]), '\ndecodes as', format(int(reply["val"]),'016b'), '\nReplyCode:',reply["sta"])

        if action=='write': 
            if len(sys.argv)!=5: print(f'Usage: {os.path.basename(sys.argv[0])} <COMx> write regNum hexdata') ; sys.exit(1)
            print('\nReg [', hex(reply["reg"]), '] was = ', hex(reply["val"]))
            data = int(sys.argv[4],16)
            print('\nSet to = ', format(data, '016b'))
            if data > 65535: print(f'Error: register data exceeds 16 bits') ; sys.exit(1)
            reply=radio.put_reg(int(sys.argv[3]),data)
            print('\nregNum:', reply["reg"], '[', hex(reply["reg"]), ']', 'now reads = ', hex(reply["val"]), '\nReplyCode:',reply["sta"])
