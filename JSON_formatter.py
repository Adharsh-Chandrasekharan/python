def json_formatter(strings):
  indent=0
  opening=['[','(','{']
  closing=[']','}',')']
  # Manually construct the string with curly braces
  data_strings = "{" + ", ".join(f'"{key}": "{value}"' for key, value in data.items()) + "}"
  data_string=""
  for i in range(len(data_strings)):
    if data_strings[i]=='"' and ( (data_strings[i+1] in opening ) or (data_strings[i-1] in closing)):
      continue
    else:
      data_string=data_string+data_strings[i]


  print(data_string)
  for i in data_string:
    if i in opening:
      print("\n"+('*'*indent)+i)
      indent+=2
      print(('*'*indent),end="")
    elif i in closing:
      indent-=2
      print("\n"+('*'*indent)+i,end="")
    elif i==',':
      print(i+"\n"+('*'*indent),end="")
    else:
      print(i,end="")

  
  
data = {"name": "John", "friend":"no one"}

json_formatter(data)