def rotate(arr,n,dir):
  if dir=="l":
    arr=arr[n:]+arr[:n]
    print(arr)
  elif dir=="r":
    arr=arr[-n:]+arr[:-n]
    print(arr)


arr=[1,2,3,4,5,6,7]
n=int(input("Enter n: "))
dir=input("Enter l or r: ")
rotate(arr,n,dir)