import sys


if __name__ == "__main__":
    g = (int(x) for x in sys.argv[1:])
    total_sum = 0
    for i in g:
        total_sum += i
    print(total_sum)
