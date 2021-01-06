def encrypt(text, n):
    text1 = []
    text2 = []
    for i in text[1::2]:
        text1.append(i)
    for u in text[::2]:
        text2.append(u)
    if n <= 0:
        return ''.join(text)
    else:
        for i in range(n):
            if n == 1:
                text3 = text1 + text2
                return ''.join(text3)
            elif n >= 1:
                text3 = text1 + text2
                n = n - 1
                return encrypt(text3, n)
            else:
                return ''.join(text)


def decrypt(encrypted_text, n):
    text = []
    encrypted_text1 = []
    encrypted_text2 = []
    encrypted_text3 = []
    for y in encrypted_text:
        text.append(y)
    if n <= 0:
        return ''.join(encrypted_text)
    else:
        for i in range(n):
            if n == 1:
                i = round(len(text) / 2)  # 4
                for y in range(i):
                    encrypted_text1.append(text[y])
                for u in range(len(text))[i:]:
                    encrypted_text2.append(text[u])
                for t in range(len(text) // 2):
                    encrypted_text3.append(encrypted_text2[t])
                    encrypted_text3.append(encrypted_text1[t])
                return ''.join(encrypted_text3)
            elif n >= 1:
                i = round(len(text) / 2)  # 4
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
                return ''.join(encrypted_text)


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
        max_words = max(words.values())  ### Находим максимальное значение повторяющегося слова
        while len(text) < 3: ### Цикл для составления списка самых популярных слов
            if len(text) == 0: ### Если список пуст, добавляем одно или два(если значения равные) ключа(слова)
                for k, v in words.items(): 
                    if v == max_words:
                        text.append(k)
                max_words-=1
            elif len(text) <= 2: ### Если в списке меньше двух слов, добавляем третье, меньшее по значению на 1
                for k, v in words.items():
                    if v == max_words:
                        text.append(k)
                max_words-=1        
            else: ### если в списке все еще меньше трех слов добавляем еще одно уже меньшее по значению на два.
                for k, v in words.items():
                    if v == max_words:
                        text.append(k)    
        return ",".join(text[:3]) ### Выводим список слов через запятую, ограничивая количество выведеных слов, ведь их могло получится больше трех.
print(edit_text()) ### Тестируем результат
