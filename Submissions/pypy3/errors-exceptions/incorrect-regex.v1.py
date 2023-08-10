import re

T = int(input())
for i in range(T):
    pattern = "r'"+input()+"'"
    try:
        re.compile(pattern)
        print("True")
    except re.error:
        print("False")
