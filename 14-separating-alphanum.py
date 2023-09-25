p=['1234python668','678java899','4566hadoop9123']
int_list=[]
str_list=[]
for letter in p:
  st=""
  it=""
  for ch in letter:
    if ch.isalpha():
      st=st+ch
    elif ch.isnumeric():
      it=it+ch
  int_list.append(int(it))
  str_list.append(st)
print(int_list)
print(str_list)
