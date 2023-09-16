def f(n):
    if n == 0:
        return 0
    if n == 1:
        return 1
    if n > 1:
        return f(n - 1) + f(n - 2)

if __name__ == '__main__':
    import timeit
    for i in range(0, 10):
        a = f"f({i})"
        print(str(f"f({i}) = "), timeit.timeit(stmt=a, setup="from __main__ import f"))