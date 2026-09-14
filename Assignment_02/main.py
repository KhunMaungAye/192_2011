from rental import Vehicle, Renter, ElectricCar, Motorbike

def main():

    car = Vehicle("BMW", "M4 Competition", "13MW4C")
    electric_car = ElectricCar("Tesla", "Model Y", "EV011", 70)
    motorbike = Motorbike("Kawasaki", "ZX10R", "KW101", 1000)

    renter = Renter("Tyzon", 670523)
 
    print("\nInitial vehicles:")
    print(car)
    print(electric_car)
    print(motorbike)

    print("\nRenter:")
    print(f"Name: {renter.name}")
    print(f"License: {renter.license_no}")
    print(f"Rented vehicles: {renter.rented}")

    print("\nRenting the BMW...")
    car.rent()
    print(car)

    print("\nReturning the BMW...")
    car.return_vehicle()
    print(car)

    print("\nTesting invalid renter name:")
    try:
        Renter("", 670523)
    except ValueError as error:
        print(f"ValueError has been found: {error}")

    print("\nTesting invalid license number:")
    try:
        Renter("Tyzon", -1)
    except ValueError as error:
        print(f"ValueError has been found: {error}")

    print("\nTesting validation after creation:")
    try:
        renter.name = ""
    except ValueError as error:
        print(f"ValueError has been found: {error}")

    try:
        renter.lincense_no = 0
    except ValueError as error:
        print(f"ValueError has been found: {error}")

    print("\nTesting Inheritance:")
    print(f"ElectricCar is_a Vehicle: {isinstance(electric_car, Vehicle)}")
    print(f"Motorbike is_a Vehicle: {isinstance(motorbike, Vehicle)} ")

    print("\nTesting Polymorphism with a mixed vehicles list:")
    vehicles = [
        car,
        electric_car,
        motorbike
    ]

    for vehicle in vehicles:
        print(vehicle)


if __name__ == "__main__":
    main()
