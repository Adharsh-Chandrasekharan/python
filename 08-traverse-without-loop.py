lst=eval(input("Enter a list :"))
start=int(input("Start index :"))
end=int(input("End index :"))
def iterate(lst,start,end):
  if start<0 or start>=end or end>=len(lst):
    return
  else:
    print(lst[start],end=" ")
    iterate(lst,start+1,end)


iterate(lst,start,end)