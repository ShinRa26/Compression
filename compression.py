import utilities as utils
from itertools import groupby
import random

FILE = "reaper.m4a"
# FILE = "DBD169_3C1_1.mzML"

# ASCII Range 33-126

def binarise(data):
    for pos, elem in enumerate(data):
        data[pos] = format(elem, "08b")
    return data

def compress(data):
    for pos, elem in enumerate(data):
        data[pos] = str(len(elem)) + "*" + elem[0] + " "
    return data

def generate_mappings(counts):
    mappings = {}
    start = 33
    for key in counts.keys():
        mappings[key] = chr(start)
        start += 1
    return mappings

def replace_mappings(mapping, data_string):
    for key, value in mapping.items():
        data_string = data_string.replace(key, value)
    return data_string

if __name__ == "__main__":
    with open(FILE, "rb") as f_d:
        for data in utils.read_in_chunks(f_d):
            print(utils.Counter(data))
            break


            # data = list("".join(x for x in binarise(data)))
            # data = [list(g) for k,g in groupby(data)]
            # data = compress(data)
            # data = "".join(x for x in data)
            # data = data.encode("utf-8").hex()
            # tmp = list(utils.splice_list(data, 4))
            # counts = dict(utils.Counter(tmp))
            # mappings = generate_mappings(counts)
            # data = replace_mappings(mappings, data)
            # print(data)
