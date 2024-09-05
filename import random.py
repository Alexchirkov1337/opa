import random
import string

print('Добро пожаловать в генератор паролей!')

length = (int(input('введите длинну пароля ')))

lower = string.ascii_lowercase
upper = string.ascii_uppercase
num = string.digits
symbols = string.punctuation

data = lower + upper + num + symbols

prepass = random.sample(data, length)

password = "".join(prepass)

print(password)