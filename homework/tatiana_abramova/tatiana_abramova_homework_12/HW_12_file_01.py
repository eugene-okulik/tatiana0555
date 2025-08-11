class Flowers:
    def __init__(self, name, color, stem_length, price, lifespan):
        self.name = name
        self.color = color
        self.stem_length = stem_length
        self.price = price
        self.lifespan = lifespan

    def __str__(self):
        return f"{self.name} ({self.color}) - Стебель: {self.stem_length} см, Цена: {self.price} руб.," \
               f" Жизнь: {self.lifespan} дн."


class Rose(Flowers):
    def __init__(self, stem_length, price):
        super().__init__("Роза", "Красный", stem_length, price, lifespan=7)


class Tulip(Flowers):
    def __init__(self, stem_length, price):
        super().__init__("Тюльпан", "Желтый", stem_length, price, lifespan=5)


class Aster(Flowers):
    def __init__(self, stem_length, price):
        super().__init__("Астра", "Белый", stem_length, price, lifespan=10)


class Bouquet:
    def __init__(self):
        self.flowers = []

    def add_flowers(self, flowers_to_add):
        self.flowers.append(flowers_to_add)

    def total_price(self):
        return sum(flower.price for flower in self.flowers)

    def average_lifespan(self):
        if not self.flowers:
            return 0
        return sum(flower.lifespan for flower in self.flowers) / len(self.flowers)

    def sort_flowers(self, key):
        self.flowers.sort(key=key)

    def find_flowers_by_lifespan(self, min_lifespan):
        return [flower for flower in self.flowers if flower.lifespan >= min_lifespan]

    def __str__(self):
        bouquet_str = "Букет состоит из:\n"
        bouquet_str += "\n".join(str(flower) for flower in self.flowers)
        bouquet_str += f"\nОбщая стоимость букета: {self.total_price()} руб."
        bouquet_str += f"\nСреднее время жизни цветов в букете: {self.average_lifespan():.2f} дн."
        return bouquet_str


bouquet = Bouquet()


rose1 = Rose(stem_length=50, price=100)
tulip1 = Tulip(stem_length=30, price=70)
aster1 = Aster(stem_length=35, price=50)

bouquet.add_flowers(rose1)
bouquet.add_flowers(tulip1)
bouquet.add_flowers(aster1)

print(bouquet)

bouquet.sort_flowers(key=lambda flower: flower.price)
print("\nПосле сортировки по цене:")
print(bouquet)

long_living_flowers = bouquet.find_flowers_by_lifespan(min_lifespan=6)
print("\nЦветы с временем жизни больше 6 дней:")
for flower in long_living_flowers:
    print(flower)
