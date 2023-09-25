from time import sleep
def run():
  print("press 'Enter' to continue and 'ctrl+c' to stop second hand :")
  attempts=1
  points=0
  points_table={}
  name=input("Enter the name of player: ")
  while True:
    try:
      for digit in range(1,13):
        print(digit)
        sleep(0.2)
    except KeyboardInterrupt:
      print("Stopped at {digit}")
      print("Points are added")
      time.sleep(2)
      if digit in [1,5,9,11]:
        points+=10
      elif digit in [4,7,8,10]:
        points+=20
      elif digit in[3,2,6,12]:
        points+=30
      attempts+=1
      if attempts==4:
        print(f"{name} has scored {points} points")
        points_table[name]=points
        ans=input("Is there any other player (y/n)").lower()
        if ans=='y':
          name = input("Enter the name of player: ")
          attempts=1
          points=0
        else:
          print("Final result: ",points_table)
          return
run()