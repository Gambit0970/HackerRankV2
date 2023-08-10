import re
c='bcdfghjklmnpqrstvwxyz'
v='aeiou'
matchs = re.findall(r'(?<=['+c+'])['+v+']{2,}(?=['+c+'])', input(), re.IGNORECASE)
if len(matchs)==0:
    print(-1)
else:
    print("\n".join([match for match in matchs]))
