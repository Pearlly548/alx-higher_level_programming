#!/usr/bin/python3
# 102-magic_calculation.py

def magic_calculation(a, b, c):
 """Match bytecode provided by Holberton School."""
    if a > b:
        return a - b
    elif a < b:
        return (a + b) * c
    else:
        return a * b - c

