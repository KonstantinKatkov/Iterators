# Задание
# Напишите класс-итератор EvenNumbers для перебора чётных чисел в определённом числовом диапазоне.
# При создании и инициализации объекта этого класса создаются атрибуты:
# start – начальное значение (если значение не передано, то 0)
# end – конечное значение (если значение не передано, то 1)
# Примечание
# Значение атрибута start всегда меньше значения атрибута end
# В решении задачи не использовать list, tuple и др. встроенные типы данных.

class EvenNumbers:

    def __init__(self, start = 0, end = 1):
        self.start = start
        self.end = end
        self.i = 0

    def __iter__(self):
        self.i = self.start - 1
        return self

    def __next__(self):

        self.i += 1
        if self.i > self.end:
            raise StopIteration()
        if self.i % 2 == 0:
            result = self.i

            return result


en = EvenNumbers(10, 25)
for value in en:
    if value is not None:
        print(value)




