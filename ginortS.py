# https://www.hackerrank.com/challenges/ginorts/problem?h_r=next-challenge&h_v=zen

phrase = input()
lowers = sorted([letter for letter in phrase if letter.islower()])
uppers = sorted([letter for letter in phrase if letter.isupper()])
numbers = sorted([char for char in phrase if char.isdigit()])
odds = []
evens = []
[odds.append(number) if int(number) % 2 else evens.append(number) for number in numbers]
print("".join(lowers + uppers + sorted(odds) + sorted(evens)))
