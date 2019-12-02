#!python

import math

with open('input.txt', 'r') as file:
  mass = 0
  for line in file:
    fuel = math.floor(int(line) / 3) - 2
    fuel_required = math.floor(fuel / 3) - 2
    while fuel_required >= 0:
        fuel += fuel_required
        print("Fuel: " + str(fuel))
        fuel_required = math.floor(fuel_required / 3) - 2
        print("Required: " + str(fuel_required))
    mass += fuel
    print("Mass: " + str(mass))
    print("+-------+")