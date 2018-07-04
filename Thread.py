import time
import threading


def print1():
    print('1')
    time.sleep(1)
    return print1()


def print2():
    print('2')
    time.sleep(1)
    return print2()


def main():
    threading.Thread(target=print1).start()
    threading.Thread(target=print2).start()


if __name__ == '__main__':
    main()
