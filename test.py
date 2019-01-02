import random

count = round(random.random() * 25)
stri = 'ж'
r = range(count)
print(r)
for number in range(count):
    if random.random() < 0.5:
        stri += 'ж'
    else:
        stri += 'Ж'

print(stri)
