from collections import defaultdict

d = defaultdict(list)

d['josé'].append(10)
d['josé'].append(20)
d['josé'].append(30)
print(d)
d['maria'].append(28)
d['maria'].append(23)
d['maria'].append(43)
print(d)

d2 = defaultdict(set)
d2['josé'].add(20)
d2['josé'].add(20)
d2['josé'].add(20)
d2['josé'].add(20)
d2['josé'].add(40)
print(d2)
