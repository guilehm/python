set_a_count = input()
elements_a = set([int(i) for i in input().split()])
other_sets_count = input()
for other_set in range(int(other_sets_count)):
    operation_name, length = input().split()
    other_set_elements = set([int(i) for i in input().split()])
    eval("elements_a.{}({})".format(operation_name, other_set_elements))
numbers = [int(i) for i in list(elements_a)]
print(sum(numbers))
