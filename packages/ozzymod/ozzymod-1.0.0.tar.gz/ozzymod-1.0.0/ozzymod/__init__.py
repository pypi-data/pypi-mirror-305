import os
import math
import json
import base64
import hashlib
from datetime import datetime
import configparser
import time
import socket

def getjson(file, key):
    with open(file, 'r') as file:
        data = json.load(file)
        
    for keya in key:
        data = data[keya]
        
    return data

import configparser

def getini(file, section, key):
    config = configparser.ConfigParser()
    
    try:
        config.read(file)
        return config[section][key]
    
    except (FileNotFoundError, KeyError) as e:
        return f"Error: {e}"

pi = math.pi

def add(num1: int, num2: int):
    return num1 + num2

def subtract(num1: int, num2: int):
    return num1 - num2

def multiply(num1: int, num2: int):
    return num1 * num2

def divide(num1: int, num2: int):
    return num1 / num2

def average(numbers: list):
    if not numbers:
        return 0
    return sum(numbers) / len(numbers)

def findhighest(list: list):
    if not list:
        return None
    
    highest = list[0]
    for number in list:
        if number > highest:
            highest = number
    
    return highest

def factorial(n: int):
    if n < 0:
        return None
    elif n == 0:
        return 1
    else:
        result = 1
        for i in range(1, n + 1):
            result *= i
        return result


def findlowest(list: list):
    if not list:
        return None
    
    lowest = list[0]
    for number in list:
        if number < lowest:
            lowest = number
    
    return lowest

def deldupes(input_list: list):
    return list(set(input_list))

def validate(value: str):
    if value.lower() in [
        "y",
        "ye",
        "yes",
        "ys",
        "1"
    ]:
        return True
    elif value.lower() in [
        "n",
        "no",
        "0",
        "nop",
        "nope"
    ]:
        return False
    else: return False

def gettime():
    return datetime.now().strftime("%H:%M.%S")

def getdate():
    return datetime.now().strftime("%Y-%m-%d")

def getepoch():
    return int(time.time())

def base64encode(string):
    encoded_bytes = base64.b64encode(string.encode('utf-8'))
    return encoded_bytes.decode('utf-8')

def base64decode(string):
    decoded_bytes = base64.b64decode(string.encode('utf-8'))
    return decoded_bytes.decode('utf-8')

def sha256encode(string): # THERE IS NO DECODE METHOD FOR SHA256
    sha_signature = hashlib.sha256(string.encode('utf-8')).hexdigest()
    return sha_signature

def iswifi():
    try:
        socket.create_connection(("8.8.8.8", 53), timeout=5)
        return True
    except OSError:
        return False

