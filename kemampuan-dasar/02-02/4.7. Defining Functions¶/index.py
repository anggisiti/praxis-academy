def fib(n):  # write Fibonacci eries up to n
    # a, b = 0, 1
    a, b = 0,10
    a = 0
    b= 1
    while a < n:
            print(a, end=" ")
            a, b = b, a+b
    print()
fib(2000)
