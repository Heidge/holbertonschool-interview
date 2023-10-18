#!/usr/bin/python3
"""
Function for utf8 validation
"""


def validUTF8(data):
    num_bytes = 0

    for num in data:
        if num >= 128:
            if num_bytes == 0:
                if (num >> 5) == 0b110:
                    num_bytes = 1
                elif (num >> 4) == 0b1110:
                    num_bytes = 2
                elif (num >> 3) == 0b11110:
                    num_bytes = 3
                else:
                    return False
            else:
                if (num >> 6) != 0b10:
                    return False
                num_bytes -= 1
        else:
            if num_bytes != 0:
                return False

    return True
