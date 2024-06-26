## My own set of 2.01.31 firmware mods for Quansheng UV-K5 VHF/UHF Handheld

### Prerequisites 
 - Windows, XP at least
 - Python 3.6.8 (at least) installed
 - Kenwood type serial comms cable (USB or RS-232)

### How to use this?
 - customize included mods, for example `mod_custom_freq_ranges.py` has possibility to edit frequency ranges
 - edit `build31.bat`, if you want omit execution of any mod, prefix its line with `::` or `rem`
 - start a shell in `firmware_mods` directory
 - run command `build31.bat`
 - look for any errors. Don't go further if any: double-check editable values in each of active mods
 - now you can flash new firmware file named `k5_v2.01.31_MODDED.bin`, with genuine `Updater.exe` from Quansheng (latest version provided in /Updater directory)

## ROM patches list
<hr>

### `mod_uart_cmds.py`

This mod replaces factory unneeded UART command 0521 by 2 new commands, 0601 (read) and 0603 (write) to read/write arbitrary values to BK4819 radio chip registers.

It works in tandem with `cmd060x_bkreg.py` script in /utils directory.

Please read /utils/readme for more information.

By the way, applying this mod frees some more bytes to compose your own tone sequence when using `mod-combo_ramreader_zvei.py` mod below.
<hr>


### `mod-combo_ramreader_zvei.py`

This is a combo mod, as 1st mod makes room for the 2nd.

1. Original RAM reader, ported to v2.00.31 firmware. Creates new 05DB UART command. Please refer to utils/readme for usage details.

2. ZVEI signalling function, to replace 2nd method for 1750Hz burst tone (long press F1 side key)

My contribution: This is a replacement function for 'Press-long F1', patched to TX a ZVEI-style burst of tones.

It is not 5-tone length limiting: you are free to set any sequence up to 32 tones. Tone 0 is blank pause. Melody artists welcome!

Customization:
```python
repeat = <number of times to repeat sequence>
tonedur = <time in ms to play each tone>
tonedelay = <time in ms for silence between tones>
seqdelay = <time in ms before looping to next sequence>
pattern = <custom tone pattern in byte array format>
```

The tone pattern is a sequence of 10*kHz, minus 68.
Example: Byte 0x30 is 48. 48+68=116. This is 1160Hz tone.
Default is ZVEI-2 Emergency sequence for Channel E in European alps: Swiss - Italy - France. Useful for hiking and rescue activities.

All three 'repeat' , 'tonedur' , 'tonedelay' values can take 255 max.

'seqdelay' takes only any of: 512, 256, 0. Zero is 128ms.
To get NO delay, please un/comment seqdelay related lines in the 'do not modify' section.
<hr>

### `mod_2to1_compressor.py`
My contribution: Activates only compressor part of the integrated compander, to get better modulation dynamics.

Auto-disables when VOX set, to preserve accuracy in digital modes.
<hr>

### `mod_battery_icon.py`
Sets a better look for battery icon.

Tip: Best to check my `mod_custom_symbols.py` which entirely replaces all icons by better alternatives. Or you can run this after my mod if you hate hearts :)
<hr>

### `mod_bugspatch.py`
My contribution: Various ROM patches for Quansheng genuine firmware bugs. Evolutive.
<hr>

### `mod_change_contrast.py`
Allows to change LCD appearance, e.g black pixels get more black.

Customization:  A good value is 35. Beware not to put too high value, as this is suspected to shorten LCD lifespan.

### `mod_change_burst_tones`
My contribution: Now allows to change PTT+F2 and 'long-press F1' burst tones. Defaults are 1750Hz and 1050Hz.

Replaces mod_change_Tone_1750Hz.py.
<hr>

### `mod_change_freq_scan_timeout.py`
My contribution: Remove infinite time (useless). Instead, restore activity graph which was stuck in previous version.

After applying this mod, the FREQ CLONE and CTC/DCS SCAN function ([F]+4, [F]+Scan) will run till given timeout or if user press [Exit] button.
<hr>

### `mod_change_RF_switch_threshold.py`
Allows to change the threshold frequencies for VHF/UHF switch of the RF path and output amplifier bias.

Factory setting is 280 MHz for both of them.

Better power and/or sensitivity may be observed in some cases.
<hr>

