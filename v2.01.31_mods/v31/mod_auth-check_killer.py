##Authenticity check killer
##Removes Quansheng's routines to block counterfeiting
#It involves CPU UUID and an unknown CPU feature related to factory signature hosting at an secret location (UART CMD 0516). Maybe OTP.
#When triggered, transceiver doesn't boot genuine firmware anymore, but still accepts UART commands

##--------------------- do not modify below this line ---------------------------------------------------
import os,sys,struct

print('* Running',os.path.basename(sys.argv[0]),'mod...')
fw =  bytearray(open(sys.argv[1],'rb').read())
nop = b'\x00\xBF'

if fw[0x1710:0x1710+8] == b'\xF0\xB5\x43\x4D\x8B\xB0\x28\x46':
    print('Killing QS anti-counterfeiting measures...')
    fw[0x505C:0x505C+1] = b'\x15'
    fw[0x5088:0x5088+54] = b'\x0A\xE0\x02\xF0\x83\xFF\x01\x20\x30\x70\x2C\x49\x0A\x20\x08\x80\x05\xE0\x00\xBF\x00\xBF\x00\xBF\x0C\x48\x04\x70\x24\x48\x04\x70\xF8\xBD\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'
    fw[0x514C:0x514C+8] = b'\x00'*8
    fw[0xD1DE:0xD1DE+4] = 2*nop
    fw[0x49C0:0x49C0+2] = nop
    fw[0x49CC:0x49CC+2] = nop
    fw[0x49D0:0x49D0+4] = 2*nop
    fw[0x4D04:0x4D04+4] = b'\x00'*4
    fw[0x497A:0x497A+14] = 7*nop
    fw[0x4CE8:0x4CE8+4] = b'\x00'*4
    fw[0x9DF2:0x9DF2+58] = b'\xF6\xF7\x71\xFE\x00\xBF\x01\x20\x40\x02\xF6\xF7\x2E\xFE\x00\x28\xF9\xD0\x10\x20\xF6\xF7\x41\xFE\x20\x80\x01\x20\x40\x02\xF6\xF7\x3C\xFE\x28\x80\x00\xBF\x70\xBD\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'
    fw[0x1710:0x1710+284] = b'\x00'*284   #Freed bytes to 00
    fw[0x7E4:0x7E4+12] = b'\x00'*12   #Freed bytes to 00
else:
    print('ERROR: Cant find function');sys.exit(1)

open(sys.argv[1],'wb').write(fw)
