def father(num):
    def son1():
        print("Hello, I'm son 1")

    def son2():
        print("Hello, I'm son 2")

    try:
        assert num == 20
        return son1
    except AssertionError:
        return son2


f1 = father(10)
f2 = father(20)

f1()
f2()
