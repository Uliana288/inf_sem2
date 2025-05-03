import numpy as np
from math import pi

def non_recursive_fft(x):
    n = len(x)
    if n & (n - 1) != 0:
        raise ValueError("Длина массива должна быть степенью 2")

    even = x[::2].copy()
    odd = x[1::2].copy()

    levels = int(np.log2(n))
    for level in range(1, levels + 1):
        step = 2 ** level
        half = step // 2
        w_step = np.exp(-2j * pi / step)

        w = np.array([w_step ** k for k in range(half)])

        for k in range(0, n, step):
            even_part = x[k:k + half]
            odd_part = x[k + half:k + step]


            x[k:k + step] = np.concatenate([
                even_part + w * odd_part,
                even_part - w * odd_part
            ])

    return x