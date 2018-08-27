import sys
import pickle
import itertools
import base64
import zlib
import utilities as utils
from collections import Counter


if __name__ == "__main__":
    f_in = [list(elem) for elem in utils.big_read(sys.argv[1])]
    tmp = [elem for elem in itertools.chain(*f_in)]
    