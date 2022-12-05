import sys
import string

def part1():
    with open(sys.argv[1], 'r') as file:
        total = 0
        for line in file:
            line = line.strip()
            first = set()
            second = set()
            for i in range (0, len(line)):
                if i < len(line) / 2:
                    first.add(line[i])
                else:
                    second.add(line[i])
            overlap = list(first.intersection(second))
            total += list(string.ascii_letters).index(overlap[0]) + 1
        file.close()
        print(total)

def part2():
    total = 0
    with open(sys.argv[1], 'r') as file:
        input_lines = [line.strip() for line in file]
        for i in range (0, int(len(input_lines) / 3)):
            lines = input_lines[i*3:(i+1)*3]
            sets = []
            for line in lines:
                sets.append(set([*line]))
            intersect = sets[0]
            for j in range (1, len(sets)):
                intersect = intersect.intersection(sets[j])
            total += list(string.ascii_letters).index(list(intersect)[0]) + 1
        file.close()
        print(total)

def main():
    part2()

main()
