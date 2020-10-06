def square_rt(n):
    counter = 0
    approx = n/10
    while True:
        better = (approx + n/approx)/2.0
        counter += 1
        if abs(better-approx) < 0.001:
            return (counter,better)
        approx = better


print(square_rt(625))
print(square_rt(10000))
print(square_rt(99))

