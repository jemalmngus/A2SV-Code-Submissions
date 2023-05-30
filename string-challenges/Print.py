# This code prints numbers from 1 to n, where n is provided as input.

# Problem link: https://www.hackerrank.com/challenges/python-print/problem?isFullScreen=true

if __name__ == '__main__':
    n = int(input())
    for i in range(1, n + 1):
        print(i, end="")
    print()

# Sample Case 1: n = 3
# Expected Output: 123

# Sample Case 2: n = 5
# Expected Output: 12345