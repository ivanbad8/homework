import requests  # модуль для выполнения HTTP-запросов
import numpy as np  # математические операции
from PIL import Image, ImageFilter  # для работы с изображением
import sys
from time import sleep
import os


response = requests.get('https://www.yandex.ru')
print(response.status_code) #200 — «OK». Запрос прошёл успешно, и мы получили ответ
print(response.text)
print(response.headers)
print('numpy ---------------------------------------------------------------------')
num_ = [1,2,'3','4',5,6]
num = np.array(num_,'int')
print(num)
print(num.sum(),num.mean(), num.max(), num.min())#сумма, среднее, максимальное.
print(np.argmax(num), np.argmin(num)) #индекс максимального и минимвльного значения
print(num > 5)


url = 'https://python-scripts.com/wp-content/uploads/2019/12/image-pillow.png'
resp = requests.get(url, stream=True).raw
image = Image.open(resp)
image.save('медуза.png', 'png')
sleep(2)
image.show()
sleep(2)
current_directory = os.getcwd()
name = 'медуза.png'
image_path = os.path.join(current_directory, name)
image = Image.open(image_path)
if image.mode != 'RGB':
    image = image.convert('RGB')
image = image.filter(ImageFilter.EMBOSS)
image.save(image_path)
image.show()
