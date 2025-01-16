import sys
import pyfiglet
import random


argv1 = ("-f" , "--font")
   

def main():
    if len(sys.argv) == 2 :
        if sys.argv[1] in argv1: 
         x= input("Input: ") 
         out = pyfiglet.figlet_format(x, font=sys.argv[2])
         print(out)
    elif len(sys.argv) == 1:
           x= input("Input: ")
           out = pyfiglet.figlet_format(x, font=random.choice(pyfiglet.FigletFont.getFonts()))
           print(out)
    else:
        sys.exit("Invalid usage")

        
main()