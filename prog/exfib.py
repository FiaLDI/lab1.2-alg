if __name__ == '__main__':
    import time
    b = 0
    for n in range(3, 15):
        for j in range(1, 1000000):
            start = time.perf_counter()
            a = [i * 0 for i in range(n + 1)]
            a[0] = 0
            a[1] = 1
            for i in range(2, n + 1):
                a[i] = a[i - 1] + a[i - 2]
            end = time.perf_counter()
            b += (end - start)
        b = b / 1000000
        print(f"{b:.09f} - {a[n - 1]}")
        b = 0