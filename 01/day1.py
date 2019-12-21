from aocd.models import Puzzle


puzzle = Puzzle(year=2017, day=1)
in1 = str(puzzle.input_data)

print(in1)
matched = []
for i in range(len(in1)-1):
    if in1[i] == in1[i+1]:
        matched.append(int(in1[i]))
if in1[0] == in1[-1]:
    matched.append(int(in1[-1]))

print("part 1", sum(matched))
# puzzle.answer_a = sum(matched)

matched = []
offset = len(in1) // 2
for i in range(len(in1)):
    if in1[i] == in1[(i + offset) % len(in1)]:
        matched.append(int(in1[i]))

print("part 2", sum(matched))
puzzle.answer_b = sum(matched)