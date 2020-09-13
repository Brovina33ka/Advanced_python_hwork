if __name__ == __main__:
    arr = [(float(i))**2 if '.' in i else (int(i))**2 for i in input().split()]
    for i in arr:
        print(i)