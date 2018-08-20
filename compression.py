import sys
import pickle
import utilities as utils


def recurse(data, rounds=1, total_rounds=5):
    if rounds > total_rounds:
        return data

    new_data = []
    for elem in data:
        if len(elem) < 2:
            new_data.append(elem[0])
        else:
            new_data.append(utils.cantor_pair(*elem))

    rounds += 1
    new_data = list(utils.splice_list(new_data, 2))
    return recurse(new_data, rounds=rounds)


if __name__ == "__main__":
    f_in = utils.big_read(sys.argv[1])
    for pos, elem in enumerate(f_in):
        f_in[pos] = list(elem)

    out = []
    for elem in f_in:
        split = list(utils.splice_list(elem, 2))
        out.append(recurse(split))
    
    print(len(out[0]))
    print(256 * 292)