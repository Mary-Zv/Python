#4. Реализуйте базовый класс Car.
#у класса должны быть следующие атрибуты: speed, color, name, is_police (булево).
# А также методы: go, stop, turn(direction), которые должны сообщать, что машина поехала, остановилась, повернула (куда);
#опишите несколько дочерних классов: TownCar, SportCar, WorkCar, PoliceCar;
#добавьте в базовый класс метод show_speed, который должен показывать текущую скорость автомобиля;
#для классов TownCar и WorkCar переопределите метод show_speed.
# При значении скорости свыше 60 (TownCar) и 40 (WorkCar) должно выводиться сообщение о превышении скорости.
#Создайте экземпляры классов, передайте значения атрибутов. Выполните доступ к атрибутам, выведите результат.
# Вызовите методы и покажите результат.

class Car:

    def __init__(self, name, speed, color, is_police=False):
       self.speed = speed
       self.color = color
       self.name = name
       self.is_police = is_police

    def go(self):
        return f'{self.name} Едет!\n'

    def stop(self):
        return f'{self.name} стоИт\n'

    def turn(self, direction):
        return f'{self.name} повернула {direction}\n'

    def show_speed(self):
        return f'скорость - {self.speed}'


class TownCar(Car):
    def show_speed(self):
        if self.speed > 60:
            return f'\nАстановитес! {self.speed}'
        else:
            return f' {self.name} ехай дальше'

class SportCar(Car):
    pass

class WorkCar(Car):
    def show_speed(self):
        if self.speed > 40:
            return f'\nАстановитес! {self.speed}'
        else:
            return f' {self.name} ехай дальше'

class Police(Car):
    pass

town = TownCar('BMW', 80, 'black', False)
print(town.go(), town.show_speed(), town.turn('налево'), town.stop())

sport = SportCar('VAZ', 52, 'natural', False)
print(sport.go(), sport.show_speed(), sport.turn('направо'), sport.stop())

work = WorkCar('Volvo', 97, 'green', False)
print(work.go(), work.show_speed(), work.turn('никуда'), work.stop())