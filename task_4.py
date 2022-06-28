from itertools import combinations


def skip_letters(word, skips):
    word_list = list(word)
    for skip in skips:
        word_list[skip] = '-'
    word_with_skips = ''.join(word_list)
    rest_word = word_with_skips.replace('-', '')
    return rest_word, word_with_skips    

def bananas(s) -> set:
    result = set()
    for skips in combinations(list(range(len(s))), len(s) - 6):
        rest_word, word_with_skips = skip_letters(s, skips)
        if rest_word == 'banana':
            result.add(word_with_skips)
    return result

if __name__ == '__main__':
    assert bananas("banann") == set()
    assert bananas("banana") == {"banana"}
    assert bananas("bbananana") == {"b-an--ana", "-banana--", "-b--anana", "b-a--nana", "-banan--a",
                        "b-ana--na", "b---anana", "-bana--na", "-ba--nana", "b-anan--a",
                        "-ban--ana", "b-anana--"}
    assert bananas("bananaaa") == {"banan-a-", "banana--", "banan--a"}
    assert bananas("bananana") == {"ban--ana", "ba--nana", "bana--na", "b--anana", "banana--", "banan--a"}
