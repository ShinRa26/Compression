import json
import math
from dahuffman import HuffmanCodec

def read_file(filename, flag="rb"):
    with open(filename, flag) as f:
        return [byte for byte in f.read()]

def read_in_chunks(f_obj, chunk_size=16384):
    while True:
        data = f_obj.read(chunk_size)
        if not data:
            break
        yield data

def big_read(filename, chunk_size=16384, flag="rb"):
    print(f"Reading {filename}...")
    f = open(filename, flag)
    data = list(read_in_chunks(f, chunk_size=chunk_size))
    f.close()

    return data

def big_write(data, filename, flag="wb"):
    print(f"Writing to {filename}...")
    with open(filename, flag) as f:
        for elem in data:
            f.write(elem)


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

def huffman_encode(data):
    print(f"Building Huffman Codec...")
    codec = HuffmanCodec.from_data(data)
    print(f"Codec built!")
    print("Encoding data...")
    out = codec.encode(data)

    return out, codec

def huffman_decode(data, codec):
    return codec.decode(data)
