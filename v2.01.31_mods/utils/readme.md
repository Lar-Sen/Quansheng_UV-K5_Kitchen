## Various utility scripts useful when modding / reversing firmware. 
All scripts uses my library `libuvk5.py`. Scripts tested only on windows.

To read write access COM Port (Serial/USB Cable) must be the Serial Module installed into Python.

Install from command prompt/cmd the serial module for Python: 
```
pip install pyserial
```
Do not confuse with `serial` module which is incompatible with this lib.
<hr>


### `flashtool.py`
Arguments:
```
flashtool.py  <COMx> <unscrambled_rom.bin> [block number] [blocks to write]
```
Description:<br>
This is a (cleartext) firmware flasher.

Its advantages over stock app is that it can flash specific blocks without having to reflash the entire ROM. Time and flash component lifespan savings.

Sadly, Quansheng decided to only allow full flash update by erasing all 120 ROM sectors as soon as the operation begins.

A bootloader mods allow for progressive erasing, thus permitting partial flashing. Look here for more information:

https://github.com/Lar-Sen/Quansheng_UV-K5_Kitchen/tree/main/Bootloader_mods

Anyway flashtool.py will work like stock without bootloader mod.

You need to provide an _unscrambled_ firmware file.

For example, if you wanna flash a modded firmware file in your mods temp directory:
```
> flashtool.py COM4 fw.dec.bin

HELO UV-K5 2.03.02

About to FLASH 59392 bytes to user ROM!
Sure?
 Confirm [Y/n]
```

The update progress will take place after confirmation.

Another example (if you previously applied mod over your bootloader): Let's update what you modded in your firmware file at offset 0xD358.

To get the right block to update, let's divide 0xD358 / 256 = 0xD3 , decimal 211. So:

```
> flashtool.py COM4 fw.dec.bin 211 1
```
will automatically update only 256 bytes starting at the lower rounded sector (offset 0xD200 in that case) and rewrite next block, as erase size is 512 bytes.

Note: Updating firmware with flashtool.py is slightly slower that the stock application, due to additional UART traffic checks and progressive erasing of blocks (in case you modded the bootloader).
<hr>




### `cmd052D_authenticate.py`
Arguments:
```
cmd052D_authenticate.py  <COMx> [unlock] | [protect] <password>
```
Description:<br>
This script requires `pycrypto` or similar to be installed. This utility initiates AES authentication, in order to gain R/W config access to a transceiver with an active password (not the Power-on one).

It is useful to recover a locked-out situation, which sometimes happen because of EEPROM misuse. Also permits custom key updating.

For example, if you only need to remove password, please set `customKey = masterKey` within the script and run `cmd052D_authenticate.py <COMx> unlock`
```
> cmd052D_authenticate.py COM4 unlock

AES Challenge : (776607318, 96531953, 662584761, 512222488)

OK, access granted!

User password now reset to (NULL)
```

You can set your own key if you want, by running `cmd052D_authenticate.py <COMx> protect <your_key>` and editing `customKey` within the script.
```
> cmd052D_authenticate.py COM4 protect UVK5isFun

AES Challenge : (640825850, 55319237, 1357743101, 1189709836

OK, access granted!

About to LOCK serial access to config!
Sure to set: UVK5isFun as password to protect the device memory?
 Confirm [Y/n]Y
```

Note: You can check the status of your device by invoking `fwversion_read.py`. It will now tell you all the missing bits.
```
2.01.31 Firmware
PIN ok?  True
Config password protected?  True
AES Challenge : (506113336, 723914795, 1684280427, 1400539874)
```
<hr>




### `cmd05DB_ramreader.py`
Arguments:
```
cmd05DB_ramreader.py <COMx> <RAM address> <length> [output_file]
```
Description:<br>
This script requires `mod-combo_ramreader_zvei` to be applied. This mod replaces a useless routine which is responsible for reply to command `0x051F` sent by uart. New `0x05DB` UART command can be used to read any memory area.

For example, you may want to capture the entire screen framebuffer:
```
> cmd05DB_ramreader.py COM4 0x20000684 0x400 screen_buffer.bin
```

Note: Please refresh the transceiver screen before launch, as the buffer is internally actively used.

Then you can use provided `bin2array.py` to convert RAW bytes in screen_buffer.bin to a bytearray in text-format, which in turn you can preview/save as bitmap using `fonts_and_graphics/Img2Cpp.htm`

Note: If you omit a filename and redirect output to a text file, you can get a text-formatted bytearray which is ready to use with img2Cpp.htm ;)
```
> cmd05DB_ramreader.py COM4 0x20000684 0x400 > screencap_array.txt
```

The last parameter is optional, if omitted you'll get raw hex data of selected memory area. Useful for reading variables. Example displaying current microphone gain value:
```
> cmd05DB_ramreader.py COM4 0x20000ad6 0x1
[0x18]
```
<hr>



### `cmd060x_bkreg.py`
Arguments:
```
cmd060x_bkreg.py <COMx> <read | write  regNum hexdata>
```
Description:<br>
This script requires `mod_uart_cmds.py` to be applied. It creates 2 news UART commands to 'live' read or write any BK4819 register. Useful for debugging and researching hidden functions of the chip.

