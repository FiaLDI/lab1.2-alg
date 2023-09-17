def nod(a, b):
    gcd = 1
    for i in range(2, max(a, b)):
        if a % i == 0 and b % i == 0:
            gcd = i
    return gcd

if __name__ == '__main__':
    import time
    b = 0
    for i in range(208, 3918848, 200):
        for j in range(10):
            start = time.perf_counter()
            a = nod(3918848, i)
            end = time.perf_counter()
            b += end - start
            if j == 10-1:
                print(f"{i}; {b/(10-1)}, {a}")
                b = 0