# 12.1
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


# 12.2
class IceCreamStand(Restaurant):
    def __init__(self, restaurant_name, cuisine_type, flavors):
        super().__init__(restaurant_name, cuisine_type)
        self.flavors = flavors

    def show_flavors(self):
        print(f"Список доступных вкусов: {', '.join(self.flavors)}")

    def add_flavor(self, new_flavor):
        if new_flavor not in self.flavors:
            self.flavors.append(new_flavor)
            print(f"Вкус '{new_flavor}' был добавлен в список.")
        else:
            print(f"Вкус '{new_flavor}' уже есть в списке.")

    def remove_flavor(self, flavor_to_remove):
        if flavor_to_remove in self.flavors:
            self.flavors.remove(flavor_to_remove)
            print(f"Вкус '{flavor_to_remove}' был удален из списка.")
        else:
            print(f"Вкус '{flavor_to_remove}' нет в списке.")

    def check_flavor(self, flavor_to_check):
        if flavor_to_check in self.flavors:
            print(f"Вкус '{flavor_to_check}' есть в списке.")
        else:
            print(f"Вкус '{flavor_to_check}' нет в списке.")


class IceCreamStick(IceCreamStand):
    def add_stick_ice_cream(self):
        print("Добавили мороженое на палочке.")


class SoftIceCream(IceCreamStand):
    def add_soft_ice_cream(self):
        print("Добавили мягкое мороженое.")


class IceCreamInCone(IceCreamStand):
    def add_ice_cream_in_cone(self):
        print("Добавили мороженое в рожок.")


ice_cream_stand = IceCreamStand("Мороженное на углу", "мороженое", ["ванильное", "шоколадное"])
ice_cream_stand.show_flavors()

ice_cream_stand.add_flavor("клубничное")
ice_cream_stand.add_flavor("ванильное")

ice_cream_stand.show_flavors()

ice_cream_stand.remove_flavor("шоколадное")
ice_cream_stand.check_flavor("ванильное")

ice_cream_stick = IceCreamStick("Мороженное на палочке", "мороженое на палочке", ["ванильное", "шоколадное"])
ice_cream_stick.add_stick_ice_cream()

soft_ice_cream = SoftIceCream("Мягкое мороженое", "мягкое мороженое", ["ванильное", "шоколадное"])
soft_ice_cream.add_soft_ice_cream()

ice_cream_in_cone = IceCreamInCone("Мороженое в рожке", "мороженое в рожке", ["ванильное", "шоколадное"])
ice_cream_in_cone.add_ice_cream_in_cone()

# 12.3
from tkinter import *

class IceCreamMenu:
    def __init__(self):
        self.root = Tk()
        self.root.title("Меню кафе-мороженного")
        self.root.geometry("400x300")
        self.photo = PhotoImage(file="ice.png")
        self.root.iconphoto(False, self.photo)
        background_color = "#E6E6FA"
        self.root.config(bg=background_color)

        # Создание объектов шрифтов
        flavor_font = ("Arial", 12, "bold")
        type_font = ("Arial", 10, "italic")

        self.flavors = ["ванильное", "шоколадное", "клубничное", "банановое"]
        self.types = ["на палочке", "мягкое", "в рожке"]

        self.flavor_label = Label(self.root, text="Выберите вкус:", font=flavor_font, fg="blue", bg=background_color)
        self.flavor_label.pack()

        self.flavor_var = StringVar()
        self.flavor_var.set(self.flavors[0])
        self.flavor_dropdown = OptionMenu(self.root, self.flavor_var, *self.flavors)
        self.flavor_dropdown.pack()

        self.type_label = Label(self.root, text="Выберите тип:", font=type_font, fg="blue", bg=background_color)
        self.type_label.pack()

        self.type_var = StringVar()
        self.type_var.set(self.types[0])
        self.type_dropdown = OptionMenu(self.root, self.type_var, *self.types)
        self.type_dropdown.pack()

        self.add_flavor_button = Button(self.root, text="Добавить вкус", command=self.add_flavor, fg="green", bg=background_color)
        self.add_flavor_button.pack()

        self.add_type_button = Button(self.root, text="Добавить тип", command=self.add_type, fg="green", bg=background_color)
        self.add_type_button.pack()

        self.remove_flavor_button = Button(self.root, text="Удалить вкус", command=self.remove_flavor, fg="red", bg=background_color)
        self.remove_flavor_button.pack()

        self.remove_type_button = Button(self.root, text="Удалить тип", command=self.remove_type, fg="red", bg=background_color)
        self.remove_type_button.pack()

        self.show_button = Button(self.root, text="Показать вкусы и типы", command=self.show_flavors, fg="purple", bg=background_color)
        self.show_button.pack()

        self.exit_button = Button(self.root, text="Выход", command=self.root.quit, fg="white", bg="#808080")
        self.exit_button.pack(side="bottom", expand=10, pady=5)
        self.root.mainloop()

    def add_flavor(self):
        new_flavor = self.flavor_var.get()
        if new_flavor not in self.flavors:
            self.flavors.append(new_flavor)
            print(f"Вкус '{new_flavor}' был добавлен в список.")
        else:
            print(f"Вкус '{new_flavor}' уже есть в списке.")

    def remove_flavor(self):
        flavor_to_remove = self.flavor_var.get()
        if flavor_to_remove in self.flavors:
            self.flavors.remove(flavor_to_remove)
            print(f"Вкус '{flavor_to_remove}' был удален из списка.")
        else:
            print(f"Вкус '{flavor_to_remove}' нет в списке.")

    def add_type(self):
        new_type = self.type_var.get()
        if new_type not in self.types:
            self.types.append(new_type)
            print(f"Тип мороженого '{new_type}' был добавлен в список.")
        else:
            print(f"Тип мороженого '{new_type}' уже есть в списке.")

    def remove_type(self):
        type_to_remove = self.type_var.get()
        if type_to_remove in self.types:
            self.types.remove(type_to_remove)
            print(f"Тип мороженого '{type_to_remove}' был удален из списка.")
        else:
            print(f"Тип мороженого '{type_to_remove}' нет в списке.")

    def show_flavors(self):
        print(f"Список доступных вкусов: {', '.join(self.flavors)}")
        print(f"Список доступных типов мороженого: {', '.join(self.types)}")

menu = IceCreamMenu()
