import copy

def subarray_sum(ar, req_sum):
    i = 0
    j = 1
    sum = ar[i]
    while j < len(ar):
        if i >=j:
            sum = ar[i]
            j = i + 1
        if sum > req_sum:
            sum = sum - ar[i]
            i += 1
        elif sum < req_sum:
            sum += ar[j]
            j += 1
        if sum == req_sum:
            print i , j-1
            break

if __name__ == '__main__':
    # Input an array
    ar = [int(each) for each in raw_input().split()]
    req_sum = int(raw_input())
    subarray_sum(ar = copy.deepcopy(ar), req_sum=req_sum)