I borrowed some inspiration from @FAGCI here.

Note: `mod_uart_cmds` also makes more room to use ZVEI-style tone sequences, up to 128 bytes.

For example, if you want to check currently set TONE1 frequency:
```
> cmd060x_bkreg.py COM4 read 113

regNum: 113 [ 0x71 ]
Actual =  0x8517
decodes as 1000010100010111
ReplyCode: 0
```
0x8517 is 34071. Conversion needs dividing it by 10.32444, so for now TONE1 is set to 3300 Hz.

Remember to always specify register number as INTEGER, and register value as 16 BIT HEX.

Another example, let's update sync bytes 0 and 1 for FSK modem:
```
> cmd060x_bkreg.py COM4 write 90 8585

Reg [ 0x5a ] was =  0x709

Set to =  1000010110000101

regNum: 90 [ 0x5a ]
Now reads =  0x8585
ReplyCode: 64
```

<hr>



### `bin2array.py`
Usage sample:
```
bin2array.py image_logo.bin logo_bytearray.txt
```
Sample output:
```
Binary successfully converted to logo_bytearray.txt
```
Description:<br>
Useful script to convert RAW image data (logos, fonts, icons..) to a text-formatted bytearray for use in mods.

Please note you can use Img2Cpp `fonts_and_graphics\image2cpp.htm` to convert standard image files to ready-to-use bytearray strings and vice-versa.
<hr>



### `fw_unpack.py`
Usage sample:
```
fw_unpack.py k5_v2.01.19_publish.bin
```
Sample output:
```
CRC OK
Saved decoded firmware to k5_v2.01.19_publish.dec.bin
Saved version info to k5_v2.01.19_publish.ver.bin
```
Description:<br>
Scripts checks file's CRC then decode it and creates two new files with suffix `.dec.bin` and `.ver.bin`. If you just want to revere engineer file then only first file is needed. Second one is used by next script `fw_pack.py` to put together file ready to upload to device.
<hr>



### `fw_pack.py`
Usage sample:
```
fw_pack.py k5_v2.01.19_publish.dec.bin k5_v2.01.19_publish.ver.bin k5_v2.01.19_reassembled.bin
```
Sample output:
```
Saved encoded firmware to k5_v2.01.19_reassembled.bin
```
Description:<br>
It creates encoded file with correct CRC and version bytes inserted in file. Ready for use with orginal updater. 
<hr>


### `configmem_read.py`
Arguments:
```
configmem_read.py <COMx> <address> <len>
```
Usage sample:
```
configmem_read.py COM4 0x0F40 8
```
Sample output:
```
00010001010101ff
```
Description:<br>
Script reads contents of configuration memory directly to console. 
<hr>




### `configmem_write.py`
Arguments:
```
configmem_write.py <COMx> <address> <hex_payload>
```
Usage sample:
```
configmem_write.py COM4 0x0F40 00010001010101ff
```
Sample output:
```
PAYLOAD= 00010001010101ff
```
Description:<br>
Script writes bytes given in payload directly to device. **Payload has to be multiply of 8 bytes**
<hr>



### `reboot_radio.py`
Arguments:
```
reboot_radio.py <COMx>
```
Usage sample:
```
reboot_radio.py COM4
```
Description:<br>
Script just reboots device. Command not produce any output in normal situation. Usefull for example after using `configmem_write.py`
<hr>



### `batt_calibrator.py`
Arguments:
```
batt_calibrator.py <COMx> <read | write  val0 val1 val2 val3 val4 val5 | calibrate>
```

To calibrate ADC so battery voltage display more accurately invoke `batt_calibrator.py COM1 calibrate` like below:
```
> batt_calibrator.py COM1 calibrate
Enter voltage from multimeter and press enter:
```
now follow steps: 
- connect radio to PC
- power on radio
- lay your radio with display to the bottom and battery up
- measure voltage on two exposed pad on bottom of the battery
- wait till voltage stabilizes
- write measuder voltage in format `1.23` or `1,23` it shoudl not matter
- hit enter
- reboot radio

You can backup current calibration values by starting `batt_calibrator.py COM1 read`



### `mic_calibrator.py`
Arguments:
```
mic_calibrator.py <COMx> <read | write  lev0 lev1 lev2 lev3 lev4>
```

Description:<br>
Allows to update the 5 Mic gain levels from menu by altering each of their corresponding factors in EEPROM. Max factor value is 31. Provides precise control over Mic sensitivity.

Usage sample:
```
> mic_calibrator.py COM4 read
Level 0: 8 /31 (Lowest)
Level 1: 10 /31 (Lower)
Level 2: 16 /31 (Mid)
Level 3: 24 /31 (Higher)
Level 4: 30 /31 (Highest)
```

If you want to alter these values, you have to use `write` command:
```
> mic_calibrator.py COM4 write 8 10 16 24 31
OK. New values written to eeprom
 ....
PLEASE REBOOT RADIO FOR THE CHANGES TO TAKE EFFECT !!!
```


Then reboot radio.
<hr>

	LarSeN.
