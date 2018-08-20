import sys
import pickle
import base64
import zlib
import itertools
import utilities as utils


def infinity_check(data):
    for elem in data:
        if elem == float("Inf"):
            return True
    return False


if __name__ == "__main__":
    f_in = utils.big_read(sys.argv[1])
    for pos, elem in enumerate(f_in):
        f_in[pos] = list(elem)

    out = []
    for elem in f_in:
        split = list(utils.splice_list(elem, 2))
        out.append(utils.recurse_pair(split, total_rounds=7))
    

    x = [elem for elem in itertools.chain(*out)]
    y = [elem for elem in itertools.chain(*x)]
    if infinity_check(y):
        print("Impossible number: Infinity")
        sys.exit(-1)

    # Try Huffman again with pairing