import sys

POINTS = {'X':1, 'Y':2, 'Z':3}
SHAPES = {'A':'X', 'B':'Y', 'C':'Z'}
WIN = [('B', 'Z'), ('A', 'Y'), ('C', 'X')]
WIN_DICT = {'B':'Z','A':'Y','C':'X'}
LOSS = [('C', 'Y'), ('B', 'X'), ('A', 'Z')]
LOSS_DICT = {'C':'Y','B':'X','A':'Z'}

# A for Rock, B for Paper, and C for Scissors.
# X for Rock, Y for Paper, and Z for Scissors
# The score for a single round is the score for the shape you selected
# (1 for Rock, 2 for Paper, and 3 for Scissors) plus the score for the outcome
# of the round (0 if you lost, 3 if the round was a draw, and 6 if you won).
def part1():
    total = 0
    with open(sys.argv[1], 'r') as file:
        for line in file:
            result = line.strip().split(" ")
            result = tuple(result)
            total += POINTS[result[1]]
            if result in WIN:
                total += 6
            elif result not in LOSS:
                total += 3
        file.close()
    print(total)

# Anyway, the second column says how the round needs to end: X means you need
# to lose, Y means you need to end the round in a draw, and Z means you need
# to win. Good luck!"
def part2():
    total = 0
    with open(sys.argv[1], 'r') as file:
        for line in file:
            move = ()
            result = line.strip().split(" ")
            if result[1] == 'X':
                move = (result[0], LOSS_DICT[result[0]])
            elif result[1] == 'Y':
                move = (result[0], SHAPES[result[0]])
            else:
                move = (result[0], WIN_DICT[result[0]])
            total += POINTS[move[1]]
            if move in WIN:
                total += 6
            elif move not in LOSS:
                total += 3
        file.close()
    print(total)

def main():
    part2()

main()
