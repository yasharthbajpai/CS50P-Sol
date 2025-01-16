import re 

def find_uppercase(x):
    if re.search(r'[A-Z]', x):
        return re.search(r'[A-Z]', x).start()
    return -5  

def split_uppercase(x,the_letter):
    return x[:the_letter+1], x[the_letter+1:]

def convert_camel_to_snake(x):
    the_letter = find_uppercase(x)
    if the_letter == -5:
         return x.lower()
    else: 
        first, second = split_uppercase(x,the_letter)
        return first.lower() + '_' + convert_camel_to_snake(second)
    


def main():
    i=0
    x = input("CamelCase: ")
    result = convert_camel_to_snake(x)
    print(f"Snake_case: {result}")


if __name__ == "__main__":
    main()