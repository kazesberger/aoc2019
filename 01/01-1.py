def fuel_fn(mass):
    return (mass // 3) - 2

with open('01/input.txt') as f:
    read_data = f.readlines()
masses = map(int,read_data)

print(sum(map(fuel_fn, masses)))
