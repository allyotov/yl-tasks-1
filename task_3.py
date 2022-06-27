def zeros(n):
    n_zeros = 0
    while(n >= 5):
        n //= 5
        n_zeros += n
    return n_zeros


if __name__ == '__main__':
    assert zeros(0) == 0
    assert zeros(6) == 1
    assert zeros(30) == 7
