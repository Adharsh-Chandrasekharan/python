def equalization(n,m,s,t):
  count=0
  s1=[]
  for ch in s:
    s1.append(ch)
  
  for i in range(n):
    char=s1.pop(i)
    for word in t:
      if "".join(s1)==word:
        count+=1
    s1.insert(i,char)
  return count
    




print(equalization(5,4,'abcde',['abcd','abcc','cddd','acde']))