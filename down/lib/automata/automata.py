from functools import reduce

import numpy as np

def filter(n):
    assert n<=7
    assert n>=0

    arr = np.zeros(3)
    for i in range(2,-1,-1):
        pos_val = 2**(i)
        if n >= pos_val:
            arr[i]=1
            n-=pos_val
    return arr


def filters(rule_number):
    """Rule number is in """
    filters = []
    inc = "{0:b}".format(rule_number)[::-1]
    for i,v in enumerate(inc):
        if v=='1':
            filters.append(filter(i))
    return filters


def apply_filter(state, f):
    vf = np.vectorize(lambda x: 1 if x==f.sum() else 0)
    return vf(np.convolve(state, f, mode='same'))


def apply_filters(state, fs):
    res = np.array([apply_filter(state, f) for f in fs])
    res = np.sum(res,axis=0)
    return (res%2)


def generate_1d(rule_number, init_state, n_rows):
    """ 
    Inputs:
        rule_number - the Wolfram rule number that dictates which patterns calls for propagation
        init_state - 
        n_rows - 
    Output:
        binary numpy ndarray of size (n_rows, len(init_state))



