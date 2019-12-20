def day_1a(contents):
    masses = [int(x) for x in contents]
    fuels = [max(m // 3 - 2, 0) for m in masses]
    return sum(fuels)

def day_1b(contents):
    masses = [int(x) for x in contents]
    fuels = [total_fuel(m) for m in masses]
    return sum(fuels)


def total_fuel(mass, acc=0):
    fuel = mass // 3 - 2
    if fuel <= 0:
        return acc
    else:
        return total_fuel(fuel, acc + fuel)


def main():
    with open('input', 'r') as input:
        contents = input.readlines()
        result = day_1a(contents)
        print('Part 1')
        print(result)
        result = day_1b(contents)
        print('Part 2')
        print(result)


if __name__ == '__main__':
    main()