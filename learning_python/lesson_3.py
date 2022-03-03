""" 1. Написать функцию num_translate(), переводящую числительные от 0 до 10 c английского на русский язык. Например:

>>> num_translate("one")
"один"
>>> num_translate("eight")
"восемь" """

def num_translate(num):
    print(english_nums.get(num.capitalize()))


english_nums = {"One": "Один", "Two": "Два", "Three": "Три", "Four": "Четыре", "Five": "Пять",
                "Six": "Шесть", "Seven": "Семь", "Eight": "Восемь", "Nine": "Девять", "Ten": "Десять"}

if __name__ == '__main__':
    while True:
        num = input("Программа переводящая числительные от 0 до 10 c английского на русский язык."
                " Введите число на английском для перевода на русский: ")
        num_translate(num)

"""Написать функцию thesaurus(), принимающую в качестве аргументов имена сотрудников и возвращающую словарь,
 в котором ключи — первые буквы имён, а значения — списки, содержащие имена, начинающиеся с соответствующей буквы. """


def thesaurus(*args):
    names_dict = {}
    for i in sorted(args):
        letter = i[0]
        if letter in names_dict:
            names_dict[letter] += [i]
        else:
            names_dict[letter] = [i]
    return

if __name__ == '__main__':
    print(thesaurus("Иван", "Мария", "Владимир", "Максим", "Илья", "Макар","Дмитрий"))


"""Написать функцию thesaurus_adv(), принимающую в качестве аргументов строки в формате «Имя Фамилия» и возвращающую словарь, 
в котором ключи — первые буквы фамилий, а значения — словари,
реализованные по схеме предыдущего задания и содержащие записи, в которых фамилия начинается с соответствующей буквы. """


def thesaurus_adv(*args):
    s_n_sort = {}
    for s_n in args:
        s_n_sort.setdefault(s_n.split()[1][0], {}).setdefault(s_n.split()[0][0], []).append(s_n)
    return s_n_sort

if __name__ == '__main__':
    print(thesaurus_adv("Иван Иванов", "Мария Габидуллина", "Владимир Путин", "Максим Захарян",
              "Илья Муромец", "Макар Великий","Дмитрий Медведев","Иван Сергеев", "Инна Серова",
              "Петр Алексеев", "Илья Иванов", "Анна Савельева"))



""" Реализовать функцию get_jokes(), возвращающую n шуток, сформированных из трех случайных слов, взятых из трёх списков (по одному из каждого):"""

from random import choice, randrange

nouns = ["автомобиль", "лес", "огонь", "город", "дом"]
adverbs = ["сегодня", "вчера", "завтра", "позавчера", "ночью"]
adjectives = ["веселый", "яркий", "зеленый", "утопичный", "мягкий"]

def some_jokes(n, repeat=False):

    no, adv, adj = nouns.copy(), adverbs.copy(), adjectives.copy()
    list_of_jokes = []
    list_min = min(no, adv, adj)

    while n and len(list_min):
        num = randrange(len(list_min))
        if repeat:
            list_of_jokes.append(f"{no.pop(num)} {adv.pop(num)} {adj.pop(num)}")
        else:
            list_of_jokes.append(f"{choice(nouns)} {choice(adverbs)} {choice(adjectives)}")
        n -= 1
    return list_of_jokes

if __name__ == '__main__':
    print(some_jokes(5, True))