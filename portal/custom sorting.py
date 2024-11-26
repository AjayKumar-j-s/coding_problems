from functools import cmp_to_key

def custom(x, y):
    if str(x)[1] > str(y)[1]:
        return 1
    else:
        return -1
my_list = [513, 389, 841, 625, 104]
sorted_list = sorted(my_list, key=cmp_to_key(custom))

print("Sorted list:", sorted_list)
