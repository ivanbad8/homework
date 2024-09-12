def custom_write(file_name, strings):
    strings_positions = {}
    file = open(file_name, 'a+')
    file.close()
    for string_ in strings:
        file = open(file_name, 'a', encoding='utf-8')
        numb_st = file.tell()
        file.close()
        file = open(file_name, 'a', encoding='utf-8')
        file.write(str(string_) + '\n')
        file.close()
        file = open(file_name, 'r', encoding='utf-8')
        text_line = file.readlines()
        file.close()
        numb_l = len(text_line)
        keys = (numb_l, numb_st)
        value = str(string_)
        strings_positions[keys] = value
    return strings_positions




info = ['Text for tell.', 'Используйте кодировку utf-8.'
    , 'Because there are 2 languages!', 'Спасибо!']

result = custom_write('test.txt', info)
print(result)
for elem in result.items():
    print(elem)


