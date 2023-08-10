

def product(fracs):
    t = Fraction(reduce(lambda x, y : x * y,fracs))
    #print(t)
    #for frac in fracs:
    #    print(Fraction(frac))
    #    print(Fraction(frac).numerator)
    #    print(Fraction(frac).denominator)
    #t = # complete this line with a reduce statement
    return t.numerator, t.denominator

