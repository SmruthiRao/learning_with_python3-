def comp_int(p,r,n,t):
    a = p * (1 + r/n) ** (n*t)
    return a

investment = float(input('Enter amount you wish to invest : '))
amt = comp_int(investment,0.08,12,5)
print('compound interest at end of year is ', amt)
