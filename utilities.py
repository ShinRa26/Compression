import json
import math
import zlib
import pickle
import base64
import random
from collections import Counter

CHUNK_SIZE = 4096
ARBITRARY = 255

def read_file(filename, flag="rb"):
    with open(filename, flag) as f:
        return [byte for byte in f.read()]

def read_in_chunks(f_obj, chunk_size=CHUNK_SIZE):
    while True:
        data = f_obj.read(chunk_size)
        if not data:
            break
        yield list(data)

def big_read(filename, chunk_size=CHUNK_SIZE, flag="rb"):
    print(f"Reading {filename}...")
    f = open(filename, flag)
    data = list(read_in_chunks(f, chunk_size=chunk_size))
    f.close()
    print(f"Finished reading {filename}!")

    return data

def big_write(data, filename, flag="ab"):
    print(f"Writing to {filename}...")
    for elem in data:
        f = open(filename, flag)
        f.write(elem)
        f.close()


def write_file(data, filename, flag="w"):
    print(f"Writing to {filename}...")
    with open(filename, flag) as f:
        f.write(data)

def read_json(filename):
    with open(filename) as f:
        return json.load(f)

def write_json(data, filename):
    with open(filename, "w") as f:
        json.dump(data, f)

def splice_list(l, n):
    for i in range(0, len(l), n):
        yield l[i:i+n]

def cantor_pair(x, y):
    return (((x + y + 1) * (x + y))/2) + y

def cantor_unpair(num):
    w = math.floor((math.sqrt(8*num + 1) - 1) / 2)
    t = (w ** 2 + w)/2
    y = num - t
    x = w - y

    return x, y

def infinity_check(data):
    for elem in data:
        if elem == float("Inf"):
            return True
    return False

def encode_data(data):
    if len(data) < 2:
        return data
    data = list(splice_list(data, 2))
    new_data = []
    for elem in data:
        if len(elem) < 2:
            elem.append(0)
        if elem[0] == 0 and elem[1] == 0:
            new_data.append(0)
            continue
        c = cantor_pair(elem[0], elem[1])
        if c < 0:
            new_data.append(c/CHUNK_SIZE)
        else:
            new_data.append(math.log10(c)/CHUNK_SIZE)
    return encode_data(new_data)


def decode_data(data, target_length):
    if len(data) == target_length:
        return data

    new_data = []
    data = list(splice_list(data, 2))

    for elem in data:
        for subelem in elem:
            if subelem == 0 or subelem == 1:
                new_data.append(subelem)
                continue
            cantor = subelem * CHUNK_SIZE
            if cantor > 255 or cantor < -1:
                new_data.append(subelem)
                continue
            if cantor < 0:
                x, y = cantor_unpair(cantor)
            else:
                cantor = 10**cantor
                x, y = cantor_unpair(cantor)
            new_data.append(x)
            new_data.append(y)
    
    return decode_data(new_data, target_length)


def str_to_hex(string):
    out = ""
    for char in string:
        out += hex(ord(char)).lstrip("0x")
    
    return out


def zlib_compress(data, level=9):
    return zlib.compress(data, level)

def zlib_decompress(data):
    return zlib.decompress(data)
