#Голубева Лидия Ильинична

# Задача-1:
class Car:

    def __init__(self, name, color):
        self._name = name
        self._color = color
        self._is_moving = False
        self._speed = 0
        self._is_police = False

    def get_color(self):
        return self._color

    def set_color(self, color):
        self._color = color

    def get_name(self):
        return self._name

    def get_speed(self):
        return self._speed

    def set_speed(self, speed):
        self._speed = speed

    def is_moving(self):
        return self._is_moving

    def is_police(self):
        return self._is_police

    def go(self):
        if not self._is_moving:
            print('{} Begins the movement.'.format(self._name))
            self._is_moving = True

    def stop(self):
        if self._is_moving:
            print('{} The car stops.'.format(self._name))
            self._is_moving = False

    def turn(self, direction):
        if not self._is_moving:
            return
        if direction.lower() == 't':
            print('{} The car turned.'.format(self._name))
        if direction.lower() == 'l':
            print('{} The car turns on the left.'.format(self._name))
        if direction.lower() == 'r':
            print('{} The car turns on the right.'.format(self._name))


class TownCar(Car):

    def __init__(self, name, color, capacity):
        super().__init__(name, color)
        self._speed = 70
        self._capacity = capacity

    def get_capacity(self):
        return self._capacity

    def set_is_police(self, is_police):
        self._is_police = bool(is_police)


class SportCar(Car):

    def __init__(self, name, color, engine_power):
        super().__init__(name, color)
        self._speed = 250
        self._engine_power = engine_power

    def get_engine_power(self):
        return self._engine_power

    def set_is_police(self, is_police):
        self._is_police = bool(is_police)


class WorkCar(Car):

    def __init__(self, name, color, load_capacity):
        super().__init__(name, color)
        self._speed = 60
        self._load_capacity = load_capacity

    def get_load_capacity(self):
        return self._load_capacity

    def load(self):
        print('{} The car is loaded.'.format(self._name))

    def unload(self):
        print('{} The car unloads.'.format(self._name))


class PoliceCar(Car):

    def __init__(self, name, color, police_station):
        super().__init__(name, color)
        self._is_police = True
        self._speed = 100
        self._police_station = police_station
        self._is_alarm = False

    def alarm_on(self):
        if not self._is_alarm:
            print('{} The car is switch on siren.'.format(self._name))
            self._is_alarm = True

    def alarm_off(self):
        if self._is_alarm:
            print('{} The car is swintch off siren.'.format(self._name))
            self._is_alarm = False

    def get_alarm(self):
        return self._is_alarm

    def get_police_station(self):
        return self._police_station


town_car = TownCar('Volkswagen', 'Black', '')
sport_car = SportCar('Ferrari', 'Red', '')
work_car = WorkCar('GAZelle', 'Dark blue', '')
police_car = PoliceCar('Reno', 'White', '')

cars = [town_car, sport_car, work_car, police_car]
for i in cars:
    i.go()
    i.turn('l')
    i.turn('t')
    i.stop()


print('The car :', police_car.get_name())
print('It is the police car :', police_car.is_police())
print('Colour :', police_car.get_color())
print('Police station :', police_car.get_police_station())
print('The maximum speed :', police_car.get_speed())

police_car.go()
police_car.turn('r')
police_car.alarm_on()
print('The car moves :', police_car.is_moving())
print('The siren works :', police_car.get_alarm())
police_car.stop()
police_car.alarm_off()
print('The car moves :', police_car.is_moving())
print('The siren works :', police_car.get_alarm())


