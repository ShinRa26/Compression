import random

FILENAME = "noise.b"
KB = 1024

data = [random.choice(range(0,256)) for _ in range(KB*KB*16)]

with open(FILENAME, "wb") as f_d:
    f_d.write(bytes(data))
