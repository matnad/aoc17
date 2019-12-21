from aocd.models import Puzzle

puzzle = Puzzle(year=2017, day=5)
in1 = [int(x) for x in puzzle.input_data.split('\n')]

# print(in1)
#
# # Part 1
# ix = steps = 0
# try:
#     while True:
#         val = in1[ix]
#         in1[ix] += 1
#         ix += val
#         steps += 1
# except IndexError:
#     print("done")
#
# puzzle.answer_a = steps

# Part 2


ix = steps = 0
try:
    while True:
        val = in1[ix]
        if val >= 3:
            in1[ix] -= 1
        else:
            in1[ix] += 1
        ix += val
        steps += 1
except IndexError:
    print("done")

puzzle.answer_b = steps