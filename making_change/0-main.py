#!/usr/bin/python3
"""
Main file for testing
"""


import sys


makeChange = __import__('0-making_change').makeChange

print(makeChange([1, 2, 5, 10, 25, 50, 100], 972))