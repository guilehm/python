# https://www.hackerrank.com/challenges/mini-max-sum/problem?h_r=next-challenge&h_v=zen


def miniMaxSum(arr):
    numbers = sorted(arr)
    lowers = sum(numbers[:4])
    highers = sum(numbers[:-5:-1])
    print(lowers, highers)


miniMaxSum([i for i in range(1, 16)])

