# Enter your code here. Read input from STDIN. Print output to STDOUT

stack = []

highest = 0
for _ in range(int(input())):
    query = list(map(int, input().split()))

    if query[0] == 1:
        if query[1] > highest: highest = query[1]
        stack.append(query[1])
    elif query[0] == 2:
        poped = stack.pop()
        if poped == highest:
            if len(stack) > 0:
                highest = max(stack)
            else:
                highest = 0
    else:
        print(highest)

