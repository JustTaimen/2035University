word = input("Введите слово для проверки на палиндром").lower() # на всякий случай
revword = word[::-1]
if word == revword:
    print("это палиндром")
else:
    print("это не палиндром")