import functools

def large(a, b):
    if a + b < b + a:
        return 1 # sort it
    else:
        return -1 # do not sort it
if __name__ == '__main__':
    ar = [each for each in raw_input().split()]
    ar.sort(key=functools.cmp_to_key(large))
    print ''.join(ar)