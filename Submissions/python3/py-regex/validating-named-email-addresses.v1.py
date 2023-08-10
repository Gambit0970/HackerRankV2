import email.utils
import re
pattern = r"^[a-zA-Z][a-zA-Z0-9_.+-]+@[a-zA-Z][a-zA-Z0-9]+\.[a-zA-Z]{1}[a-zA-Z]{0,2}$"
for _ in range(int(input())):
    emDets = email.utils.parseaddr(input())
    if re.match(pattern,emDets[1]):
        print(email.utils.formataddr(emDets))
