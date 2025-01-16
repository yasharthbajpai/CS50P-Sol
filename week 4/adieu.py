import inflect

p = inflect.engine()

def main ():
    items = []
    while True:
        try:
             x= input("Name: ")
             items.append(x)
        except EOFError:
            break

    result_tuple = tuple(items)
    mylist = p.join((result_tuple))
    print( "Adieu, adieu, to " + mylist)
main()

         
