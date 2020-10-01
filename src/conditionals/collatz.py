def collatz(n):
    """ run till n is 1, if num is even divide by 2, if odd, calc 3n+1"""
    while n != 1:
        print(n, end=', ')
        if n % 2 == 0:
            n //= 2
        else:
            n = 3*n + 1
    print(n, end='.\n')


collatz(3)
collatz(21)
collatz(16)
