import logging
logging.basicConfig(level=logging.DEBUG)

def zeros(n):
    logging.debug('Исходное число n = %s' % n)
    pow_of_5 = 5
    zeros = 0
    iter = 0
    while n >= pow_of_5:
        iter += 1
        zeros += n // pow_of_5
        pow_of_5 *= 5
    logging.debug('количество итераций цикла: %s' % iter)
    return zeros


if __name__ == '__main__':
    assert zeros(0) == 0
    assert zeros(6) == 1
    assert zeros(30) == 7
    assert zeros(633922932) == 158480726
    assert zeros(703594007) == 175898498
