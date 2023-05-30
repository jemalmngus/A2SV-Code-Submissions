
# Solution for the problem "Swap Case" on HackerRank
# Problem Link: https://www.hackerrank.com/challenges/swap-case/problem?isFullScreen=true

def swap_case(s):
    return s.swapcase()

if __name__ == '__main__':
    s = input()
    result = swap_case(s)
    print(result)

# Sample Test Case
s='HackerRank.com presents "Pythonist 2".'

# output
# 'hACKERrANK.COM PRESENTS "pYTHONIST 2".'