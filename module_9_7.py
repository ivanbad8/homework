def is_prime(func):
    def wrapper(*args):
        result = func(*args)
        if result <= 1:
            is_prime_number = False
        else:
            is_prime_number = True
            for i in range(2, int(result ** 0.5) + 1):
                if result % i == 0:
                    is_prime_number = False
                    break
        if is_prime_number:
            print("Простое")
        else:
            print("Составное")
        return result

    return wrapper


@is_prime
def sum_three(*args):
    sum_ = sum(args)
    return sum_


result = sum_three(2, 3, 6)
print(result)
result = sum_three(2, 4, 5, 7)
print(result)
