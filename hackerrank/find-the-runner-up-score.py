# https://www.hackerrank.com/challenges/find-second-maximum-number-in-a-list/problem

if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())
    arr_sorted = sorted(set(arr))
    runner_up = arr_sorted[-2] if len(arr_sorted) > 1 else arr_sorted[0]
    print(runner_up)
