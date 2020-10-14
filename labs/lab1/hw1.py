if __name__ == '__main__':
	arr = {(float(i))**2 for i in input().split()}
	arr = list(arr)
	arr.sort()
	print(*arr)