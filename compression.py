import sys
import pickle
import itertools
import base64
import zlib
import utilities as utils
from collections import Counter

def compress_and_encode(item):
    if isinstance(item, utils.HuffmanCodec):
        compressed_item = zlib.compress(pickle.dumps(item), 9)
    else:
        compressed_item = zlib.compress(item, 9)

    return base64.a85encode(compressed_item)

if __name__ == "__main__":
    f_in = utils.big_read(sys.argv[1])
    tmp = [elem for elem in itertools.chain(*f_in)]

    output, codecs = [], []
    for elem in f_in:
        out, codec = utils.huffman_encode(elem)
        output.append(compress_and_encode(out))
        codecs.append(compress_and_encode(codec))
