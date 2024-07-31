from random import randint

def play_game():
    number = randint(1, 100) # Мы генерируем число от 1 до 100
    print("Добро пожаловать в числовую угадайку")
    cnt = 0 # Количество попыток отгадывания

    # Функция корректности введенных данных
    def is_invalid(arg):
        if arg.isdigit(): # Если значение состоит только из чисел, то прододолжаем работу кода
            if 1 <= int(arg) <= 100:
                return True
            else:
                return False
        else:
            return False

    # Основной цикл
    while True:
        arg = input("Введите число от 1 до 100: ")
        if is_invalid(arg):
            guess = int(arg) # Преобразуем к целому числу
            if guess < number:
                print("Ваше число меньше загаданного, попробуйте еще разок")
                cnt += 1
            elif guess > number:
                print("Ваше число больше загаданного, попробуйте еще разок")
                cnt += 1
            else:
                print("Вы угадали, поздравляем!")
                print("Количество попыток отгадывания:", cnt)
                print("Спасибо, что играли в числовую угадайку. Еще увидимся...")
                break
        else:
            print("А может быть все-таки введем целое число от 1 до 100?")
while True:
    play_game()
    play_new_game = input("Желаете сыграть ещё раз? (Да/Нет) ")
    if play_new_game != "Да":
        print("Спасибо за игру. Ещё увидимся:)")
        break