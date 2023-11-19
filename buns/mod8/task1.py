class Transport:
    def __init__(self, coordinates, speed, brand, year, number):
        self._coordinates = coordinates
        self._speed = speed
        self._brand = brand
        self._year = year
        self._number = number

    @property
    def coordinates(self):
        return self._coordinates

    @coordinates.setter
    def coordinates(self, coordinates):
        self._coordinates = coordinates

    @property
    def speed(self):
        return self._speed

    @speed.setter
    def speed(self, speed):
        self._speed = speed

    @property
    def brand(self):
        return self._brand

    @brand.setter
    def brand(self, brand):
        self._brand = brand

    @property
    def year(self):
        return self._year

    @year.setter
    def year(self, year):
        self._year = year

    @property
    def number(self):
        return self._number

    @number.setter
    def number(self, number):
        self._number = number

    def __str__(self):
        return f"Transport: {self._brand} {self._number}"

    def isInArea(self, pos_x, pos_y, length, width) -> bool:
        return pos_x <= self._coordinates[0] <= pos_x + length and pos_y <= self._coordinates[1] <= pos_y + width


class Passenger:
    @property
    def passengers_capacity(self):
        return self._passengers_capacity

    @passengers_capacity.setter
    def passengers_capacity(self, passengers_capacity):
        self._passengers_capacity = passengers_capacity

    @property
    def number_of_passengers(self):
        return self._number_of_passengers

    @number_of_passengers.setter
    def number_of_passengers(self, number_of_passengers):
        self._number_of_passengers = number_of_passengers


class Cargo:
    @property
    def carrying(self):
        return self._carrying

    @carrying.setter
    def carrying(self, carrying):
        self._carrying = carrying


class Plane(Transport):
    def __init__(self, coordinates, speed, brand, year, number, height):
        super().__init__(coordinates, speed, brand, year, number)
        self._height = height

    @property
    def height(self):
        return self._height

    @height.setter
    def height(self, height):
        self._height = height


class Ship(Transport):
    def __init__(self, coordinates, speed, brand, year, number, port):
        super().__init__(coordinates, speed, brand, year, number)
        self._port = port

    @property
    def port(self):
        return self._port

    @port.setter
    def port(self, port):
        self._port = port


class Auto(Transport):
    def __init__(self, coordinates, speed, brand, year, number, fuel_type):
        super().__init__(coordinates, speed, brand, year, number)
        self._fuel_type = fuel_type

    @property
    def fuel_type(self):
        return self._fuel_type

    @fuel_type.setter
    def fuel_type(self, fuel_type):
        self._fuel_type = fuel_type


class Car(Auto, Passenger):
    def __init__(self, coordinates, speed, brand, year, number, fuel_type, passengers_capacity):
        super().__init__(coordinates, speed, brand, year, number, fuel_type)
        self._passengers_capacity = passengers_capacity


class Bus(Auto, Passenger):
    def __init__(self, coordinates, speed, brand, year, number, fuel_type, passengers_capacity, number_of_passengers):
        super().__init__(coordinates, speed, brand, year, number, fuel_type)
        self._passengers_capacity = passengers_capacity
        self._number_of_passengers = number_of_passengers


class CargoAuto(Auto, Cargo):
    def __init__(self, coordinates, speed, brand, year, number, fuel_type, carrying):
        super().__init__(coordinates, speed, brand, year, number, fuel_type)
        self._carrying = carrying


class Boat(Ship):
    def __init__(self, coordinates, speed, brand, year, number, port, engine_type):
        super().__init__(coordinates, speed, brand, year, number)
        self._port = port
        self._engine_type = engine_type

    @property
    def engine_type(self):
        return self._engine_type

    @engine_type.setter
    def engine_type(self, engine_type):
        self._engine_type = engine_type


class PassengerShip(Ship, Passenger):
    def __init__(self, coordinates, speed, brand, year, number, port, passengers_capacity, number_of_passengers):
        super().__init__(coordinates, speed, brand, year, number)
        self._port = port
        self._passengers_capacity = passengers_capacity
        self._number_of_passengers = number_of_passengers


class CargoShip(Ship, Cargo):
    def __init__(self, coordinates, speed, brand, year, number, port, carrying):
        super().__init__(coordinates, speed, brand, year, number)
        self._port = port
        self._carrying = carrying


class Seaplane(Plane, Ship):
    def __init__(self, coordinates, speed, brand, year, number, height, port):
        super().__init__(coordinates, speed, brand, year, number)
        self._height = height
        self._port = port