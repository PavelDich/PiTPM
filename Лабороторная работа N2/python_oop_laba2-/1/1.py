class Car:
    color = "Red"
    fuel = 100
    brand = "Lada"

    def go(self):
        pass

    def turn(self):
        pass

    def stop(self):
        pass

    def info(self):
        print(Car.color, Car.fuel, Car.brand)

    class Driver:
        def __init__(self):
            pass

        name = "Nikita"
        surname = "Svetli"
        age = "21"

        def info(self):
            print(driver.name, driver.surname, driver.age)


myCar = Car()
myCar.go()
myCar.turn()
myCar.stop()
myCar.info()
driver = Car.Driver()
driver.info()
