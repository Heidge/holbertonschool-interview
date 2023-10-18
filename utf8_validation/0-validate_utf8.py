#!/usr/bin/python3
"""
Function for utf8 validation
"""


def validUTF8(data):

	dataL = len(data)
	binary_data = []
	count = 0
	i = 1
	
	for num in data:
		binary_string = bin(num)
		binary_data.append(binary_string[2:])

	print(binary_data)
	if binary_data[0][:5] == "11111":
		return False

	first_string = str(binary_data[0][:4])

	for char in first_string:
		if char == '1':
			count += 1
	
	for binary_num in binary_data:
		if i == count:
			break
		else:
			if binary_num[i][:2] == "10" or binary_num[i][:1] == "0":
				continue
				i += 1
			else:
				return False

	return True
 
