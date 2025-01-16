import re 

def find_uppercase(x):
    uppercase_letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    for i in range(len(x)):
        if x[i] in uppercase_letters:
            return i
    return 0  

def split_uppercase(x,the_letter):
    return x[:the_letter], x[the_letter:]

def main():
    i=0
    x = input("CamelCase: ")
    the_letter = find_uppercase(x)
    if the_letter == 0:
        print(f"Snake_case: {x}")  
    elif the_letter != 0:
        first, second = split_uppercase(x,the_letter)
        print(f"Snake_case: {first.lower() + '_' + second.lower()}")  

if __name__ == "__main__":
    main()