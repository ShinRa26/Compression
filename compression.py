import sys
import pickle
import itertools
import utilities as utils



if __name__ == "__main__":
    f_in = utils.big_read(sys.argv[1])
    tmp = [elem for elem in itertools.chain(*f_in)]

    out, codec1 = utils.huffman_encode(f_in)
    out2, codec2 = utils.huffman_encode(tmp, freqs=True)
    