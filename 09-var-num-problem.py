#get input from the user in the form of aaabbcccd and conert it into the form of a3b2c3d1
str1=input("enter a string of form aaabbccccd: ")
output=""
count=0
for char in str1:
  
  if char in output:
    count+=1
  else:
    if count != 0:
      output=output+(str(count))
    count=1
    output=output+char
output=output+(str(count))  








print(output)
