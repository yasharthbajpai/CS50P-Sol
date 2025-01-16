import re
import sys

def main():
    try:
        ip = input("IPv4 Address: ")
        result = validate(ip)
        print(result)
    except KeyboardInterrupt:
        print("\nProgram interrupted.")
        sys.exit(1)

def validate(ip):
    ipv4_pattern = r'^(?:(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.){3}(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)$'
    
    if re.match(ipv4_pattern, ip):
        return "Valid"
    else:
        return "Invalid"

if __name__ == "__main__":
    main()
