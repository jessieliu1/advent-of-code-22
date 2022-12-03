import sys

def main():
    elves = []
    with open(sys.argv[1], 'r') as file:
        sackVal = 0
        for line in file:
            if line.strip() != "":
                sackVal += int(line.strip())
            else:
                elves.append(sackVal)
                sackVal = 0
        if sackVal != 0:
            elves.append(sackVal)
        file.close()
    print(sum(sorted(elves, reverse=True)[:3]))

main()
