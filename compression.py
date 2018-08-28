import sys
import zlib
import math
import pickle
import base64
import itertools
import numpy as np
import utilities as utils

if __name__ == "__main__":
    f_in = [list(elem) for elem in utils.big_read(sys.argv[1])]
    tmp = [elem for elem in itertools.chain(*f_in)]

    x = math.log2(tmp[1])
    print(x)