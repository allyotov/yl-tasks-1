import logging

logging.basicConfig(level=logging.INFO)


def multiply_list(numbers_list):
    result = 1
    for element in numbers_list:
        result *= element
    return result

def count_find_num(primesL, limit):
    mults = set()
    first_mult = multiply_list(primesL)
    greatest = first_mult
    if first_mult < limit:
        mults.add(first_mult)
    elif first_mult == limit:
        return [1, first_mult]
    else:
        logging.debug('no way')
        return []

    logging.debug('first mult %s' % first_mult)
    logging.debug('greatest %s' % greatest)

    initial_copy = primesL[:]
    el = 0
    pow = 1
    while multiply_list(primesL) < limit:
        for i, element in enumerate(primesL):
            degree = 1
            multiplication = 0
            while True:
                prime_list_copy = primesL[:]
                prime_list_copy[i] = element * initial_copy[i] ** degree
                logging.debug('current list [%s]' % ', '.join([str(element) for element in prime_list_copy]))
                multiplication = multiply_list(prime_list_copy)
                logging.debug('Multiplication: %s' % multiplication)
                if multiplication <= limit:
                    mults.add(multiplication)
                    if multiplication > greatest:
                        greatest = multiplication
                    degree += 1
                else:
                    break
        logging.debug('\n\n\n')
        primesL = initial_copy[:]
        primesL[el] *= initial_copy[el] ** pow
        el += 1
        if el > len(primesL) - 1:
            el = 0
            pow += 1

    extended = True
    while extended:
        extended = False
        for mult in initial_copy:
            for old_mult in list(mults):
                new_mult = mult * old_mult
                if new_mult not in mults and new_mult <= limit:
                    extended = True
                    mults.add(new_mult)
                    if greatest < new_mult:
                        greatest = new_mult
    
    logging.debug('numbers [%s]' % ', '.join([str(element) for element in sorted(list(mults))]))
    logging.debug('count %s' % len(mults))
    logging.debug('greatest %s' % greatest)
    return [len(mults), greatest]


if __name__ == '__main__':
    primesL = [2, 5, 7]
    limit = 500
    assert count_find_num(primesL, limit) == [5, 490]


    primesL = [2, 3]
    limit = 200
    assert count_find_num(primesL, limit) == [13, 192]

    primesL = [2, 5]
    limit = 200
    assert count_find_num(primesL, limit) == [8, 200]

    primesL = [2, 3, 5]
    limit = 500
    assert count_find_num(primesL, limit) == [12, 480]

    primesL = [2, 3, 5]
    limit = 1000
    assert count_find_num(primesL, limit) == [19, 960]

    primesL = [2, 3, 47]
    limit = 200
    assert count_find_num(primesL, limit) == []
    logging.info('All tests passed!')