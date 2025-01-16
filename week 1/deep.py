def main():
    print(f"What is Great Question of Life, the Universe and Everything? ")
    answer = input ()

    if answer == "42":
        print("Yes")
    elif answer == "forty-two":
        print("Yes")
    elif answer == "fourty two":
        print("Yes")
    else:
        print("No")


if __name__== "__main__":
    main()