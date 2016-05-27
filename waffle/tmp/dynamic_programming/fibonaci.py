# -*- coding: utf-8 -*-


def fibo(n):
    if n == 0:
        return 0
    if n == 1:
        return 1
    if n == 2:
        return 1
    fibo_series = [1, 1]

    for i in range(2, n+1):
        added = fibo_series[i-1] + fibo_series[i-2]
        fibo_series.append(added)

    return fibo_series[-1]

print(fibo(6))
