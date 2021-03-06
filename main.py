def encrypt(text, n):
    text1 = [] 
    text2 = []
    for i in text[1::2]: ### Записываем все нечетные числа
        text1.append(i)
    for u in text[::2]: ### Записываем все четные числа
        text2.append(u)
    if n <= 0:
        return ''.join(text) ### Возвращаем условие если n меньше или равно нулю
    else:
        for i in range(n): ### Производим итерации над текстом пока n не закончится
            if n == 1: ### Если n равно еденице то склеиваем наши числа и выводим результат
                text3 = text1 + text2
                return ''.join(text3)
            elif n >= 1: ### Если n больше чем еденица то склеиваем наши числа и заного запускаем функцию пока n не станет равно единице
                text3 = text1 + text2
                n = n - 1
                return encrypt(text3, n)
            else: ### В остальных случаях вернуть исходные данные
                return ''.join(text)


def decrypt(encrypted_text, n):
    text = []
    encrypted_text1 = []
    encrypted_text2 = []
    encrypted_text3 = []
    for y in encrypted_text: ### разбиваем входящую строку на символы
        text.append(y)
    if n <= 0: ### если символов ноль или меньше возвращаем исходную строку
        return ''.join(encrypted_text)
    else: 
        for i in range(n): 
            if n == 1:
                i = round(len(text) / 2)  ### разбиваем список пополам и находим наше первое число с которого начнем считать.
                for y in range(i):
                    encrypted_text1.append(text[y]) ### находим все четные числа
                for u in range(len(text))[i:]:
                    encrypted_text2.append(text[u]) ### находим все нечетные числа
                for t in range(len(text) // 2):
                    encrypted_text3.append(encrypted_text2[t]) ### добавляем по очередности нечетные числа
                    encrypted_text3.append(encrypted_text1[t]) ### а тут четные числа
                return ''.join(encrypted_text3) ### возвращаем результат
            elif n >= 1: ### если n больше еденици повторяем пока не станет 1
                i = round(len(text) / 2)  
                for y in range(i):
                    encrypted_text1.append(text[y])
                for u in range(len(text))[i:]:
                    encrypted_text2.append(text[u])
                for t in range(len(text) // 2):
                    encrypted_text3.append(encrypted_text2[t])
                    encrypted_text3.append(encrypted_text1[t])
                n = n - 1
                return decrypt(encrypted_text3, n)
            else:
                return ''.join(encrypted_text) ### В остальных случаях вернуть исходные данные


def edit_text():
    s = [i for i in input().lower().split()] ### Вводим нужный нам текст, разбиваем его по пробельному символу, приводим в нижний регистр.
    words = {} 
    text = []
    for i in s: ### Записываем все слова в словарь
        if i in words:
            words[i] += 1
        else:
            words[i] = 1
    if len(words) < 3: ### Проверяем на количество записаных слов в словаре, если меньше трех возвращаем пустой
        return words.clear()
    else:
        sorted_by_value =  sorted(words.items(), key=lambda x: x[1]) ### Сортируем словарь по величине значений
        a = sorted_by_value[-1] ### Создаем кортеж из максимальных трех значений
        b = sorted_by_value[-2]
        c = sorted_by_value[-3]          
    return a[0],b[0],c[0] ### Возвращаем ключи без количества повторений.
print(edit_text()) ### Тестируем результат
