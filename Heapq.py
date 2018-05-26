import heapq

# priority lines
ages = [15, 10, 12, 13, 15, 18, 10, 22]
print(heapq.nsmallest(3, ages))
print(heapq.nlargest(3, ages))

print(ages)
heapq.heapify(ages)
print(ages)
heapq.heappop(ages)
print(ages)
heapq.heappop(ages)
print(ages)
heapq.heappop(ages)
print(ages)
heapq.heappush(ages, 3)
print(ages)
heapq.heappush(ages, 18)


class PriorityQueue:
    def __init__(self):
        self._queue = []
        self._index = 0

    def push(self, item, priority):
        heapq.heappush(self._queue, (-priority, self._index, item))

    def pop(self):
        return heapq.heappop(self._queue)[-1]


class Person:
    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return self.name


q = PriorityQueue()
q.push(Person('Marcos'), 28)
q.push(Person('João'), 30)
q.push(Person('Maria'), 79)

print(q.pop())
print(q.pop())
print(q.pop())
print(dir(q))
