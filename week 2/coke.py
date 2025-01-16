def main ():
   x=50 
   print (f"Amount Due: {x}")
   while x>0:
         x = calculate(x)
   else:
            print(f"Change Owed: {abs(x)}")


     



def get_input():
    return int(input("Insert Coin: "))

def calculate(y):
    y =  y- get_input()
    if y < 0:
        return y
    else:
        print(f"Amount Due: {y}") 
    return y


if __name__ == "__main__":
    main()