# -*- coding: utf-8 -*-


def fibo(n):
    if n == 0:
        print("Invalid Input")
        raise Exception
    if n == 1:
        return 1
    if n == 2:
        return 1
    else:
        fibo_series = [1, 1]
        k = n - 1
        for i in range(2, n):
            added = fibo_series[i-1] + fibo_series[i-2]
            fibo_series.append(added)
            # fibo_series[i] = added
        print(fibo_series)
        return fibo_series[-1]

print(fibo(6))
