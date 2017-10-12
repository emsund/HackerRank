from math import factorial

boy, girl = 1.09, 1
prob_boy = boy/(boy+girl)

trials = 6


def bi(x,n,p):
    c = factorial(n)/((factorial(x)*factorial(n-x)))
    b = c * (p**x) * ((1-p)**(n-x))
    return(b)

# "at least 3 boys" means "3 boys OR 4 boys OR 5 boys OR 6 boys"
b = [bi(boys, trials, prob_boy) for boys in range(3,7)]
b = sum(b)

print(round(b, 3))
