import random



def get_level():
    while True:
        try:
            x= int(input("Level: " ))
            if x>0 and x<4:
             return x
        except ValueError:
         raise ValueError("Invalid level")
    



def generate_integer(level):
    if level == 1:
        return [random.randint(0, 9) for _ in range(2)]
    elif level == 2:
        return [random.randint(10, 99) for _ in range(2)]
    else:
         return [random.randint(100, 999) for _ in range(2)]
    


def main():
    i=0
    y= get_level()
    for _ in range(10):
        i= do_calculation(y,i)
    
    print(f"Your score is {10 - i}")	

    

def do_calculation(y,i):
    m,n = generate_integer(y)
    for _ in range(3):
     print(f"{m} + {n} =", end="")
     x= int(input())
     if x == m+n:
          return i
          break
    else:
          i= i+1
          print(f"{m} + {n} = {m+n}")
          print("EEE")  
          return i
    
          


        



      

    


if __name__ == "__main__":
    main()