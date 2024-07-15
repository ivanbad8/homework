import random


def password(n):
    result = ""
    i = 1
    while i < n:
        j = i + 1
        while j <= n:
            if n % (i + j) == 0:
                result += str(i) + str(j)
            j += 1
        i += 1
    return result


numbers = [3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
n = random.choice(numbers)
passw = password(n)
print(f"Пароль для числа {n}: {passw}")