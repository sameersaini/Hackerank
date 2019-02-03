# Enter your code here. Read input from STDIN. Print output to STDOUT
import re

def isIp4(string):
    pattern = "^((2([0-4][0-9]|5[0-5])|1[0-9][0-9]|[0-9][0-9]|[0-9])\.){3}(2([0-4][0-9]|5[0-5])|1[0-9][0-9]|[0-9][0-9]|[0-9])$"
    regex = re.compile(pattern)
    match = re.match(regex, string)
    if match:
        return True
    else:
        return False


def isIpv6(string):
    pattern = "^([0-9a-f]{1,4}:){7}[0-9a-f]{1,4}$"
    regex = re.compile(pattern)
    match = re.match(regex, string)
    if match:
        return True
    else:
        return False


for _ in range(int(input())):
    test = input()
    if isIp4(test):
        print("IPv4")
    elif isIpv6(test):
        print("IPv6")
    else:
        print("Neither")
