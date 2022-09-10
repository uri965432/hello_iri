# class Car:
#     pass
# car_object = Car()
# print(dir(Car))



class Car:

    default_color = 'Grey'
    default_weight = 5000

    def __init__(self, color, model):
        self.color = color
        self.model = model

    def turn_on(self):
        pass

    def ride(self):
        pass
car_object = Car()