### `mod_change_tx_limits.py`
Self explanatory. Please be aware that TXing below ~80MHz is known to produce a considerable amount of spurious emissions with this unit.

Smarter use is the wiser mod_enable_tx_50to850_except_limits.py .
<hr>

### `mod_enable_tx_50to850_except_limits.py`
Creates a band block for TX frequencies: an interval where you're not allowed to xmit, even if frequency domain is unlocked.

Please be aware that TXing below ~80MHz is known to produce a considerable amount of spurious emissions with this unit.

Customization: Blocks AIR band by default. You can change it at the beginning of the script.
<hr>

ℹ️This patch alone doesn't extend available frequency ranges. For this use `mod_custom_freq_ranges.py` mod.
<hr>

### `mod_custom_bootscreen_narrow.py`
My contribution: Completely reworked the display routine. Now better nested and switchable from main menu (edit line FULL to Logo).

Adds a customisable boot screen, sparing ROM bytes by allowing an offset from top of the screen.

Customization: before drawing logo, screen buffer is filled with value defined in `clean_pattern` variable. Have a look at utils/fonts_and_graphics/Clearing_patterns.bmp

To make your own logo, get a 128x64 (max) BMP or PNG file, then convert it using utils/fonts_and_graphics/img2cpp.htm

Import file, change for "Vertical drawing" at the end of the page, then click generate. The code you get have to be pasted into the python script. Look at "MARIO", it's self explanatory.
<hr>

### `mod_custom_ctcss_codes.py`
My contribution: Genuine CTCSS embedded code list is badly numbered. I restored CTCSS base code list+extended codes to the end.

Please keep in mind that Quansheng codeplug software won't be aware of the new ordered list: Just check your channels after programming.
<hr>

### `mod_custom_digits.py`
My contribution: Grouped some of the best fonts for Big and Small digits display (BBC mode 7, Geneva, Terminus, Videotex, old computer, etc)

Change fonts used to display big and small digits.
<hr>

### `mod_custom_font.py`
My contribution: Integrated some good fonts (Apple Chicago, CP/M..)

Customization:
You can generate your own fonts using utils/fonts_and_graphics/img2cpp.htm . You just have to insert generated string to the beginning of the python script, at font = b'\STRINGSTRINGSTRING'
<hr>

### `mod_custom_freq_ranges.py`
The purpose of  this mod is to unlock receiving range of the transceiver. Default is 25-630MHz.
<hr>

### `mod_custom_mdc_data.py`
My contribution: Aims to produce a better MDC signalling when MDC1200 roger beep is chosen. String is an EOT for PTT-ID 0001.

Not really working. No differential coding, just plain AFSK.

Due to Beken chip limitations, bit coding doesn't conform to MDC spec, so as frame format.

More investigation about register values is needed to get a hint about proper MDC1200 support, claimed by Beken themselves.

Fee free to check more advanced MDC1200 work done by @OneOfEleven on custom firmware.
<hr>

### `mod_custom_noaa_freqs.py`
My contribution: default is now first 1-7 GMRS channels and 22-20 GMRS call/repeater channels. This is because of forced 12.5kHz deviation.

Also check mod_disable_1050hz_noaa, to use these without 1050Hz toneburst.

Customization: Just sets new values for frequencies in NOAA scan list, nothing less, nothing more. 
<hr>

### `mod_disable_1050hz_noaa.py`
My contribution: Permits normal listening and background scan detection of said "NOAA" channels, without needing for 1050Hz toneburst.
<hr>

### `mod_custom_symbols.py`
My contribution: Integrated BMP converter, and better symbols (I hope!)

Customization: Just edit provided Symbols_mod.bmp. Keep in mind that you must keep orientation and file format as 2 color BMP.

Replaces all symbols on screen with a rotated +90 degree, 1bit BMP
<hr>

### `mod_disable_tx_completely.py`
No customization. 

On ALL frequencies radio shows "DISABLED" info and don't transmit at any band.

ℹ️ Please do not use this mod together with `mod_enable_tx_50to850.py`
<hr>

### `mod_enable_am_everywhere.py`
No customization. 

On ALL frequencies, AM mode will be switchable.
<hr>

### `mod_enable_swd_port.py`
If you are experimenting deep modifications, need active debugging or playing with EEPROM, this could be useful, even for brick recovery.

Not harmful to enable.
<hr>

