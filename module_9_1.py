def apply_all_func(int_list: (int,float), *functions):
    results = {}
    for key_ in functions:
        result_func = key_(int_list)
        results[key_.__name__] = result_func
    return results




print(apply_all_func([6, 20, 15, 9], max, min))
print(apply_all_func([6, 20, 15, 9], len, sum, sorted))

