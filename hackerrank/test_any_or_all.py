def palindromic(text):
    text = str(text)
    return str(text[::-1]) == text


def test_palindromic():
    assert palindromic('roma') is False
    assert palindromic('12321') is True


input()
numbers = input()
numbers_int = [int(number) for number in numbers.split()]
print(numbers_int)
if min(numbers_int) <= 0:
    print(False)
else:
    any([palindromic(number) for number in numbers_int])
