import re 

def find_uppercase(x):
    if re.search(r'[A-Z]', x):
        return re.search(r'[A-Z]', x).start()
    return 0  

def split_uppercase(x,the_letter):
    return x[:the_letter], x[the_letter:]

def convert_camel_to_snake(x):
    the_letter = find_uppercase(x)
    if the_letter == 0:
         return x.lower()
    else: 
        first, second = split_uppercase(x,the_letter)
        # Changed this line: removed .lower() from second
        # This ensures that subsequent uppercase letters are detected
        return first.lower() + '_' + convert_camel_to_snake(second)

def main():
    i=0
    x = input("CamelCase: ")
    # Changed these lines to avoid calling convert_camel_to_snake twice
    result = convert_camel_to_snake(x)
    print(f"Snake_case: {result}")

if __name__ == "__main__":
    main()