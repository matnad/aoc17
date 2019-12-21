from collections import defaultdict

from aocd.models import Puzzle

puzzle = Puzzle(year=2017, day=6)
in1 = [int(x) for x in puzzle.input_data.split('\t')]

# seen = defaultdict(bool)
# state = in1
#
# it = 0
# while True:
#     if seen[tuple(state)]:
#         break
#     seen[tuple(state)] = True
#     val = ix = -9999
#     for i, v in enumerate(state):
#         if v > val:
#             val = v
#             ix = i
#     state[ix] = 0
#     for i in range(val):
#         state[(ix + i + 1) % len(state)] += 1
#
#     it += 1
#
# print("iterations", it)
# puzzle.answer_a = it


seen = defaultdict(int)
state = in1

it = 0
phase2 = False
while True:
    if seen[tuple(state)] == 1 and not phase2:
        it = 0
        phase2 = True
    if seen[tuple(state)] == 2:
        break
    seen[tuple(state)] += 1
    val = ix = -9999
    for i, v in enumerate(state):
        if v > val:
            val = v
            ix = i
    state[ix] = 0
    for i in range(val):
        state[(ix + i + 1) % len(state)] += 1

    it += 1

print("iterations", it)
puzzle.answer_b = it
