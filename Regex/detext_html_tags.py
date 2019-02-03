# Enter your code here. Read input from STDIN. Print output to STDOUT
import re

Regex_Pattern = r"<\s*(\w+).*?>"  # Do not delete 'r'.

tags = {}
for _ in range(int(input())):
    Test_String = input()
    match = re.findall(Regex_Pattern, Test_String)
    if match:
        for tag in match:
            tags[tag] = 1

print(";".join(sorted(list(tags.keys()))))