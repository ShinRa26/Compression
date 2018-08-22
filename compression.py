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

    # Small output, large codec
    out1, codec1 = utils.huffman_encode(f_in)
    # Large output, small codec
    # out2, codec2 = utils.huffman_encode(tmp)

    out2, codec2 = utils.huffman_encode(pickle.dumps(codec1))
    out2 = bz2.compress(out2)
    print(len(list(out2)))

    # Large codec decrypts large output
    # Small codec does not decrypt small output
    # utils.write_file(base64.b64encode(out2), "out.txt", flag="wb")
    # utils.write_file(base64.b64encode(pickle.dumps(codec2)), "codec.txt", flag="wb")
