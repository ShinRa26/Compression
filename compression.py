import sys
import pickle
import itertools
import base64
import bz2
import utilities as utils
from collections import Counter


if __name__ == "__main__":
    f_in = utils.big_read(sys.argv[1])
    tmp = [elem for elem in itertools.chain(*f_in)]

    compressed = bz2.compress(bytes(tmp))

    # Small output, large codec
    # out1, codec1 = utils.huffman_encode(compressed)
    # Large output, small codec
    # out2, codec2 = utils.huffman_encode(compressed, freqs=True)
    

    # Large codec decrypts large output
    # Small codec does not decrypt small output1
