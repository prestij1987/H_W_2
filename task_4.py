
# Написать метод bananas, который принимает на вход строку и
# возвращает количество слов «banana» в строке.

# (Используйте - для обозначения зачеркнутой буквы)

def bananas(s) -> set:
    find_word = 'banana'
    result = set()
    for combination in combinations(range(len(s)), len(s) - len(find_word)):
        list_s = list(s)
        for index in combination:
            list_s[index] = '-'
        variant = ''.join(list_s)
        if variant.replace('-', '') == find_word:
            res.add(variant)
    return res
              
