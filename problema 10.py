import itertools
multime = {1,2,3,4}
for i in range(len(multime)):
    subm = itertools.combinations(multime, i + 1)
    print(set(multime))