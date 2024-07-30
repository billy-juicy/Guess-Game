from random import randint

number = randint(1, 100) # Мы генерируем число от 1 до 100
print("Добро пожаловать в числовую угадайку")

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
        elif guess > number:
            print("Ваше число больше загаданного, попробуйте еще разок")
        else:
            print("Вы угадали, поздравляем!")
            print("Спасибо, что играли в числовую угадайку. Еще увидимся...")
    else:
        print("А может быть все-таки введем целое число от 1 до 100?")