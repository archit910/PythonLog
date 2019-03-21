def missing_element(ar):
    n = len(ar)
    actual_sum = sum(ar)
    n = n + 1
    expected_sum = n * ( n + 1)
    expected_sum /= 2
    print abs(actual_sum-expected_sum)

if __name__ == '__main__':
    # Input an array
    ar = [int(each) for each in raw_input().split()]
    missing_element(ar)