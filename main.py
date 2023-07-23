'''
    requires:
    ddcutil
'''

import os
import sys
import subprocess
import build.gui
import threading
import argparse

# argparses -gui
parser = argparse.ArgumentParser()
parser.add_argument('-gui', action='store_true')
parser.add_argument('-cmd', nargs=2, type=str, metavar=('+or-', 'value(usually 10)'), help="example: -cmd + 10")
args = parser.parse_args()

def check_ddcutil():
    try:
        subprocess.check_output(['ddcutil', '-h'])
        return True
    except FileNotFoundError:
        os.system("sudo apt-get -y install ddcutil")
        return False

check_ddcutil()

def get_busses():
    busses = subprocess.check_output(['ddcutil', 'detect']).decode('utf-8').split('\n')
    busses = [bus.split(' ')[-1] for bus in busses if bus.startswith('   I2C bus:  /dev/i2c-')]
    busses = [bus.split('-')[-1] for bus in busses]
    return busses

def execute_brightness(bus: str = 'all'):
    text = build.gui.entry_1.get()
    if text.count('+'):
        _tmp = text.split('+')
        text = ["", ""]
        text[0] = "+"
        text[1] = _tmp[1]
    elif text.count('-'):
        _tmp = text.split('-')
        text = ["",""]
        text[0] = "-"
        text[1] = _tmp[1]

    print(text)
    if bus == 'all' and not args.cmd:
        busses = get_busses()
        for bus in busses:
            # os.system(f"ddcutil setvcp 10 {text[0]} {text[1]} -b {bus}")
            threading.Thread(target=os.system, args=(f"ddcutil setvcp 10 {text[0]} {text[1]} -b {bus}",)).start()

    if bus == 'all' and args.cmd:
        for bus in get_busses():
            # os.system(f"ddcutil setvcp 10 {args.cmd[0]} {args.cmd[1]} -b {bus}")
            threading.Thread(target=os.system, args=(f"ddcutil setvcp 10 {args.cmd[0]} {args.cmd[1]} -b {bus}",)).start()

if args.gui:
    build.gui.button_1['command'] = lambda: execute_brightness()
    build.gui.main() # type: ignore

if args.cmd:   
    execute_brightness()