def decoder(root, str):
    length = 0
    ans = ''
    for char in str:
        if char == '1' and root.right != None:
            root = root.right
            length += 1
        elif char == '0' and root.left != None:
            length += 1
            root = root.left

        if root.left == None and root.right == None:
            ans = root.data
    return [ans, length]



# Enter your code here. Read input from STDIN. Print output to STDOUT
def decodeHuff(root, s):
    i = 0
    final = ''
    while i < len(s):
        char, length = decoder(root, s[i:])
        i += length
        final += char
    print(final)