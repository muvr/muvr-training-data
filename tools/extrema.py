from fractions import Fraction
import scipy.signal as sig
import itertools
import numpy as np

smooth_windows = ['flat', 'hanning', 'hamming', 'bartlett', 'blackman']

def tswap(a):
    return a[1], a[0]

def smooth(x, window_len=11, window='hanning'):
    """Smooth function from SciPy cookbook: http://wiki.scipy.org/Cookbook/SignalSmooth"""
    if x.ndim != 1:
        raise ValueError, "smooth only accepts 1 dimension arrays."

    if x.size < window_len:
        raise ValueError, "Input vector needs to be bigger than window size."

    if window_len < 3:
        return x

    if not window in smooth_windows:
        raise ValueError, ("Window is non of %s" % ", ".join(smooth_windows))


    s = np.r_[x[window_len-1:0:-1], x, x[-1:-window_len:-1]]
    if window == 'flat':  # moving average
        w = np.ones(window_len, 'd')
    else:
        w = getattr(np, window)(window_len)

    y = np.convolve(w/w.sum(), s, mode='valid')
    return y

def extrema(arr):
    arr_smooth = smooth(arr, window_len=51)
    maxima = sig.argrelmax(arr_smooth)[0]
    minima = sig.argrelmin(arr_smooth)[0]
    return maxima, minima

def find_window(arr, v):
    size = arr.shape[0]

    # Find closest index and value matching v
    closest_index = np.searchsorted(arr, v)
    closest_index = closest_index if closest_index < size else size - 1
    closest = arr[closest_index]

    # Attempt to find indexes and values surrounding v
    prev_index, next_index = (closest_index - 1, closest_index) if v < closest else (closest_index, closest_index + 1)
    prev = arr[prev_index] if prev_index >= 0 else None
    next_ = arr[next_index] if next_index < size else None

    # Adjust surrounding values on edge cases
    if prev_index < 0:
        prev = v - (next_ - v)

    if next_index >= size:
        next_ = v + (v - prev)

    return (v - prev) / 4, (next_ - v) / 4

def has_between(arr, low, high):
    low_i, high_i = np.searchsorted(arr, [low, high])
    for closest in arr[low_i-1:high_i+1]:
        if low < closest < high:
            return True
    return False

def matching_values_ratio(source, window_source, target):
    counter = 0
    for v in source:
        left, right = find_window(window_source, v)
        if has_between(target, v - left, v + right):
            counter += 1
    return Fraction(counter, source.shape[0])

def matching_values_mean(first, second):
    n1 = matching_values_ratio(first[0], first[1], second[0])
    n2 = matching_values_ratio(second[0], second[1], first[0])
    return (n1 + n2) / 2

def matching_values_all_combinations(first, second):
    combs = [
        (first, second),
        (tswap(first), second),
        (first, tswap(second)),
        (tswap(first), tswap(second)),
    ]
    return (matching_values_mean(a, b) for a, b in combs)

def matching_extrema(arr):
    ex = [extrema(a) for a in arr]
    combs = [(0, 1), (0, 2), (1, 2)]
    res = (matching_values_all_combinations(ex[a], ex[b]) for a, b in combs)
    return (float(v) for v in itertools.chain(*res))

