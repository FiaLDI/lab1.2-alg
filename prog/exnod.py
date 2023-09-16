
def EuclidGcd(a, b):
    if a == 0:
        return b
    if b == 0:
        return 0
    if a >= b:
        return EuclidGcd(a % b, b)
    if b >= a:
        return EuclidGcd(a, b % a)

if __name__ == '__main__':
    import timeit
    b = 0
    for y in range(1, 10):

        a = f"EuclidGcd{(i,j)}"
        print(EuclidGcd(i, j))
        timee = timeit.timeit(stmt = a,setup="from __main__ import EuclidGcd")
        b += timee
        if y == 10-1:
            b /= 10
    print(b)


