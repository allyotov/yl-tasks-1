import logging

logging.basicConfig(level=logging.DEBUG)

def zeros(n):
    num_zeros = 0
    for i in range(1, n + 1):
        if i % 5 == 0:
            logging.debug('dev. by 5: %s' % i)
            num_zeros += 1
            new_i = i
            while True:
                new_i = new_i / 5
                if new_i % 5 == 0:
                    num_zeros += 1
                else:
                    break
    logging.debug('Number: %s' % n)
    logging.debug('Trailing zeros: %s' % num_zeros)
    return num_zeros


if __name__ == '__main__':
    assert zeros(0) == 0
    assert zeros(6) == 1
    assert zeros(30) == 7
