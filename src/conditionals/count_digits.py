def count_digits(n):
    dig = 0
    while n != 0:
        dig += 1
        n //= 10
    return dig


print('No of digits is ', count_digits(2134))
print('No of digits is ', count_digits(1))
print('No of digits is ', count_digits(1256128438))
