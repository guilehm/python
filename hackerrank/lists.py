# https://www.hackerrank.com/challenges/python-lists/problem

if __name__ == '__main__':
    N = int(input())
    result = []
    for i in range(N):
        text = input()
        command, *args = text.split()
        args = map(int, args)
        try:
            getattr(result, command)(*args)
        except AttributeError:
            print(result)
