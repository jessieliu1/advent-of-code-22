import sys

def part1():
    overlaps = 0
    with open(sys.argv[1], 'r') as file:
        for line in file:
            pairs = line.split(",")
            first = pairs[0].split("-")
            second = pairs[1].split("-")
            if (int(first[0]) <= int(second[0]) and int(first[1]) >= int(second[1])) or (int(second[0]) <= int(first[0]) and int(second[1]) >= int(first[1])) :
                overlaps +=1
        file.close()
    print(overlaps)

def part2():
    overlaps = 0
    with open(sys.argv[1], 'r') as file:
        for line in file:
            pairs = line.split(",")
            first = pairs[0].split("-")
            second = pairs[1].split("-")
            if (int(first[0]) <= int(second[0]) and int(first[1]) >= int(second[0])) or (int(second[0]) <= int(first[0]) and int(second[1]) >= int(first[0])) :
                overlaps +=1
        file.close()
    print(overlaps)

def main():
    part2()

main()
