class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __repr__(self):
        return self.name


def by_name(person):
    return person.name


def by_age(person):
    return person.age

p1 = Person('Zoraide', 22)
p2 = Person('Marcela', 24)
p3 = Person('Geraldo', 38)
p4 = Person('Agenor', 44)

persons = [p1, p2, p3, p4] 

print(sorted(persons, key=by_name))
print(sorted(persons, key=by_age))

print()

print(sorted(persons, key=by_name, reverse=True))
print(sorted(persons, key=by_age, reverse=True))
