

def main():
    x= input("Enter what you want  " )
    print(convert(x))

def convert (x):
    y = x.replace(":)" , "😊").replace(":(" , "😢")
    return y

if __name__ == "__main__":
    main()