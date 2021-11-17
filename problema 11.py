import itertools
multime = {'A', 'B', 'C', 'D'}
for lengh in range(len(multime)):
    submultime = itertools.combinations(multime, lengh + 1)
    print(set(submultime))