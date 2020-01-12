cars = ['kia', 'audi', 'bmw']
for car in enumerate(cars, 1):
  print(car)

cars = ['kia', 'audi', 'bmw']
print(list(enumerate(cars, start=1)))

# This code isn’t just longer. You can also see that a complex for loop
# implementation would get clunky and error-prone easily.
cars = ['kia', 'audi', 'bmw']
listOfCars = []
n = 1
for car in cars:
    listOfCars.append((n, car))
    n += 1
print(listOfCars)



