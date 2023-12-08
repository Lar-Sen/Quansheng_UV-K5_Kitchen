#!/usr/bin/env python3
##Perform AES authentication, in order to gain R/W config access to a transceiver with an active password (not the Power-on one)
##Useful to recover from EEPROM misuse. Also permits custom key updating.
##Courtesy of LarSeN
#needs pycrypto lib installed

import libuvk5
import sys,os,struct
from Crypto.Cipher import AES
from os import urandom

##Quansheng backdoor AES key.
#If only need is remove password, please set 'customKey = masterKey' and run 'cmd052D_authenticate.py <COMx> unlock'
#masterKey = b'\x4A\xA5\xCC\x60\x03\x12\xCC\x5F\xFF\xD2\xDA\xBB\x6B\xBA\x7F\x92'

#my UUID_le
masterKey = b'\x0B\x02\x02\x01\x34\x46\x53\x0D\x10\xFF\x59\x52\x00\xA5\x00\x3F'

##You can set your own key if you want, by running 'cmd052D_authenticate.py <COMx> protect <your_key>' and editing 'customKey' below
#customKey = b'UVK5isFun'
customKey = masterKey

##--------------------- do not modify below this line ---------------------------------------------------
if len(sys.argv) < 2: print(f'Usage: {os.path.basename(sys.argv[0])} <COMx> [unlock] | [protect] <password>') ; sys.exit(1)

arg_port = sys.argv[1]
customKey = customKey + b'\x00'*(16 - len(customKey))

with libuvk5.uvk5(arg_port) as radio:
    if radio.connect():
        reply = radio.get_fw_version()
        print('\nAES Challenge :',reply["nonce"])
        challenge = struct.pack('>IIII',reply["nonce"][0],reply["nonce"][1],reply["nonce"][2],reply["nonce"][3])
        response = AES.new(customKey, AES.MODE_CBC, bytes(16)).encrypt(challenge)

        #B2l conversion the derpy way
        reply = struct.pack('<IIII', int.from_bytes(response[0:4],"big"), int.from_bytes(response[4:8],"big"), int.from_bytes(response[8:12],"big"), int.from_bytes(response[12:16],"big"))

        if radio.try_login(reply) == b'\x00':
            print('\nOK, access granted!')
            if (len(sys.argv) == 3) and (sys.argv[2] == 'unlock'):
                radio.set_cfg_mem(0x0F30, b'\xFF'*16)
                print('\nUser password now reset to (NULL)')

            if (len(sys.argv) == 4) and (sys.argv[2] == 'protect'):
                upwd = bytes(sys.argv[3], "ascii") + b'\x00'*(16 - len(sys.argv[3]))
                if len(upwd) == 16:
                    print('\nAbout to LOCK serial access to config!\nSure to set:', sys.argv[3],'as password to protect the device memory?')
                    if input(' Confirm [Y/n]') == 'Y':
                        upwd = struct.pack('<IIII', int.from_bytes(upwd[0:4],"big"), int.from_bytes(upwd[4:8],"big"), int.from_bytes(upwd[8:12],"big"), int.from_bytes(upwd[12:16],"big"))
                        print(upwd.hex())
                        radio.set_cfg_mem(0x0F30, upwd)
                else: print('\nProvided password is too long (max 16 char.)!')

        else: print('Something went wrong. Your firmware may not honor login process correctly.\nDid you provide the masterKey?')