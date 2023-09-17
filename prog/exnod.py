
def EuclidGcd(a, b):
    if a == 0:
        return b
    if b == 0:
        return a
    if a >= b:
        return EuclidGcd(a % b, b)
    if b >= a:
        return EuclidGcd(a, b % a)

if __name__ == '__main__':
    import time
    b = 0
    for i in range(208, 3918848, 200):
        for j in range(100000):
            start = time.perf_counter()
            a = EuclidGcd(3918848, i)
            end = time.perf_counter()
            b += end - start
            if j == 100000 - 1:
                print(f"{i}; {(b / (100000 - 1)):.8f}")
                b = 0

