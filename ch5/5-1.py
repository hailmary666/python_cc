cars = ["bmw", "subaru", "toyota", "porche", "tesla"]
for car in range(1, 11):
    if car < 6:
        print(f"{car}. Is car == mazda?")
        print(cars[car - 1] == 'mazda')
    else:
        print(f"{car}. Is car == {cars[car-6]}?")
        print(cars[car - 6] == cars[car-6])