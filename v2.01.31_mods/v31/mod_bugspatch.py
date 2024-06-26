## Various severe bugs patch
## Courtesy of LarSeN

##--------------------- do not modify below this line ---------------------------------------------------
import os,sys,struct

print('* Running',os.path.basename(sys.argv[0]),'mod...')
fw =  bytearray(open(sys.argv[1],'rb').read())

if fw[0xE250:0xE250+7] == b'\x32\x2E\x30\x31\x2E\x33\x31':
    print('Patching miscellaneous bugs...')
    # Plutot que la supprimer, on pad la fin du nom d'un canal modifie avec des [DEL] non affichable
    fw[0x6CEA:0x6CEA+1] = b'\x7F'
    fw[0x6CF8:0x6CF8+20] = b'\x08\x30\x3C\x18\x69\x46\x20\x46\x04\xF0\xCB\xF9\x00\xBF\x00\xBF\x00\xBF\x00\xBF'
    #Bug stupide SURE? demeurant mm apres Exit
    fw[0x3FDE:0x3FDE+1] = b'\x1A'
    fw[0x3FE4:0x3FE4+4] = b'\x46\x1C\x15\x38'
    fw[0x4022:0x4022+1] = b'\x0A'
    fw[0x4032:0x4032+30] = b'\x06\x48\x01\x70\x2F\x70\xF8\xBD\x49\x1E\xC9\xB2\x01\x70\x09\x4A\x0A\x20\x50\x54\xF6\xE7\x96\x03\x00\x20\x43\x04\x00\x20'
    fw[0x492C:0x492C+2] = b'\xB0\x04'                 #change alarm sound to industry std 500-1200 Hz
    fw[0x5AB0:0x5AB0+6] = b'\x37\x20\x00\x01\x01\x21' #change ringtone to ~880Hz
    fw[0x23EE:0x23EE+1] = b'\x1E'            #Maximum menu value for DT Preamble
    fw[0x6688:0x6688+8] = b'\x1B\x29\x02\xD3\x1E\x20\x00\xBF'       #also patch eeprom value check
    #correct preamble routine (TX carrier+wait*10+DT_audio)
    ##fw[0x7AD4:0x7AD4+36] = b'\x05\xD1\x04\x21\x37\x48\x04\xF0\xBD\xFA\x01\x20\x38\x70\xA8\x7B\x03\xF0\x76\xF9\xA8\x88\x1E\x28\x00\xD2\x1E\x20\x0A\x21\x48\x43\x05\xF0\x34\xFB'
    #correct preamble routine v2: we add time to RX longer DTMF string before any action (255ms + TX_carrier + pre_time*10 + DT_audio)
    fw[0x7AD4:0x7AD4+36] = b'\x05\xD1\x04\x21\x37\x48\x04\xF0\xBD\xFA\x01\x20\x38\x70\xFF\x20\x05\xF0\x3C\xFB\xA8\x7B\x03\xF0\x73\xF9\xA8\x88\x0A\x21\x48\x43\x05\xF0\x34\xFB'
    fw[0x807A:0x807A+1] = b'\x00'             #QS Bug fix: Prevent DDD*##### to be killed without KillCode knowledge
    fw[0x809E:0x809E+1] = b'\x00'
    #Removes Quansheng's backdoor password. Instead, use pure CPU UUID. Get your unique CpuID by dumping a Hello packet or reading memory @0x40000080 (4 words)
    fw[0x7480:0x7480+1] = b'\xA9'
    fw[0xCC0:0xCC0+30] = b'\x10\xD1\x22\x46\x15\x49\x16\x48\x00\xF0\x86\xFC\x06\x00\x0A\xF0\x7F\xF9\x12\x49\x22\x46\x00\xF0\x7F\xFC\x30\x40\x02\xD0'
    fw[0xAFD0:0xAFD0+28] = b'\x00\xBF\x05\x48\x05\x4A\x11\x68\x01\x60\x51\x68\x41\x60\x91\x68\x81\x60\xD1\x68\xC1\x60\x70\x47\x54\x08\x00\x20'
    #Implement the 2 official 2.01.32 QS fixes
    fw[0x54A4:0x54A4+6] = b'\x20\x49\x19\x20\x40\x01'
    fw[0xC49A:0xC49A+32] = b'\x7C\x49\x08\x78\x00\x28\x0F\xD1\x84\x39\x08\x88\x00\x28\x0B\xD1\x00\xBF\x00\xBF\x78\x49\x08\x88\x00\x28\x05\xDD\x40\x1E\x08\x80'
    fw[0xC502:0xC502+24] = b'\x62\x49\x08\x78\x02\x28\x17\xD0\x01\x28\x15\xD0\x04\x28\x13\xD0\x84\x39\x08\x88\x00\x28\x0F\xD1'
    fw[0xC56A:0xC56A+32] = b'\x48\x49\x08\x78\x04\x28\x0F\xD0\x84\x39\x08\x88\x00\x28\x0B\xD1\x00\xBF\x00\xBF\x4E\x49\x08\x88\x00\x28\x05\xDD\x40\x1E\x08\x80'

else:
    print('ERROR: Pattern not found!');sys.exit(1)

open(sys.argv[1],'wb').write(fw)
