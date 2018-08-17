f = open('Week2IntegerArray.txt')
l = []
for line in f:
    x = line.strip()
    l.append(int(x))



def inversions(items):
    n = len(items)
    if n <= 1:
        return items, 0

    # number of inversions in partitions
    left, linv = inversions(items[:n // 2])
    right, rinv = inversions(items[n // 2:])

    inv = linv + rinv
    llen, rlen = len(left), len(right)
    i, j, aux = 0, 0, []

    # merge and count inversions
    for k in range(n):
        if i < llen and j < rlen and left[i] > right[j]:
            inv += llen - i
            aux.append(right[j])
            j += 1
        elif i < llen:
            aux.append(left[i])
            i += 1
        else:
            aux.append(right[j])
            j += 1

    return aux, inv

print(len(l))
aux, inv = inversions(l)
print(inv)

'''
%timeit inversions(l)
440 ms ± 2.86 ms per loop (mean ± std. dev. of 7 runs, 1 loop each)
'''