def main():
    x = input("Input: ")
    y= shorten(x)
    print("Output: ", y)


def shorten(word):
    vowels = "aeiouAEIOU"
    result = ""
    for char in word:
        if char not in vowels:
            result = result + char
    return result


if __name__ == "__main__":
    main()