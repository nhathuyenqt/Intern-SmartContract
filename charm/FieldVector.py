from GlobalConfig import *


    
def subtract(vec1, vec2):

    print(vec1[0] - vec2[0])
    res = [vec1[i] - vec2[i] for i in range(n)]
    return res

def hadamard_product(vec1, vec2):

    had = []
    for i in range(n):
        had.append(vec1[i] * vec2[i])
    return had
    
def mul(vec, num):
    res = [vec[i] *num for i in range(n)]
    return res

def add(vec1, vec2):
    res = []
    for i in range(n):
        res.append(vec1[i] + vec2[i])
    return res

uni_vec = [group1.init(ZR, 1) for i in range(n)]
bin_vec = [group1.init(ZR, 2**i) for i in range(n)]


