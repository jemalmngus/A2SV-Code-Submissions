# Solution for the problem "Text Wrap" on HackerRank
# Problem Link: https://www.hackerrank.com/challenges/text-wrap/problem?isFullScreen=true

def wrap(string, max_width):
    x=""
    for i in range(len(string)):
        if i%max_width==0 and i>0:
            x+="\n"
        x+=string[i]
    return x


# Sample Test Case
string = "ABCDEFGHIJKLIMNOQRSTUVWXYZ"
max_width = 4
result = wrap(string, max_width)
print(result)

# Output:
# ABCD
# EFGH
# IJKL
# IMNO
# QRST
# UVWX
# YZ