### `mod_fm_radio_64-108mhz.py`
My contribution: Now a working 64 to 108MHz, and function keys remapping (F+VFO: memory recall, F+FM:scan, F+FC:auto-MR)

Extends WFM receive range from 64MHz to 108MHz.
<hr>

### `mod_increase_backlight_timeout`
My contribution: Fixed old derpy way to increase backlight expiry time. Now factor is a multiplier*500ms. New: Backlight forever if set to 5.
<hr>

### `mod_menu_strings.py`
My contribution: Edited most of the menu text, messages, and option text to get a better conformity to standards. A must have.
<hr>

### `mod_mic_gain.py`
My contribution: Mod is next to useless now. Please check my "utils/mic_calibrator.py". Good values have to be set in EEPROM.
<hr>

### `mod_negative_screen.py`
No customization.
<hr>

Edits initialization routine of ST7565 (LCD controller) to change default LCD mode normal to negative.
<hr>

Here you can change low and high limit for each frequency band. 

The underscore `_` symbol is omitted by python interpreter and is added only for better readability.

So for example, if you want to fill the gap between 76 and 108Mhz then in second array change first limit from `76_000_000` to `107_999_990` or 
if you want to extend above 600MHz then change last limit from `600_000_000` to `1300_000_000`. Please keep in mind that different ranges 
are demodulated slightly different inside BK4819 chip, and some ranges have enabled AM demodulation while other don't. 
<hr>

### `mod_custom_steps.py`
Customization:
```python
# change below sets to new ones, values are in Hz
new_freq_steps = [2500, 5000, 6250, 10000, 12500, 25000, 8330]
```
Changes array of frequency steps in menu at position 2
<hr>

### `mod_enable_tx_50to850.py`
No customization. You can just disable or enable it in `build.bat`. The purpose of this mod is to **globally disable/bypass** TX lock. 

ℹ️ This patch alone doesn't extend available frequency ranges. For this use `mod_custom_freq_ranges.py` mod.
<hr>

ℹ️ This patch doesn't extend available mic gain steps (they will still be 0-4.) It just increases the _starting point_ on the mic gain
scale sent to the BK4819 mic sensitivity register.
<hr>

### `mod_negative_screen.py`
No customization. You can just disable or enable it in `build.bat`.

Edits initialization routine of ST7565 (LCD controller) to change default LCD mode normal to negative.
<hr>

### `mod_ota_qrg.py`
Customization:
```python
AIR_COPY_FREQ_HZ = 433_600_000
```

Default value for copying setting over the air aka "AIR COPY" is 410.025 MHz. You can change that default value using this mod.
<hr>

### `mod_roger_beep.py`
My contribution: Now with single, dual, or triple beep!  Completely rewrote roger routine.

Changes "Roger" beep tone number and frequency(ies).

Customization: You can change duration and/or frequency for each tone used. Put 0 in correct duration if single ou dual beep is preferred.
<hr>

### `mod_rssi_bars_SOS_alert.py`

My contribution: Change RSSI meter behaviour, using 7 possible step bars. Evaluating RSSI is done via maths linear approach. Adds Morse code flashes as an added bonus.

Rewrote some routines here, and created new function to blink flashlight (call, alarm)

New! Now Alarm (panic button) will trigger a custom Morse code you can change if you want. Default is classic SOS pattern ... --- ...

A different Morse pattern can also be chosen for classic blinking of flashlight (or SelCall ringing)

Customization:
```python
panic_pat = <alarm_custom_binary_pattern>
blink_pat = <blinking_custom_binary_pattern>
```
VHF: @14B2 origin offset, @14B4 slope, @14B6 s=0 limit. UHF: @14CE origin offset, @14D0 slope, @14D2 s=0 limit. Needs easier method to customize, anyway.

NEED to change Symbols font: 7 bars+eliminate antenna icon. If you disable this mod, please replace Symbols_mod.bmp in v31 directory by Symbols_mod_(without_rssi_patch).bmp .

Upgrades genuine RSSI meter. Also makes use of freed ROM space to put new routines which make flashlight follow a defined Morse pattern when called via DTMF SelCall, and when Alarm is triggered.
<hr>

### `mod_widen_scr_range`
My contribution:
Changes the scrambler inversion frequency range. Step mod from 100Hz to more conventional 115.5Hz, in order to reach theorical scrambling maximum at 3730Hz (~step/2)
<hr>

	LarSeN.

