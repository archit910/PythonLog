import functools
def my_comparator_1(a, b):
    #it is a comparator which sorts in descending order
    if a < b:
        return 1 # do sort it
    else:
        return -1 # do not sort it ( keep the element a earlier)

def my_comparator_2(a, b):
    #it is a comparator which sorts even and odd numbers
    #keeps even numbers earlier
    if a % 2 == 0 and b % 2 == 0:
        if a > b:
            return 1  # sort evens in ascending
        else:
            return -1  # do not sort it
    if a % 2 != 0 and b % 2 != 0:
        if a > b:
            return 1 # sorting odds in ascending order
        else:
            return -1 #do not sort it
    elif a % 2 == 0:
        return -1 # do not sort it ( keep even numbers earlier)
    else:
        return 1 # sort it


l = [1 , 22, 12 , 3, 34 , 5, 12 , 10, 0 , 100, 43]
l.sort(key = functools.cmp_to_key(my_comparator_2))

print (l)
