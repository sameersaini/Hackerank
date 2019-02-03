# Enter your code here. Read input from STDIN. Print output to STDOUT
import re
sequences = [input() for _ in range(int(input()))]
queries = [input() for _ in range(int(input()))]

for query in queries:
    total = 0
    pattern = "[a-zA-Z0-9_]+({q})[a-zA-Z0-9_]+".format(q=query)
    Regex_Pattern = re.compile(pattern)
    for sequence in sequences:
        match = re.findall(Regex_Pattern, sequence)
        if match:
            total += len(match)
    print(total)
