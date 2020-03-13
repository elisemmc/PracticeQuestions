from primes import primes
from collections import Counter

def euler49():
    p = primes()
    ps = [x for x in p.primesLessThan(10000) if x > 999 ]
    retVal = []
    # print(ps)

    for item in ps:
        # item = 1487
        s = list(str(item))
        perms = [
            listToInt(i)
            for i in permutations(s) 
            if listToInt(i) in ps ]

        perms.sort()
        diffs = differences(perms)
        for key, val in diffs.items():
            for k,v in diffs.items():
                if key != k:
                    val_set = set(val)
                    intersections = val_set.intersection(v)
                    if len(intersections) > 0:
                        for i in intersections:
                            maxVal = key
                            midVal = key - i
                            minVal = key - 2*i
                            if maxVal in ps and midVal in ps and minVal in ps:
                                if maxVal in perms and midVal in perms and minVal in perms:
                                    ret = str(minVal) + str(midVal) + str(maxVal)
                                    if ret not in retVal:
                                        retVal.append(ret)
    print(retVal)

def differences(lst):
    retVal = { lst[0] : {} }
    for i in range(1, len(lst)):
        retVal[lst[i]] = {lst[i] - j for j in lst[:i]}
    return retVal

def isPermutation(x, y):
    sorted_x = [item for item in x] # Shallow copy x
    sorted_x.sort()
    print(sorted_x)

    sorted_y = [item for item in y] # Shallow copy y
    sorted_y.sort()
    print(sorted_y)

    return x == y

def permutations(lst):
    if len(lst) == 1:
        return [lst]
    
    retVal = []
    for i in range(len(lst)):
        m = [ lst[i] ]
        # print(f'm : {m}')
        remLst = lst[:i] + lst[i+1:]
        # print(f'r : {remLst}')
        for p in permutations(remLst):
            newPerm = m + p
            if newPerm not in retVal:
                retVal.append( newPerm )
    return retVal

def listToInt(lst):
    return int(''.join(lst))

if __name__ == '__main__':
    # print(permutations(list([1,1,2,3])))
    # print(differences([1487,4817,8147]))
    euler49()