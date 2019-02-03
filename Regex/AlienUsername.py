# Enter your code here. Read input from STDIN. Print output to STDOUT
import re
pattern = "^[_.][0-9]+[a-zA-Z]*_?$"
regex = re.compile(pattern)

for _ in range(int(input())):
    match = re.findall(regex, input())
    if match:
        print("VALID")
    else:
        print("INVALID")
