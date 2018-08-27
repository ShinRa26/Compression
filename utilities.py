import json
import math
import zlib
import pickle
import base64
from collections import Counter
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

def recurse_pair(data, rounds=1, total_rounds=5):
    if rounds > total_rounds:
        return data

    print(f"Splicing list: Round: {rounds}/{total_rounds}")
    new_data = []
    for elem in data:
        if len(elem) < 2:
            new_data.append(elem[0])
        else:
            new_data.append(cantor_pair(*elem))

    rounds += 1
    new_data = list(splice_list(new_data, 2))
    return recurse_pair(new_data, rounds=rounds, total_rounds=total_rounds)

def infinity_check(data):
    for elem in data:
        if elem == float("Inf"):
            return True
    return False

def huffman_codec(input_data, freqs=False):
    if freqs:
        return HuffmanCodec.from_frequencies(Counter(input_data))
    return HuffmanCodec.from_data(input_data)

def huffman_encode(data, freqs=False):
    print(f"Building Huffman Codec...")
    codec = huffman_codec(data, freqs=freqs)
    print(f"Codec built!")
    print("Encoding data...")
    out = codec.encode(data)

    print("Compressing output and codec with zlib...")
    compressed_output = zlib.compress(out, 9)
    compressed_codec = zlib.compress(pickle.dumps(codec), 9)

    encoded_output = base64.a85encode(compressed_output)
    encoded_codec = base64.a85encode(compressed_codec) 

    return encoded_output, encoded_codec

def huffman_decode(data, codec):
    print("Rebuilding Huffman codec from supplied string...")
    decoded_codec = base64.a85decode(codec)
    decompressed_codec = pickle.loads(zlib.decompress(decoded_codec))
    print("Codec rebuilt!")

    print("Decoding input...")
    decoded_output = base64.a85decode(data)
    decompressed_output = zlib.decompress(decoded_output)
    out = decompressed_codec.decode(decompressed_output)
    print("Decoded!")

    return out
