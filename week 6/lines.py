import sys

def count_lines(file_path):
    try:
        with open(file_path, 'r') as file:
            lines = file.readlines()
            code_lines = sum(1 for line in lines if line.strip() and not line.strip().startswith('#'))
        return code_lines
    except FileNotFoundError:
        sys.exit("File does not exist")

def main():
    if len(sys.argv) != 2:
        sys.exit("Usage: python lines.py <python_file>")
    
    file_path = sys.argv[1]
    if not file_path.endswith('.py'):
        sys.exit("Not a Python file")
    
    loc = count_lines(file_path)
    print(loc)

if __name__ == "__main__":
    main()
