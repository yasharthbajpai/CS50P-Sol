def main():
    x = get_input()
    vowels = "aeiouAEIOU"
    result = ""
    for char in x:
        if char not in vowels:
            result = result + char            
    print(result)


def get_input():
    return input("Input: ")



if __name__ == "__main__": 
    main()