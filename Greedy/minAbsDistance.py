# Complete the minimumAbsoluteDifference function below.
def minimumAbsoluteDifference(arr):
    arr.sort()
    diff = abs(arr[0] - arr[1])
    for i in range(1, len(arr)-1):
        tempDiff = abs(arr[i] - arr[i+1])
        if tempDiff < diff:
            diff = tempDiff

    return diff