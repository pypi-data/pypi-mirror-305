from itertools import permutations
def permutation(l):
    result = permutations(l)
    return [list(i) for i in result]