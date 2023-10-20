#!/usr/bin/python3
"""
Function for utf8 validation
"""


def validUTF8(data):

	binary_data = []
	index = 0

	for num in data:
		binary_string = bin(num)
		binary_data.append(binary_string[2:])

	print(binary_data)
	print(binary_data[0][1:4])

	for binary_num in binary_data:
			if check_bit(binary_num) or check_size(binary_num):
				return False
			else:
				if binary_num[0] == 0:
					continue
				else:
					count = check_after(binary_num)
					
	return True
 
def check_after(binary_num):
	count = 0
	for char in binary_num[1:4]:
		if char == '1':
			count += 1
		else:
			break
	return count

def check_bit(binary_num):
	count = 0
	for char in binary_num:
		count += 1
	if count > 8:
		return True
	return False
	#couper si sup�rieur � 8

def check_size(binary_num):
	if binary_num[:5] == "11111":
		return True