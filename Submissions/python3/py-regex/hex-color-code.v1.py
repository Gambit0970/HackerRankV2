import re
pattern=r'\#[a-fA-F0-9]{3,6}(?=[;,)])'
N = int(input())
html = ''.join(input() for _ in range(N))
html = html.replace(" ","")
found = re.findall(pattern,html)
print('\n'.join(found))
