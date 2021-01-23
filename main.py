import sys

from parseData import getData

data = getData()
print(data)

if __name__ == "__main__":
    print(f"Argument: {sys.argv[0]}")