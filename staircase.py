# https://www.hackerrank.com/challenges/staircase/problem


def staircase(size):
    spaces = size - 1
    for i in range(size):
        print('{spaces}{hashes}'.format(spaces=' ' * spaces, hashes='#' * (size - spaces)))
        spaces -= 1


staircase(4)
