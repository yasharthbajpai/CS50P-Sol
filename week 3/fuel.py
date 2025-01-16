def main (): 
    x= get_fraction()
    y= make_percentage(x)
    print(f"{y}")



def get_fraction():
    integers = "0123456789"
    fraction = input("Fraction: ")
    try:
     a, b = map(float, fraction.split('/'))
     if b==0 or a>b:
        get_fraction()
    except (ValueError, ZeroDivisionError):
     print(f"There is some error")

    



    """try :
     while str(a) in integers or str(b)  in integers or int(a)<int(b) or b != "0" :
        get_fraction()
    except (ValueError , ZeroDivisionError):
         print(f"There is some error")
    else:
       return f"{(a/b):.2f}"""
     


     
        

def make_percentage(i):
     y =  float(i)*100
     if y>99:
       return "F"
     elif y<1:
         return "E"
     else:
        return f"{y}%"
      
     
if __name__ == "__main__":
    main()