""" 1. Написать функцию num_translate(), переводящую числительные от 0 до 10 c английского на русский язык. Например:

>>> num_translate("one")
"один"
>>> num_translate("eight")
"восемь" """

# def num_translate(num):
#     print(english_nums.get(num.capitalize()))
#
#
# english_nums = {"One": "Один", "Two": "Два", "Three": "Три", "Four": "Четыре", "Five": "Пять",
#                 "Six": "Шесть", "Seven": "Семь", "Eight": "Восемь", "Nine": "Девять", "Ten": "Десять"}
#
# if __name__ == '__main__':
#     while True:
#         num = input("Программа переводящая числительные от 0 до 10 c английского на русский язык."
#                 " Введите число на английском для перевода на русский: ")
#         num_translate(num)

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

thesaurus("Иван", "Мария", "Владимир", "Максим", "Илья", "Макар","Дмитрий")


