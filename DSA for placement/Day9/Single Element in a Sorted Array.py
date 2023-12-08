def singleNonDuplicate(arr):
    i=0
    while i<len(arr):
        n=arr.count(arr[i])
        if n==1:
            return arr[i]
        i+=n
