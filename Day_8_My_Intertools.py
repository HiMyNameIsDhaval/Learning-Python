
# Intertools : product, permutation, combination, accumlate, groupby, and infinite iterators

from itertools import combinations_with_replacement, product

print('Product')
print(' ')

a = [1,2,5]
b = [3]


prod = product(a,b, repeat=2)
print(prod)
print(list(prod))
print(' ')

from itertools import permutations

print('Permutations')
print(' ')


c = [1,2,3]

perm = permutations(c)
perm_1 = permutations(c, 2)

print(perm)
print(list(perm))
print(' ')
print(list(perm_1))
print(' ')

from itertools import combinations

print('Combination')
print(' ')

d = [4,2,8,6]

comb = combinations(d,4)

print(comb)
print(list(comb))
print(' ')

comb_wr = combinations_with_replacement(d,4)
print(list(comb_wr))