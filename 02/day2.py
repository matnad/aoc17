from aocd.models import Puzzle


puzzle = Puzzle(year=2017, day=2)
in1 = [[int(y) for y in x.split('\t')] for x in puzzle.input_data.split('\n')]

sum = 0
for line in in1:
    sum += max(line) - min(line)

print("part a:", sum)
# puzzle.answer_a = sum

sum = 0
for line in in1:
    for ix1, d1 in enumerate(line):
        for ix2, d2 in enumerate(line):
            if ix1 != ix2 and d1 % d2 == 0:
                sum += d1//d2

print("part b:", sum)
puzzle.answer_b = sum