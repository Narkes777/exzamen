# import random
# # ---Task 2---
# from tkinter.tix import InputOnly


# def main():
#     print("Добро пожаловать в игру: камень, ножницы, бумага!")
    
#     while True:
#         # Идет выбор игроком
#         player = input("Выбор хода: камень, ножницы, бумага: ")
#         # Идет выбор компьютера рандом
#         computer = random.choice(["камень", "ножницы", "бумага"])
        
#         print(f"Вы сделали выбор: {player}")
#         print(f"Компьютер сделал выбор: {computer}")

#         # Вывод результата
#         if player == computer:
#             print("Ничья!")
#         elif player == "камень" and computer == "ножницы" or\
#              player == "ножницы" and computer == "бумага" or\
#              player == "бумага" and computer == "камень":
#             print("Вы выйграли!")
#         else:
#             print("Выйграл компьютер!")
        
#         new_game = ("Хотите ли Вы сыграть снова? (да/нет): ")
#         if new_game != "да":
#             break
#     print("Спасибо за игру!")
# if __name__== "__main__":
#     main()
    
# ---Task 1---             
class Pizza():
    def __init__(self, name, dough, sauce, filling):
        self.name = name #Имя
        self.dough = dough #Тесто
        self.sauce = sauce #Соус
        self.filling = filling #Наполнение
    
    def prepare(self):
        #Метод подготовки пиццы
        print(f"Preparing {self.name} pizza: dough {self.dough}, sauce {self.sauce}, toppings {', '.join(self.toppings)}")
    
    def bake(self):
        #Метод выпечки
        print(f"Baking {self.name} pizza ")
        
        #Метод нарезки
    def cut(self):
        print(f"Cutting {self.name} pizza into pieces")

        #Метод упаковки
    def box(self):
        print(f"Packing {self.name} pizza")
        
#Подклассы для пицц
class Pepperoni(Pizza):
#Вызов родительского класса Pizza
    def __init__(self):
        super().__init__("Pepperoni Pizza", "Thin Crust", "Tomato Sauce", ["Pepperoni", "Cheese"])
    
class BBQ(Pizza):
#Вызов родительского класса Pizza
    def __init__(self):
        super().__init__("BBQ Pizza", "Thick Crust", "BBQ Sauce", ["Chicken", "Onions", "Cheese"])
    
class Seafood(Pizza):
#Вызов родительского класса Pizza
    def __init__(self):
        super().__init__("Seafood Pizza", "Regular Crust", "White Sauce", ["Shrimp", "Calamari", "Cheese"])
        
#Класс заказа
class Order:
    def __init__(self):
        #Cоздает список для хранения пицц
        self.pizzas = []

    def add_pizza(self, pizza):
        # Добавляет пиццу в заказ
        self.pizzas.append(pizza)

    def total_cost(self):
        # Подсчитывает стоимость заказа
        total = sum([10.0 for pizza in self.pizzas])
        return total

    def confirm_order(self):
        print("Заказ подтвержден!")

# Класс Терминал
class Terminal:
    def __init__(self):
        self.menu = {1: Pepperoni(), 2: BBQ(), 3: Seafood()}
        self.current_order = None

    def display_menu(self):
        # Отображает меню с пиццами
        print("Menu:")
        for number, pizza in self.menu.items():
            print(f"{number}. {pizza.name}")

    def start_new_order(self):
        self.current_order = Order()
        
    def take_order(self, pizza_number):
        if self.current_order:
            if pizza_number in self.menu:
                # Проверяем, существует ли выбранная пицца в меню.
                pizza = self.menu[pizza_number]
                # Получаем объект пиццы из меню.
                self.current_order.add_pizza(pizza)
                # Добавляем пиццу в текущий заказ.
                print(f"Добавлено {pizza.name} к заказу.")
            else:
                print("Неверный номер пиццы. Пожалуйста, выберите действительную пиццу.")
                # Если выбрана неверная пицца, выводим сообщение об ошибке.
        else:
            print("Заказ не выполняется. Пожалуйста, сначала начните новый заказ.")
    
    def finish_order(self):
        # Выводит информацию о заказе, общую стоимость и подтверждает заказ.
        if self.current_order:
            print("итог заказа:")
            for pizza in self.current_order.pizzas:
                print(f"- {pizza.name}")
            total_cost = self.current_order.total_cost()
            print(f"Общая стоимость: ${total_cost:.2f}")
            self.current_order.confirm_order()
        else:
            print("Заказ не выполняется. Пожалуйста, сначала начните новый заказ.")
            
                
            
        
            
        
        

    
    