from fractions import Fraction
x = ['w']*5 + ['b']*4
y = ['w']*7 + ['b']*6
def black_probability(x, y):
    return (Fraction(x.count('w') * y.count('b'), len(x) * (len(y)+1)) + Fraction(x.count('b') * (y.count('b')+1), len(x) * (len(y)+1)))  
print(black_probability(x, y))
