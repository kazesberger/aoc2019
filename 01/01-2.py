def fuel_fn(mass):
    fuel = (mass // 3) - 2
    return 0 if fuel < 0 else fuel + fuel_fn(fuel)

# fuel_fn(1969)

with open('01/input.txt') as f:
    read_data = f.readlines()
masses = map(int,read_data)

print(sum(map(fuel_fn, masses)))
