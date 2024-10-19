import datetime
from multiprocessing import Pool


# Функция для чтения содержимого файла
def read_info(name):
    all_data = []
    with open(name, 'r') as file:
        for line in file.readline():
            all_data.append(line)


filenames = [f'file {number}.txt' for number in range(1, 5)]

start = datetime.datetime.now()
for filename in filenames:
    read_info(filename)

end = datetime.datetime.now()
print(end - start)

if __name__ == '__main__':
    start = datetime.datetime.now()
    with Pool(processes=len(filenames)) as pool:
        pool.map(read_info, filenames)
    end = datetime.datetime.now()
    print(end - start)
