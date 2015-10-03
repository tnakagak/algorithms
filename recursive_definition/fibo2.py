# coding: utf-8
# フィボナッチ関数（末尾再帰）

def fibo(n, a1 = 1, a2 = 0):
    if n < 1: return a1
    return fibo(n - 1, a1 + a2, a1)

if __name__ == '__main__':
    for i in range(10):
        print 'fibo(', i, ')=', fibo(i)
