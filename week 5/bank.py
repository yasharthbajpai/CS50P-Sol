def main():
    x = input("Greetings: ").lower()
    y = value(x)
    print (y)


def value(greeting):
    if greeting == "hello":
      return(f"0$")
    elif greeting[0] == "h":
        return (f"20$")
    else:
     return(f"100$")

    


if __name__ == "__main__":
    main()