from collections import deque

line = deque(maxlen=4)

line.append(1)
line.append(2)
line.append(3)
line.append(4)

print(line)

line.append(5)
line.append(6)

print(line)

line.appendleft(7)

print(line)

line.pop()

print(line)

line.popleft()

print(line)
