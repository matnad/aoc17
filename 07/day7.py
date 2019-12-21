import re

import networkx as nx
from aocd.models import Puzzle

puzzle = Puzzle(year=2017, day=7)
in1 = puzzle.input_data.split('\n')

# print(in1)
in1 = '''pbga (66)
xhth (57)
ebii (61)
havc (66)
ktlj (57)
fwft (72) -> ktlj, cntj, xhth
qoyq (66)
padx (45) -> pbga, havc, qoyq
tknk (41) -> ugml, padx, fwft
jptl (61)
ugml (68) -> gyxo, ebii, jptl
gyxo (61)
cntj (57)'''.split('\n')

G = nx.DiGraph()
for line in in1:
    node = line.split()[0].strip()
    weight = int(re.findall(r'\d+', line)[0])
    G.add_node(node, weight=weight)
    if '->' in line:
        above = line.split('->')[1].split()
        for target in above:
            target = target.replace(',', '').strip()
            G.add_edge(node, target)

print(G.nodes(data='weight'))
# nx.draw_networkx(G)
# plt.show()
# print(G.in_degree)
# print(root := [n for n, d in G.in_degree if d == 0])
# puzzle.answer_a = root[0]
