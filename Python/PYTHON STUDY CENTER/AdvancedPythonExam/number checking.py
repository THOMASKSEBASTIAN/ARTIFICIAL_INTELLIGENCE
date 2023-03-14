import re
s="+915678905432 +914567890321 765432167 123450987765 +919976532456"
rule='[+][9][1][0-9]{10}'
matcher=re.fullmatch(rule,s)
if matcher is not None:
    print(matcher)

