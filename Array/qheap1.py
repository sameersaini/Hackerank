# Enter your code here. Read input from STDIN. Print output to STDOUT

stack = []

minimum = 10**9
for _ in range(int(input())):
    query = list(map(int, input().split()))

    if query[0] == 1:
        if query[1] < minimum: minimum = query[1]
        stack.append(query[1])
    elif query[0] == 2:
        stack.remove(query[1])
        removed = query[1]
        if removed == minimum:
            if len(stack) > 0:
                minimum = min(stack)
            else:
                minimum = 10**9
    else:
        print(minimum)