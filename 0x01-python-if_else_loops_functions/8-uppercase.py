#!/usr/bin/python3

def uppercase(str):
    result = ""
    for c in str:
        result += chr(ord(c) - 32) if 'a' <= c <= 'z' else c
    print("{}".format(result))
