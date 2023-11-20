#!/usr/bin/env python3
##RAM Reader - An arbitrary RAM dumper for UV-K5
##needs corresponding mod and libuvk5 library installed

import sys,struct
import serial
import libuvk5

if len(sys.argv)<4: print('cmd05DB_ramreader.py <COMx> <address> <len> [filename]') ; sys.exit(1)
com_port = sys.argv[1]
address  = int(sys.argv[2],0)
data_len = int(sys.argv[3],0)

if len(sys.argv)>4:
    filename = sys.argv[4]
else:
    filename = None

with libuvk5.uvk5(com_port) as radio:
    radio.debug=False
    if radio.connect():
        reply=radio.read_mem(address,data_len)

if filename is not None:
    open(filename,'wb').write(reply)
else:
    print('[{}]'.format(', '.join(format(int(x), '#04x') for x in reply)))