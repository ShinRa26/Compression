import sys
import pickle
import itertools
import base64
import zlib
import numpy as np
import math
import utilities as utils

def bit_totaller(data, bit=0):
    print(f"Current bit: {bit}")
    bit_string = ""
    for elem in data:
        bits = "{:08b}".format(elem)
        bit_string += bits[bit]
    
    try:
        logarithm = math.log10(int(bit_string, 2))
        return logarithm
    except Exception:
        print("Most likely all zeros, returning total number of zeros")
        return len(str(bit_string))


if __name__ == "__main__":
    f_in = [list(elem) for elem in utils.big_read(sys.argv[1], chunk_size=16384)]
    tmp = [elem for elem in itertools.chain(*f_in)]

    
    out = []
    for i in range(8):
        x = bit_totaller(tmp, bit=i)
        out.append(bytes(str(x).encode("utf-8")).hex())

    print(out)
