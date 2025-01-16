def main():
    while True:
     x= input("Date: ")
     if "/" in x:
        input_number(x)
     else:
        input_date(x)


def input_number(y):
    u,v,w = y.split("/")
    print (f"{w}-{u}-{v}")

def input_date(z):
    months = ["January","February","March","April","May","June","July","August","September","October","November","December"]
    try:
        a,w = z.split(",")    
        u,v = a.split(" ")
        if u in months:
            print (f"{w}-{months.index(u)+1}-{v}")
    except ValueError:
        return False



if __name__ == "__main__":
    main()


