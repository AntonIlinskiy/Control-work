# class Cat:
#     def __init__(self, name):
#         self.name = name
#
#     def meow(self):
#         print(f"{self.name}: Мяу!")
#
#
# cat = Cat("Барсик")
# cat2 = Cat("Мурзик")
# cat.meow()
# cat2.meow()


# class Student:
#     def __init__(self, full_name, age, course):
#         self.full_name = full_name
#         self.age = age
#         self.course = course
#
#     def info(self):
#         return f"{self.full_name}: {self.age} лет, {self.course} курс."
#
#
# sasha = Student("Александр", 20, 3)
# print(sasha.info())


class Field:
    def __init__(self):
        self.field = [' '] * 9

    def _check(self, index):
        return self.field[index] == ' '

    def turn(self, index, symbol):
         if self._check(index):
            self.field[index] = symbol

    def print(self):
        print(self.field[:3])
        print(self.field[3:6])
        print(self.field[6:])
        print()


field = Field()
field.print()
field.turn(3, 'X')
field.print()
field.turn(3, 'O')
field.print()
