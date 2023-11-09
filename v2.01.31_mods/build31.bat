@echo off
@mkdir temp 2>NUL
@del /F temp\fw.dec.bin temp\fw.ver.bin 2>NUL

@echo Extracting firmare...
c:\python\python.exe qsfirm.py unpack k5_v2.01.31_publish.bin temp\fw.dec.bin

:: mods implying firmware grow
:: please choose only one of them and always 
:: place as first mod in this batch file
c:\python\python.exe v31\mod_custom_bootscreen_narrow.py temp\fw.dec.bin
REM c:\python\python.exe v31\mod_more_freq_steps_and_backlight_duration.py temp\fw.dec.bin

:: start of mods
c:\python\python.exe v31\mod-combo_ramreader_zvei.py temp\fw.dec.bin
c:\python\python.exe v31\mod_2to1_compressor.py temp\fw.dec.bin
REM c:\python\python.exe v31\mod_battery_icon.py temp\fw.dec.bin
c:\python\python.exe v31\mod_change_burst_tones.py temp\fw.dec.bin
c:\python\python.exe v31\mod_change_contrast.py temp\fw.dec.bin
c:\python\python.exe v31\mod_change_freq_scan_timeout.py temp\fw.dec.bin
c:\python\python.exe v31\mod_change_RF_switch_threshold.py temp\fw.dec.bin
c:\python\python.exe v31\mod_change_tx_limits.py temp\fw.dec.bin
c:\python\python.exe v31\mod_custom_ctcss_codes.py temp\fw.dec.bin

c:\python\python.exe v31\mod_custom_digits.py temp\fw.dec.bin
c:\python\python.exe v31\mod_custom_font.py temp\fw.dec.bin
c:\python\python.exe v31\mod_custom_mdc_data.py temp\fw.dec.bin
c:\python\python.exe v31\Symbols_encode31.py v31\Symbols_mod.bmp v31\mod_custom_symbols.py
c:\python\python.exe v31\mod_custom_symbols.py temp\fw.dec.bin

c:\python\python.exe v31\mod_custom_freq_ranges.py temp\fw.dec.bin
c:\python\python.exe v31\mod_custom_noaa_freqs.py temp\fw.dec.bin
c:\python\python.exe v31\mod_custom_steps.py temp\fw.dec.bin
c:\python\python.exe v31\mod_disable_1050hz_noaa.py temp\fw.dec.bin
REM c:\python\python.exe v31\mod_disable_tx_completely.py temp\fw.dec.bin
c:\python\python.exe v31\mod_enable_am_everywhere.py temp\fw.dec.bin
c:\python\python.exe v31\mod_enable_swd_port.py temp\fw.dec.bin
REM c:\python\python.exe v31\mod_enable_tx_50to850.py temp\fw.dec.bin
c:\python\python.exe v31\mod_enable_tx_50to850_except_limits.py temp\fw.dec.bin
c:\python\python.exe v31\mod_fm_radio_64-108mhz.py temp\fw.dec.bin
c:\python\python.exe v31\mod_increase_backlight_timeout.py temp\fw.dec.bin
REM c:\python\python.exe v31\mod_instant_on.py temp\fw.dec.bin
c:\python\python.exe v31\mod_menu_strings.py temp\fw.dec.bin
c:\python\python.exe v31\mod_mic_gain.py temp\fw.dec.bin
REM c:\python\python.exe v31\mod_negative_screen.py temp\fw.dec.bin
c:\python\python.exe v31\mod_ota_qrg.py temp\fw.dec.bin
c:\python\python.exe v31\mod_roger_beep.py temp\fw.dec.bin
c:\python\python.exe v31\mod_rssibars_SOS_alert.py temp\fw.dec.bin
c:\python\python.exe v31\mod_widen_scr_range.py temp\fw.dec.bin
c:\python\python.exe v31\mod_bugspatch.py temp\fw.dec.bin
:: end of mods

@echo Adding v2 header and ciphering...
c:\python\python.exe qsfirm.py pack temp\fw.dec.bin 2.00.00 k5_v2.01.31_MODDED.bin

