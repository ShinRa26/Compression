import sys
import pickle
import itertools
import base64
import zlib
import utilities as utils


if __name__ == "__main__":
    f_in = utils.big_read(sys.argv[1])
    tmp = [elem for elem in itertools.chain(*f_in)]
    x = [hex(elem).lstrip("0x").encode("utf-8") for elem in tmp]
    print(x)