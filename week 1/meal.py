def main():
    x = input("Time: ")
    x = convert(x)

    
    if  7<=x<=8:
        print(f"Breakfast")
    elif 12<=x<=13:
        print(f"Lunch")
    elif 19<=x<=20:
        print(f"Dinner")
    else:  
        print(f"Hammer Time")



def convert(time):
    y = time.split(":")
    #return (float(y[0] + str(float(y[1])/60)))
    return round(float(y[0]) + float(y[1])/60, 2)

if __name__ == "__main__":
    main()