import sys
import pickle
import itertools
import base64
import zlib
import utilities as utils

if __name__ == "__main__":
    f_in = [list(elem) for elem in utils.big_read(sys.argv[1], chunk_size=1024*1024)]
    # tmp = [elem for elem in itertools.chain(*f_in)]

    chunk = f_in[0]
    print(chunk)
