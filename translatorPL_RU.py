# -*- coding: utf-8 -*-

def main(first=True):
    if first:
        print "--------------------------------------"
        print "Zamiennik polskich liter na rosyjskie"
        print "--------------------------------------"
    print "Podaj literę::"
    letter = raw_input()
    letter = letter.lower()
    alphabet = {'a' : 'Аа',
    'b' : 'Бб',
    'be' : 'Бб',
    'w' : 'Вв',
    'wy' : 'Вв',
    'g' : 'Гг',
    'gie' : 'Гг',
    'd' : 'Дд',
    'de' : 'Дд',
    'je' : 'Ee',
    'je' : 'Ee',
    'jo' : 'Ёё',
    'ż' : 'Жж',
    'że' : 'Жж',
    'żet' : 'Жж',
    'z' : 'Зз',
    'zy' : 'Зз',
    'i' : 'Ии',
    'j' : 'Йй',
    'k' : 'Кк',
    'ka' : 'Кк',
    'l' : 'Лл',
    'el' : 'Лл',
    'ł' : 'Лл',
    'eł' : 'Лл',
    'm' : 'Мм',
    'em' : 'Мм',
    'n' : 'Нн',
    'en' : 'Нн',
    'o' : 'Oo',
    'p' : 'Пп',
    'pe' : 'Пп',
    'r' : 'Рр',
    'er' : 'Рр',
    'ry' : 'Рр',
    's' : 'Cc',
    'es' : 'Cc',
    'es' : 'Cy',
    't' : 'Tt',
    'te' : 'Tt',
    'ty' : 'Tt',
    'u' : 'Уу',
    'f' : 'Фф',
    'ef' : 'Фф',
    'h' : 'Хх',
    'ch' : 'Хх',
    'ha' : 'Хх',
    'c' : 'Цц',
    'ce' : 'Цц',
    'cz' : 'Чч',
    'ć' : 'Чч',
    'ćie' : 'Чч',
    'cze' : 'Чч',
    'sz' : 'Шш',
    'sza' : 'Шш',
    'szcz' : 'Щщ',
    'szczy' : 'Щщ',
    'szyczy' : 'Щщ',
    'twardy znak' : 'Ъъ',
    'twardy' : 'Ъъ',
    'tz' : 'Ъъ',
    'y' : 'Ыы',
    'miekki znak' : 'Ьь',
    'miękki znak' : 'Ьь',
    'miękki' : 'Ьь',
    'miekki' : 'Ьь',
    'mz' : 'Ьь',
    'e' : 'Ээ',
    'ju' : 'Юю',
    'ja' : 'Яя'}

    print "Rosyjski odpowiednik: "
    print alphabet[letter]
    main(first=False)

if __name__ == "__main__":
    main(first=True)
