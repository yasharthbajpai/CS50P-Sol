from datetime import date, datetime
import inflect

def minutes_since_birth(birth_date):
    today = date.today()
    delta = today - birth_date
    total_minutes = delta.days * 24 * 60
    p = inflect.engine()
    minutes_in_words = p.number_to_words(total_minutes, andword="")
    return minutes_in_words

def main():
    birth_date_str = input("Enter your date of birth (YYYY-MM-DD): ")
    try:
        birth_date = datetime.strptime(birth_date_str, "%Y-%m-%d").date()
        minutes_in_words = minutes_since_birth(birth_date)
        print(f"You are {minutes_in_words} minutes old.")
    except ValueError:
        print("Invalid date format. Please use YYYY-MM-DD.")

if __name__ == "__main__":
    main()
