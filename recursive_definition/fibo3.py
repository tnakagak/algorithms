# coding: utf-8
# フィボナッチ数列（繰り返し）

def fibo(n):
    a1, a2 = 1, 0
    while n > 0:
        a1, a2 = a1 + a2, a1
        n -= 1
    return a1

if __name__ == '__main__':
    for i in range(10):
        print 'fibo(', i, ')=', fibo(i)
