import random

def generate_key(word):
    key = ""
    for _ in range(len(word)):
        key += random.choice("0123456789abcdef") # Шестнадцатеричная систкма 
    return key

def en_de_crypt(text, key):
    new_text = ""
    for i in range(len(text)):
        new_text += chr(ord(text[i])^ord(key[i%len(key)]))
    return new_text

text_1 = 'Машина быстро проехала мимо парка'
text_2 = 'Кошка тихо спала на мягком диване'

key = generate_key(text_1)
en_text_1 = en_de_crypt(text_1, key)
de_text_1 = en_de_crypt(en_text_1, key)
en_text_2 = en_de_crypt(text_2, key)
de_text_2 = en_de_crypt(en_text_2, key)

print("Ключ -", key)
print("Текст 1","\nЗашифрованный текст -", en_text_1, "\nДешифрованный текст -", de_text_1)
print("Текст 2","\nЗашифрованный текст -", en_text_2, "\nДешифрованный текст -", de_text_2)