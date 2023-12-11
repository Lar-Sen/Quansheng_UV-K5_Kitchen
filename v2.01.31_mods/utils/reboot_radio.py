#!/usr/bin/env python3
import libuvk5
from sys import argv,exit
from os import path

if len(argv)!=2: print(f'Usage: {path.basename(argv[0])} <COMx> ') ; exit(1)

arg_port = argv[1]

with libuvk5.uvk5(arg_port) as radio:
    if radio.connect():
        if radio.reboot(): print('\nReboot request sent.')