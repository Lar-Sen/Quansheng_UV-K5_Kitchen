#!/usr/bin/env python3

import libuvk5
from sys import argv,exit
from os import path
from binascii import hexlify

# Handle arguments
nargs = len(argv)
if (nargs < 2): print('\nMissing parameters. Please specify at least <pack> or <unpack>.');exit()

#-------- main ------------------
if argv[1]=='unpack':
    if nargs != 4: print('Parameter mismatch!');exit(1)
    encoded_firmware =  open(argv[2],'rb').read()

    #Check source file CRC
    if libuvk5.CrcXmodem_le(encoded_firmware[:-2]) == encoded_firmware[-2:]:
        print('CRC OK')
    else:
        print('CRC MISMATCH! Packed firmware file required!');exit(1)
    
    decoded_firmware = libuvk5.firmware_xor(encoded_firmware[:-2])
    
    #save decoded firmware to file
    open(argv[3],'wb').write(decoded_firmware[:0x2000]+decoded_firmware[0x2000+16:])
    print(f'Saved decoded firmware to {argv[3]}')

    #display downgrade limiting version level
    version = decoded_firmware[0x2000:0x2000+16]
    print('This firmware has version',version.decode('ascii'))

elif argv[1]=='pack':
    if nargs != 5 or len(argv[3]) > 10: print('Parameter mismatch or version number too long!');exit(1)
    decoded_firmware = open(argv[2],'rb').read()
    version_info = bytes(argv[3], 'ascii')

    # visual indicator for firmware size and big warning if too big
    current_size = len(decoded_firmware)
    max_size = 0xefff

    percentage = (current_size / max_size) * 100
    bar_length = int(percentage / 2)  # Assuming each character represents 2% progress
    size_bar = '[' + '=' * bar_length + ' ' * (50 - bar_length) + ']'

    print(f"\n\nFirmware takes up {current_size}/{max_size} bytes of available space:")
    print(f"Flash usage: {size_bar} {percentage:.2f}%\n\n")
    
    if current_size > max_size:
        print("WARNING WARNING WARNING WARNING WARNING WARNING WARNING WARNING WARNING WARNING WARNING")
        print("WARNING WARNING WARNING WARNING WARNING WARNING WARNING WARNING WARNING WARNING WARNING")
        print("WARNING WARNING WARNING WARNING WARNING WARNING WARNING WARNING WARNING WARNING WARNING")
        print("WARNING WARNING WARNING WARNING WARNING WARNING WARNING WARNING WARNING WARNING WARNING\n")
        print("WARNING: Firmware size exceeds the maximum allowed size of 0xefff (61439) bytes!")
        print("Using an oversize firmware will not work correctly and may lead to freezes, crashes and defects.\n")

    if len(version_info) < 16:
        version_info += b'\x00' * (16 - len(version_info))
    
    firmware_with_version = decoded_firmware[0:0x2000] + version_info + decoded_firmware[0x2000:]
    firmware_with_version_encoded = libuvk5.firmware_xor(firmware_with_version)

    open(argv[4], 'wb').write(firmware_with_version_encoded + libuvk5.CrcXmodem_le(firmware_with_version_encoded))
    print(f'Saved encoded firmware to {argv[4]}')

else:
    print('\nUsage: qsfirm.py unpack <encoded_firmware_in.bin> <decoded_firmware_out.bin>\n\tqsfirm.py pack <decoded_firmware_in.bin> <target_version as X.XX.XX> <encoded_firmware_out.bin>'); exit(1)
