
def max_subarray_contiguos(ar):
    """
    Implementation of Kadane's Algorithm
    """
    max_end_here = -10000000000 # Really small number
    max_so_far = -10000000000 # Really small number
    for each in ar:
        if max_end_here < 0 :
            max_end_here = each
        else:
            max_end_here += each
        max_so_far = max(max_so_far, max_end_here)
    return max_so_far
if __name__ == '__main__':
    ar = [int(each) for each in raw_input().split()]
    print max_subarray_contiguos(ar)

