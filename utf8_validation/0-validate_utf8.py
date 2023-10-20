#!/usr/bin/python3
"""
Function for utf8 validation
"""


def validUTF8(data):
    """Determines if a given data set represents a valid UTF-8 encoding"""

    binary_data = []
    index = 0

    for num in data:
        binary_string = bin(num)
        binary_data.append(binary_string[2:])

    print(binary_data)
    print(binary_data[0][1:4])

    for binary_num in binary_data:
        if check_bit_too_large(binary_num) or check_size(binary_num):
            return False
        else:
            if check_bit_small(binary_num):
                continue
            else:
                count = check_after(binary_num)
                for x in binary_data:
                    if x == binary_num:
                        for x in range(count):
                            x += 1
                            if binary_data[index + x][:2] == "10":
                                continue
                            else:
                                return False
                index += 1
    return True


def check_after(binary_num):
    count = 0
    for char in binary_num[1:4]:
        if char == "1":
            count += 1
        else:
            break
    return count


def check_bit_too_large(binary_num):
    count = 0
    for char in binary_num:
        count += 1
    if count > 8:
        return True
    return False
    # couper si supérieur à 8


def check_bit_small(binary_num):
    count = 0
    for char in binary_num:
        count += 1
    if count < 8:
        return True
    return False


def check_size(binary_num):
    if binary_num[:5] == "11111":
        return True