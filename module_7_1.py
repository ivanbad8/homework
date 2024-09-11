class Product:
    def __init__(self, name: str, weight: float, category: str):
        self.name = name
        self.weight = weight
        self.category = category

    def __str__(self):
        return (f'{self.name}; {self.weight}; {self.category}')


class Shop:
    def __init__(self):
        self.__file_name = 'products.txt'
        file = open(self.__file_name, 'a+')
        file.close()

    def get_products(self):
        self.__file_name = 'products.txt'
        file = open(self.__file_name, 'r')
        products = file.read()
        file.close()
        return products

    def add(self, *products):
        self.__file_name = 'products.txt'
        file = open(self.__file_name, 'r')
        prod = file.read()
        file.close()
        for product in products:
            if str(product) not in prod:
                file = open(self.__file_name, 'a')
                file.writelines(str(product) + '\n')

            if str(product) in prod:
                print(f'Продукт {str(product)} уже есть в магазине')
        file.close()


s1 = Shop()
p1 = Product('Potato', 50.5, 'Vegitables')
p2 = Product('Spaghetti', 3.4, 'Groceries')
p3 = Product('Potato', 5.5, 'Vegetables')
print(p2)
s1.add(p1, p2, p3)

print(s1.get_products())
