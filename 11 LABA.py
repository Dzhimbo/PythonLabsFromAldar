class Restaurant:
    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        self.rating = 0

    def open_restaurant(self):
        print("Ресторан открыт!")

    def describe_restaurant(self):
        print(
            f"Ресторан {self.restaurant_name} предлагает блюда {self.cuisine_type}. Этому ресторану присвоен рейтинг {self.rating}.")

    def update_rating(self, new_rating):
        self.rating = new_rating


new_restaurant = Restaurant("МамаНаДАЧЕ", "Домашняя")
print(new_restaurant.restaurant_name)
print(new_restaurant.cuisine_type)
new_restaurant.open_restaurant()
new_restaurant.describe_restaurant()
print('---------------------------------------------------------------')
restaurres1 = Restaurant("KFC", "Американская")
print(restaurres1.restaurant_name)
print(restaurres1.cuisine_type)
restaurres1.open_restaurant()
restaurres1.describe_restaurant()
print('---------------------------------------------------------------')
restaurres2 = Restaurant("Аха 'ЧитоГрито'", "Грузинская")
print(restaurres2.restaurant_name)
print(restaurres2.cuisine_type)
restaurres2.open_restaurant()
restaurres2.describe_restaurant()
print('---------------------------------------------------------------')
restaurres3 = Restaurant("Пиццерия 'Pizza_Tower'", "итальянская")
print(restaurres3.restaurant_name)
print(restaurres3.cuisine_type)
restaurres3.open_restaurant()
restaurres3.describe_restaurant()
print('---------------------------------------------------------------')

new_restaurant = float(input('Введите новый рейтинг для МамаНаДАЧЕ: '))
print('---------------------------------------------------------------')
new_rating1 = float(input('Введите новый рейтинг для KFC: '))
print('---------------------------------------------------------------')
new_rating2 = float(input('Введите новый рейтинг для ЧитоГрито: '))
print('---------------------------------------------------------------')
new_rating3 = float(input('Введите новый рейтинг для PizzaTower": '))
print('---------------------------------------------------------------')

restaurres1.update_rating(new_rating1)
restaurres2.update_rating(new_rating2)
restaurres3.update_rating(new_rating3)


restaurres1.describe_restaurant()
restaurres2.describe_restaurant()
restaurres3.describe_restaurant()

restaurres1.describe_restaurant()
restaurres2.describe_restaurant()
restaurres3.describe_restaurant()
