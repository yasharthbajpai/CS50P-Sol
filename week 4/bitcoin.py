import json
import requests
import sys



try:
    response = requests.get("https://api.coindesk.com/v1/bpi/currentprice.json")
    data = response.json()
    rate = data["bpi"]["USD"]
    amount = rate["rate_float"] * float(sys.argv[1])
    print(f"${amount:,.4f}")



except requests.RequestException:
    print("Error fetching data")
    sys.exit(1)

except IndexError:
    print("Missing command line argument")
    sys.exit(1) 

except ValueError:
    print("Command line argument is not a number")
    