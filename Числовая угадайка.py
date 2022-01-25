def game():
    import random
    print('Добро пожаловать в числовую угадайку')
    print('Укажите максимально возможное число диапазона')
    maximum = int(input())
    print('Начинайте угадывать')
    x = random.randint(1, maximum)
    def is_valid(n):
        if 1 <= n <= maximum:
            return True
        else:
            return False
    counter = 0
    while x != True:
        n = int(input())
        counter += 1
        if is_valid(n) == False:
            print('А может быть все-таки введем целое число от 1 до', maximum, '?')
        elif n < x:
            print('Ваше число меньше загаданного, попробуйте еще разок')
        elif n > x:
            print('Ваше число больше загаданного, попробуйте еще разок')
        elif n == x:
            print('Вы угадали, поздравляем!')
            print('Число попыток:', counter)
            x = True
    print('Хотите сыграть еще раз? да = д, нет = н')
    text = input()
    if text == 'д':
        game()
    elif text == 'н':
        print('Спасибо, что играли в числовую угадайку. Еще увидимся...')
game()
