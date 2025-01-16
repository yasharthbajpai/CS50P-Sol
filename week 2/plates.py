def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):
    if len(s)>6 or len(s)<2:
        return False
    elif s.isalpha():
      return True
    elif s[0].isdigit():
        return False
    for i, char in enumerate(s):
        if char.isdigit():
            y = i   
            break
    for j in range(y, len(s)):
        if not s[j].isdigit():
            return False
        elif s[y]==0:
         return False

    return True
    
    




main()