from threading import Thread, Lock
from random import randint
from time import sleep


class Bank:

    def __init__(self):
        self.balance = 0
        self.lock = Lock()

    def deposit(self):
        for _ in range(100):
            rand_ = randint(50, 500)  # Генерация случайной суммы пополнения
            self.lock.acquire()
            self.balance += rand_
            print(f'Пополнение: {rand_}. Баланс: {self.balance}')
            if self.balance >= 500 and self.lock.locked():
                self.lock.release()
                sleep(0.001)

    def take(self):
        for i in range(100):
            rand_1 = randint(50, 500)
            print(f'Запрос на {rand_1}.')
            if self.balance >= rand_1:
                self.balance -= rand_1
                print(f'Снятие: {rand_1}. Баланс: {self.balance}')
            else:
                print('Запрос отклонен не достаточно средств.')
                self.lock.acquire()
                sleep(0.001)


bk = Bank()

th1 = Thread(target=Bank.deposit, args=(bk,))
th2 = Thread(target=Bank.take, args=(bk,))

th1.start()
th2.start()
th1.join()
th2.join()
print(f'Итоговый баланс: {bk.balance}')
