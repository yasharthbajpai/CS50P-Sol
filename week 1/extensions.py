def main():
    x= input("File name: ")
    y = x.split(".")

    if y[1] == "gif":
     print(f"image/gif")   
    elif y[1] == "jpg":
        print(f"image/jpeg")   
    elif y[1] == "png":
        print(f"image/png")
    elif y[1] == "jpng":
        print(f"image/jpng")
    elif y[1] == "pdf":
        print(f"application/pdf")
    elif y[1] == "doc":
        print(f"application/msword")
    elif y[1] == "txt":
        print(f"text/plain")
    else:
        print(f"ni pata kya hai")



if __name__ == "__main__":
    main()

    