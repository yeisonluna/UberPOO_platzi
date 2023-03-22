from car import Car
from account import Account

if __name__ == "__main__":
    print("Hola mundo")

    car = Car("AMS432", Account("Andrés Herrera", "AND453"))
    print(vars(car))
    print(vars(car.driver))
    