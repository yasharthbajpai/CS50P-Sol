def main():
    while True:
        try:
            fraction = input("Fraction: ")
            percentage = convert(fraction)
            result = gauge(percentage)
            print(result)
            break
        except (ValueError, ZeroDivisionError):
            pass

def convert(fraction):
    try:
        x, y = fraction.split('/')
        if not x.isdigit() or not y.isdigit():
            raise ValueError
        x, y = int(x), int(y)
        if x > y:
            raise ValueError
        if y == 0:
            raise ZeroDivisionError
        return round(x / y * 100)
    except (ValueError, ZeroDivisionError) as e:
        raise e

def gauge(percentage):
    if percentage <= 1:
        return 'E'
    elif percentage >= 99:
        return 'F'
    else:
        return f"{percentage}%"

if __name__ == "__main__":
    main()