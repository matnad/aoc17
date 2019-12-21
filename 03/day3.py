from collections import defaultdict

from aocd.models import Puzzle

puzzle = Puzzle(year=2017, day=3)
in1 = int(puzzle.input_data)

# Part 1
# grid = defaultdict(int)
# nr_to_pos = {}
# grid[(0,0)] = 1
# i, c, x, y = 2, 0, 1, 0
# cx, cy = [-1, 0, 1, 0], [0, 1, 0, -1]
# dx, dy = [0, -1, 0, 1], [-1, 0, 1, 0]
# while i <= in1:
#     while grid[(x + cx[c], y + cy[c])] > 0:
#         grid[(x,y)] = i
#         nr_to_pos[i] = (x,y)
#         i += 1
#         x += dx[c]
#         y += dy[c]
#     c = (c+1) % 4
#
# print(in1, i, x, y, nr_to_pos[in1])
# ans = abs(nr_to_pos[in1][0]) + abs(nr_to_pos[in1][1])
# print(ans)
# puzzle.answer_a = ans

# Part 2
grid = defaultdict(int)
grid[(0, 0)] = 1
i, c, x, y = 2, 0, 1, 0
cx, cy = [-1, 0, 1, 0], [0, 1, 0, -1]
dx, dy = [0, -1, 0, 1], [-1, 0, 1, 0]
nbx, nby = [0, 0, 1, 1, 1, -1, -1, -1], [1, -1, 0, 1, -1, 0, 1, -1]
ans = False
while not ans:
    while grid[(x + cx[c], y + cy[c])] > 0:
        val = sum([grid[(a, b)] for a, b in [(x + ddx, y + ddy) for ddx, ddy in zip(nbx, nby)]])
        grid[(x, y)] = val
        print(val)
        if val > in1:
            ans = val
            break
        x += dx[c]
        y += dy[c]
    c = (c + 1) % 4

print(ans)
puzzle.answer_b = ans
