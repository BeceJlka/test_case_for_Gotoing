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
    s = [i for i in input().lower().split()]
    book = {}
    text = []
    for i in s:
        if i in book:
            book[i] += 1
        else:
            book[i] = 1
    if len(book) < 3:
        return book.clear()
    else:
        for k in book.keys():
            text.append(k)
    return ' '.join(text[:3])
print(edit_text())