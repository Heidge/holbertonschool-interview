#!/usr/bin/python3
import random
import sys
import signal
from time import sleep
import datetime

status_codes = {"200": 0, "301": 0, "400": 0, "401": 0, "403": 0, "404": 0, "405": 0, "500": 0}
file_size = 0
nbline = 0

for line in sys.stdin:
    status_code = line.split('"')[2].split()[0]
    file_size += int(line.split('"')[2].split()[1])
    for key, value in status_codes.items():
        if status_code == key:
            status_codes[key] = value + 1
    if signal.SIGINT | (nbline % 10 == 0 & nbline != 0):            
        print("File size: {}".format(file_size))
        for key, value in status_codes.items():
            print(key + ": " + str(value))




    #total_size =
    #if signal.SIGINT | linenb % 10 == 0:
        #print(f'File size: {linenb}')
    #linenb + 1
