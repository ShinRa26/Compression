import utilities as utils
from itertools import groupby
import math

FILE = "reaper.m4a"
# FILE = "DBD169_3C1_1.mzML"

def encode(filename):
    pass

def decode(encoded_file):
    pass


def output(data, filesize):
    file_info = FILE.split(".")
    out = {
        "file_size": filesize,
        "file_ext": file_info[-1],
        "file_name": file_info[0],
        "data_string": "|".join(utils.str_to_hex(str(x)) for x in final),
    }

    with open("out.json", "w") as f:
        utils.json.dump(out, f, indent=4)


if __name__ == "__main__":
    final = []
    file_length = 0

    with open(FILE, "rb") as f_d:
        print("Encoding...")
        for data in utils.read_in_chunks(f_d):
            file_length += len(data)
            data = utils.encode_data(data)
            final.append(data[0])
            break

    print("Decoding...")
    decoded = []
    for elem in final:
        target = utils.CHUNK_SIZE
        file_length -= target
        if file_length < 0:
            decoded.append(utils.decode_data(elem, target-abs(file_length)))
        else:
            decoded.append(utils.decode_data([elem], target))
        break


    # output(final, file_length)