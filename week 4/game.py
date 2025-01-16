import random

def main():
    while True:
      x= int(input("Level: " ))
      if type(x) == int:
       break
      
      

    y= random.randint(0, x)
    get_number(y)
     


def get_number(m):
  while True:
    n= int(input("Guess : "))
    if n==m:
      print("Just right!")
      break
    elif n>m:
        print("Too large!")
    else:
        print("Too small!")
    


main()