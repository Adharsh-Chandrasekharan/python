#"AC*wv12n/:#e123we2.45oin (fwoi6n#a98nfwb+owi"

str1="AC*wv12n/:#e123we2.45oin (fwoi6n#a98nfwb+owi"
temp=""
data=[]
for ch in str1:
  if ch.isdigit() or ch==".":
    temp=temp+ch
  elif len(temp)!=0:
    data.append(eval(temp))
    temp=""
data.sort()
print(data)