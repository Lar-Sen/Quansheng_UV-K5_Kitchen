#!/usr/bin/env python3
import libuvk5
import struct
from sys import argv,exit
from os import path

if len(argv)<3: print(f'Usage: {path.basename(argv[0])} <COMx> <read | write  val0 val1 val2 val3 val4 val5 | calibrate>') ; exit(1)
arg_port = argv[1]
action   = argv[2]

with libuvk5.uvk5(arg_port) as radio:
    radio.debug=False
    if radio.connect():
        if radio.get_fw_version()["prot"] == 1:
            print('\nWARN: Config is password protected. Make sure you logged in first.')
        calib_raw = radio.get_cfg_mem(0x1F40,16)
        calib_data     = list(struct.unpack('<8H',calib_raw))
        calib_data_old = [i for i in calib_data]
        if action == 'read':
            def calculate_voltage(value, denominator):
                if denominator != 0:
                    return 760 * value / denominator / 100
                else:
                    return 0  # Handle the division by zero case
            print('Level {}: [{:>4}] {:.2f} V {}'.format(0, calib_data[0], calculate_voltage(calib_data[0], calib_data[3]), '// Empty battery blinking'))
            print('Level {}: [{:>4}] {:.2f} V {}'.format(1, calib_data[1], calculate_voltage(calib_data[1], calib_data[3]), '// 1 battery bar if above this value'))
            print('Level {}: [{:>4}] {:.2f} V {}'.format(2, calib_data[2], calculate_voltage(calib_data[2], calib_data[3]), '// 2 battery bars if above this value'))
            print('Level {}: [{:>4}] {:.2f} V {}'.format(3, calib_data[3], calculate_voltage(calib_data[3], calib_data[3]), '// 3 battery bars if above this value, also value used to calculate adc to volt'))
            print('Level {}: [{:>4}] {:.2f} V {}'.format(4, calib_data[4], calculate_voltage(calib_data[4], calib_data[3]), '// 4 battery bars if above this value'))
            print('Level {}: [{:>4}] {:.2f} V {}'.format(5, calib_data[5], calculate_voltage(calib_data[5], calib_data[3]), '// overwritten by radio to 2300 anyway'))
            print('\nActual = {:.2f} V'.format(calculate_voltage(radio.get_adc()["volt"], calib_data[3])))

        if action=='write': 
            if len(argv)!=9: print(f'Usage: {path.basename(argv[0])} <COMx> write val0 val1 val2 val3 val4 val5') ; exit(1)
            calib_data[0] = int(argv[3],0)
            calib_data[1] = int(argv[4],0)
            calib_data[2] = int(argv[5],0)
            calib_data[3] = int(argv[6],0)
            calib_data[4] = int(argv[7],0)
            calib_data[5] = int(argv[8],0)
            calib_raw = struct.pack('<8H',*calib_data)
            radio.set_cfg_mem(0x1F40,calib_raw)

        if action=='calibrate':
            while True:
                actual_voltage = input("Enter voltage from multimeter and press enter: ")
                try:
                    actual_voltage = float(actual_voltage.replace(',','.'))
                except:
                    actual_voltage = None
                    
                if actual_voltage is not None:
                    break
            adc_value = radio.get_adc()["volt"]
            new_coeff = int(760*adc_value/actual_voltage/100)
            print('Current battery voltage         = {:.2f}'.format(760*adc_value/calib_data[3]/100))
            print('Current battery ADC coefficient = {}'.format(calib_data[3]))
            print('')
            print('Desired battery voltage         = {:.2f}'.format(actual_voltage))
            print('New battery ADC coefficient     = {}'.format(new_coeff))
            print('Wait... ', end='')
            calib_data[3] = new_coeff
            calib_raw = struct.pack('<8H',*calib_data)
            radio.set_cfg_mem(0x1F40,calib_raw)
            print('OK. New value written to eeprom')
            print('Previous calibration values:',calib_data_old[0:6])            
            print('Current calibration values :',struct.unpack('<8H',radio.get_cfg_mem(0x1F40,16))[0:6])
            print('')
            print('!!! PLEASE REBOOT RADIO FOR THE CHANGES TO TAKE EFFECT !!!')