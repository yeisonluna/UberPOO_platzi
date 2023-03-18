from car import Car

if __name__ == "__main__":
    print("Hola mundo")

    car = Car()
    car.license = "AMS432"
    car.driver = "Andrés Herrera"
    print(vars(car))

    car2 = Car()
    car2.license = "AQW342"
    car2.driver = "Martha Lopez"
    print(vars(car2))
    