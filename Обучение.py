# Оператор WHILE создает условие в цикле
# i = 5
#while i < 15:
    #print(i)
   # i += 1
# Списки данных (представляются квадратными скобками)= []
#Пример: nums = [5, 7, 2, 3]
#print(nums)
# find = позволяет найти определенные символы
# split = разбить строку по определенному символу
# Кортежи (используют для передачи данных) для них используются круглые скобки ()
#data = (4, 5, 6, 7, 6, True, "Hello")
#print(data[1:7]) # Срезы (:) Работают по индексу
# в Кортежах используются функии: count(показывает кол-во элементов) и len(общий подсчет всех элементов)
# data = (5, 6, 7, 8)
# for el in data:
    #print(el)
# Преобразование кортежей в список tuple
#nums = [5, 6, 7]
#new_nums = tuple(nums)
#print(new_nums)
                          # Словари и их функции. Для них используются фигурные скобки {}
#country = {4, 3}
#print(country[4])
#country = {'code': 'RU', 'name': 'Russian', 'population': 144}
#print(country['name'])
# функция dict(dictionary)
#country = dict(code='RU', name='Russian', population=144)
                        # Функции (def, lambda) Позволяют сократить повторяющийся код
            # Создание функции
#def summa(a, b):
    #res = a + b
  #  print("Result:", res)
#summa(5, 7)
#summa("N", "o")
                         # Обработчик исключений (try и except) try-создает обработчика except-отслеживает ошибку 
 #x = 1
 #while x == 1:
    #try:
       # x = int(input("Введите число: "))
       # print(x)
   # except ValueError:
      #  print("Введите именно число!")
                                               # Модули
    #  Встроенные модули
#import datetime as dt    Встр модуль datetime показывает дату и время
#print(dt.datetime.now())  as - это оператор как переименовование
                         # ОПП (Объектно-ориентированное программирование)
#class Cat:
    #name = None               За счет класса мы можем описать общие характеристики в одном месте          В них также можно использовать функции, списки, кортежи и тд
    #age = None                     После этого мы можем добавить объекты и внести нужные нам значения
    #isHappy = None
#cat1 = Cat()
#cat1.name = "Микки"
#cat1.age = 3
#cat1.isHappy = True
#cat2 = Cat()
#cat2.name = "Эрика"
#cat2.age = 13
#cat2.isHappy = False
#print("Я люблю вас:", end="")
#print(cat1.name, cat2.name, sep=",")
                                               # Кострукторы для работы в классах! Упрощают сам код
                                               # __init__ = создание конструктора
#class Cat:
    #name = None
    #age = None
    #isHappy = None
    #def __init__(self,name, age, isHappy ):
#cat1 = Cat("Микки", 3, True)

#cat2 = Cat("Эрика", 13, False)

#print("Я люблю вас:", end="")
#print(cat1.name, cat2.name, sep=",")
                                             # Наследование, полиморфизм, инкапсуляция

#class Building:
    #year = None
   # city = None

    #def __init__(self, year, city):
        #self.year = year
        ##def get_info(self):
        #print("Year: ", self.year, ".City:", self.city)

#class school(Building):                                       #Здесь идет наследие класса Building и передается классу школе
    #pass

#school = school(2000, "Moscow")
#school.get_info()
#house = Building(2000, "Moscow")
#shop = Building(2000, "Moscow")
                                             #Полиморфизм - это возможность объектов разных классов реагировать на одно и то же сообщение по-разному.
                                             # например мы хотим добавить в подкласс школу учеников, тогда;
                                    # class school(Building):
                                    # pupils=100
                                    # def__init__(self, pupils, year,city)
                                          #self.pupils=pupils 


                                         # Декораторы функций (Нужны для того чтобы к функции добавить доп функции)



#import webbrowser

#def validator(func):                   # Чтобы создать декоратор, нужны вложенные функции
    #def wrapper(url):                     # Внутри вложенной функции еще одну вложенную функцию и прописываем условия
        #if "." in url:
            #func(url)
        #else:
            #print("Введен неверный  URL")





    #return wrapper

#@validator                        # @ нужна чтобы указать, что используется декоратор
#def open_url(url):
    #webbrowser.open(url)





