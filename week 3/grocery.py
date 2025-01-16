def main():
    c=[]
    while True:
        try:
            x = input ().title()
            c.append(x)
        except EOFError:
            break
    """
    w=1
    for i in range(len(c)):
        print(f"{w}. {c[i]}")
        w+=1"""
    for i , item in enumerate(c, 1):
        print(f"{i}. {item}")            
main()
         