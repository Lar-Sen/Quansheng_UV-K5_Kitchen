##Change threshold frequencies used to control RF filter path transition and set final RF stage driver gains.
#"In my unit, changing the RF switch frequency to 250 MHz produces a dramatic improvement in sensitivity and power, in the 250-280 MHz band."
#Factory PA gains are VHF{gain1=1 , gain2=0} and UHF{gain1=4 , gain2=2}

#Factory setting
#rf_path_threshold = 280_000_000
#power_amplifier_gain_threshold = 280_000_000

#Custom values (in Hz)
rf_path_threshold = 265_000_000
power_amplifier_gain_threshold = 280_000_000

##--------------------- do not modify below this line ---------------------------------------------------
import os,sys,struct
print('* Running',os.path.basename(sys.argv[0]),'mod...')
fw =  bytearray(open(sys.argv[1],'rb').read())

print('Old RF path threshold frequency:  {:>13_} Hz'.format(struct.unpack_from('<I', fw, offset=0x1EA8)[0]*10))
print('Old Power Amplifier gain threshold frequency: {:>13_} Hz'.format(struct.unpack_from('<I', fw, offset=0xAB6C)[0]*10))

fw[0x1EA8:0x1EA8+4] = struct.pack('<I',rf_path_threshold//10) 
fw[0xAB6C:0xAB6C+4] = struct.pack('<I',power_amplifier_gain_threshold//10)

print('New RF path threshold frequency:  {:>13_} Hz'.format(struct.unpack_from('<I', fw, offset=0x1EA8)[0]*10))
print('New Power Amplifier gain threshold frequency: {:>13_} Hz'.format(struct.unpack_from('<I', fw, offset=0xAB6C)[0]*10))

open(sys.argv[1],'wb').write(fw)
