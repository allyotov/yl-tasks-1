def zeros(n):
    pow_of_5 = 5
    zeros = 0
    
    while n >= pow_of_5:
        zeros += n // pow_of_5
        pow_of_5 *= 5
        
    return zeros

if __name__ == '__main__':
    assert zeros(0) == 0
    assert zeros(6) == 1
    assert zeros(30) == 7
