import copy

# list is used as a stack python
# for push - append()
# for pop - pop()


def next_greater_element(ar):
    stack = []
    nge = []
    stack.append(ar[-1]) # last element in stack
    nge.append(-1)

    for i in range(len(ar)-2 , -1 , -1):

        while(stack):
            top = stack[-1]
            if ar[i] > top:
                stack.pop()
            else:
                nge.append(top)
                stack.append(ar[i])
                break

            if len(stack) == 0:
                nge.append(-1)
    return nge[::-1] # reversed list

if __name__ == '__main__':
    # l = [13,7,6,12]
    l = [4,5,2,25]
    nge = next_greater_element(ar = copy.deepcopy(l))
    print nge

