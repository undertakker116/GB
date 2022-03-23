def odd_num(num):
    for i in range(1, num + 1, 2):
        yield i

def odd_next_num(num):
    nums = (x for x in range(1, num + 1, 2))
    return nums

def print_screen_generator(nums):
    elements = 0
    for elem in odd_next_num(nums):
        elements += 1
        print(f'{elements} число последовательности - {elem}')

def main():
    num = int(input("Введите число: "))
    generator_num_1 = odd_num(num)
    generator_num_2 = odd_next_num(num)
    print_screen_generator(nums=num)

    print(type(f'"generator_num_1": {generator_num_1}'))
    print(type(f'"generator_num_2": {generator_num_2}'))

if __name__ == '__main__':
    main()

