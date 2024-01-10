# class User:
#     count = 1
#
#     def __init__(self):
#         self.count = 7
#
# user = User()
#
#
# print(user.count)
# print(User.count)

# class User:
#     count = 1
#
#     __slots__ = ("name", "age")
#
#     def __init__(self, name, age):
#         self.name = 7
#         self.age = age
#
# user = User(name: 'max', age:15)
#
# print(User.name)
# print(user.name)
# user.status = True
# print(user.status)
# print(user.count)
# print(User.count)

# class User:
#     __cout =1
#     def __init__(self, name):
#         self.__name = name
#
#     def get_name(self):
#         print(self.__name)
#
# user = User('Max')
# # user.__get_name()
#
# print(user._User._name)
#  print(User._User.__count)



# class Car:
#
#     def __init__(self, brand):
#         self.brand = brand
#
# class Tools:
#
#     def greeting(self)
#          print('hello')
#
# class SuperCar(Car):
#     def __init__(self, brand, model):
#         super().__init__(brand)
#
#         self.model = model
# car.greeting()

# class User:
#
#     def __init__(self, name, age):
#         self._name = name
#         self.__age = age
#
#
#
#     def get_name(self):
#         return self.__name
#
#
#
#     def set_name(self, name):
#         self.__name = name
#
#     def __del_name(self):
#         del self.__name
#     name = property(fget=__get_name, fdel=__del_name)
#
#
# user = User(name: 'Max', age: 15)
#
# print(user.name)
# user.set_name('Karina')
# print(user.name)
# print(user.name)
#
# @property
# def name(self):
#     return self.__name
# @name.setter
# def name(self):
#     return self.__name
# @name.deleter
# def name(self):
#     return self.__name


from abc import ABC, abstractmethod

class Shape(ABC):
    @abstractmethod
    def perimeter(self):
        pass

    @abstractmethod
    def area(self):
        pass



# class Triangle(Shape)
#
#      def __init__(self, a, b):
#          self.a = a
#          self.b = b
#          self.c = c
#
#
#     def perimeter(self):
#         return self.b+self.a+self.c
#
#     def area(self):
#         return self.a*self.b*self.c
# #     def __init__(self, a):
# #         self.a = a
# #
# #
# # shape = Shape()
#
# shapes: list[Shape] = [
#     Triangle( a: 1, b: 2, c:3),
#
# ]
#
#
# for shape in shapes
#     print(shape.area())
#     print(shape.perimeter())


# class User:
#     __count = 0
#
#
#     @classmethod
#     def inc_count(cls):
#         User.count+=1
#         cls.__count+=1
#
#     @classmethod
#     def print_count(cls):
#         print(cls.__count)
#
#     @classmethod
#     def hello(self):
#         print('Hello World!')
#
# User.print_count()
# User.inc_count()
# User.print_count()
#
# user = User()
# user.hello()


 # class User:
 #     def __init__(self, name, age):
 #         self.name = name
 #         self.age = age
 #
 #     def __str__(self):
 #          return f'{self.mame} -- {self.age}'
 #
 # user = User(name:'max', age:15)
 # print(user.age)
 # print(user.name)
 # print(user +user2)


#  class User:
#      __intance = None
#      def __new__(cls, *args, **kwargs):
#          if not isinstance(cls.__intance, cls):
#              cls.__intance = super().__new__(cls)
#          return cls.__intance
#
#
#      def __init__(self, name):
#          self.name = name
#
#
# user1 = User('Max')
# user2 = User('Kira')
# user3 = User('Oleh')
#
# print(user1.name)
# print(user2.name)
# print(user3.name)




# class Array:
#
#     def __init__(self, *args):
#         self.__arr = [*args]
#
#
#     def __str__(self):
#          return str(self.__arr)
#
#     def __setiem__(self, key, value):
#         self



