from collections import defaultdict

from aocd.models import Puzzle

puzzle = Puzzle(year=2017, day=4)
in1 = puzzle.input_data.split('\n')

# part 1
# nvalid = 0
# for line in in1:
#     used = defaultdict(bool)
#     pws = line.split()
#     valid = True
#     for pw in pws:
#         if used[pw]:
#             valid = False
#             break
#         used[pw] = True
#     if valid:
#         nvalid += 1
#
# puzzle.answer_a = nvalid

# part 2
nvalid = 0
for line in in1:
    pws = line.split()
    valid = True
    for ix1, pw1 in enumerate(pws):
        for ix2, pw2 in enumerate(pws):
            if ix1 != ix2:
                if len(pw1) == len(pw2) and all(a in pw2 for a in pw1):
                    valid = False
                    break
    if valid:
        nvalid += 1

print(nvalid)
puzzle.answer_b = nvalid