import random
digits = '0123456789'
lowercase_letters = 'abcdefghijklmnopqrstuvwxyz'
uppercase_letters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
punctuation = '!#$%&*+-=?@^_'
chars = ''

print('Сколько паролей нужно?')
amount = int(input())
print('Какая длина пароля?')
length = int(input())
print('Включать ли цифры 0123456789?; д = да, н = нет')
digit = input()
if digit == 'д':
    chars += digits

print('Включать ли прописные буквы ABCDEFGHIJKLMNOPQRSTUVWXYZ?; д = да, н = нет')
upper = input()
if upper == 'д':
    chars += uppercase_letters

print('Включать ли строчные буквы abcdefghijklmnopqrstuvwxyz?; д = да, н = нет')
lower = input()
if lower == 'д':
    chars += lowercase_letters

print('Включать ли символы !#$%&*+-=?@^_?; д = да, н = нет')
symbols = input()
if symbols == 'д':
    chars += punctuation

print('Исключать ли неоднозначные символы il1Lo0O?; д = да, н = нет')
similar_symbols = input()
if similar_symbols == 'д':
    for i in 'il1Lo0O':
        chars = chars.replace(i,'')


def generate_password(length, chars):
    password = ''
    for _ in range(amount):
        for _ in range(length):
            password += random.choice(chars)
        print(password, end='\n')
        password = ''


generate_password(length, chars)
