def nod(a, b):
    gcd = 1
    for i in range(max(a, b), 2, -1):
        if (a % i == 0 and b % i == 0):
            gcd = i
            return gcd

if __name__ == '__main__':
    import time
    for i in range(1, 1653264, 200):
        start = time.perf_counter()
        a = nod(3918848, i)
        end = time.perf_counter()
        if a != None:
            print(f"{end - start}; {i}")