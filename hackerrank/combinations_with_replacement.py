# https://www.hackerrank.com/challenges/itertools-combinations-with-replacement/problem?h_r=next-challenge&h_v=zen

from itertools import combinations_with_replacement


text = input()
text, number = text.split()
combinations = list(combinations_with_replacement(sorted(text), int(number)))
for combination in combinations:
    print("".join(combination))
