import utilities as utils

FILE = "noise.b"


def convert_to_bit_string(data):
    out = [bin(x).lstrip("0b").zfill(8) for x in data]
    return out

def compress(data):
    pass

def pair_loop(data):
    while len(data) >= 2:
        data = list(utils.splice_list(data, 2))
        data = [int(utils.elegant_pair(*elem)) for elem in data]

    return data

def run():
    with open(FILE, "rb") as f_d:
        print("Encoding...")
        for data in utils.read_in_chunks(f_d):
            data = pair_loop(data)
            # TODO::Add each summation to new list, log, and repeat

if __name__ == "__main__":
    run()
