#B7A1R3

str1 =input("Enter a alphal number string : ")
alphabets=[]
numbers=[]

for ch in str1:
  if ch.isalpha():
    alphabets.append(ch)
  else:
    numbers.append(ch)

final_list=sorted(alphabets)+sorted(numbers)
output=''.join(final_list)

print(output)
