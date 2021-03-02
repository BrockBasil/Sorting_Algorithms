#!/usr/bin/env python3

def merge_sort(array):
	if len(array) > 1:
		split = len(array) // 2
		left = array[:split]
		right = array[split:]

		merge_sort(left)
		merge_sort(right)

		k = 0
		j = 0
		i = 0

		while i < len(left) and j < len(right):
			if left[i] <= right[j]:
				array[k] = left[i]
				i = i + 1
			else:
				array[k] = right[j]
				j = j + 1
			k = k + 1

		while i < len(left):
			array[k] = left[i]
			i = i + 1
			k = k + 1

		while j < len(right):
			array[k] = right[j]
			j = j + 1
			k = k + 1

def main():
	array = []
	with open("data.txt", "r") as f:
		for line in f:
			array.append(int(line))
	f.close()

	merge_sort(array)
	print(array)

#Executes main function
if __name__ == "__main__":
	main()