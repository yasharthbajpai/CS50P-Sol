def main ():
    inpu = input("Expression : ")
    x,y,z = inpu.split(" ")

    if y == "+":
        print(f"{float(int(x) + int(z)):.1f}")
    elif y == "-": 
        print(f"{float(int(x) - int(z)):.1f}")
    elif y == "*":
        print(f"{float(int(x) * int(z)):.1f}")
    elif y == "/":  
        print(f"{float(int(x) / int(z)):.1f}")  
    else: 
        print("Invalid Operator")      


if __name__ == "__main__": 
    main()