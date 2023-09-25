mystr="a,a,a,b,b,c,c,c"
mylist=mystr.split(",")
visited=[]
final_list=[]
for ch in mylist:
  if ch not in visited:
    final_list.append(f"{ch}:{mylist.count(ch)}")
    
    visited.append(ch)
print(",".join(final_list))