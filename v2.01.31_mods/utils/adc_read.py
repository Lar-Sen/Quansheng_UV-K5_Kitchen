#!/usr/bin/env python3
import libuvk5
import sys,os,struct,time

if len(sys.argv)!=2: print(f'Usage: {os.path.basename(sys.argv[0])} <COMx> ') ; sys.exit(1)

arg_port = sys.argv[1]

with libuvk5.uvk5(arg_port) as radio:
    radio.debug=False
    if radio.connect():
        _=radio.get_fw_version()
        calib_data = radio.get_cfg_mem(0x1F40,12)
        calib_coef = struct.unpack('<6H',calib_data)[3]
        while True:
            x = radio.get_adc()
            print('{:.4f} V (RAW={})  | RAW Charge current={})'.format(760*x["volt"]/calib_coef/100, x["volt"], x["amp"]))
            time.sleep(5)