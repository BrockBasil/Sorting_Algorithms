#!/usr/bin/env python3
import sys

#This program reads a text file containing integers into a list. Next the list
#is sorted with a quick sort method using the first element of each array and
#subarray as the pivot. Finally the sorted list is printed to the screen.

#Increases recursion limit
sys.setrecursionlimit(10**6)

#Partitions an array from start index to end index.
#Uses value at array[start] as pivot.
#Returns index of the value that is now in its correct position in the list
def partition(array, start, end):
	pivot = array[start]
	last_low = start
	i = start + 1

	while i <= end:
		if array[i] < pivot:
			last_low = last_low + 1
			array[last_low], array[i] = array[i], array[last_low]

		i = i + 1

	array[last_low], array[start] = array[start], array[last_low]
	return last_low

#Takes in array with start and end indecies. returns if size == 1.
def quick_sort(array, start, end):
	if (start >= end):
		return

	p = partition(array, start, end)
	quick_sort(array, start, p-1)
	quick_sort(array, p+1, end)


#Opens data file and reads into list. Runs quick sort and prints sorted array.
def main():
	array = []
	with open("data.txt", "r") as f:
		for line in f:
			array.append(int(line))
	f.close()

	quick_sort(array, 0, len(array) - 1)
	print(array)

#Executes main function
if __name__ == "__main__":
	main()
