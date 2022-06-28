def get_numbers(base, primesL, n):
    if(base > n):
        return []
    numbers = [base]
    for p in primesL:
        numbers += get_numbers(base * p, primesL, n)   
    return list(set(numbers))
    

def count_find_num(primesL, n):
    base = 1
    for p in primesL:
        base *= p
    
    numbers = get_numbers(base, primesL, n)
    if(len(numbers) == 0):
        return []
    return [len(numbers), max(numbers)]


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
