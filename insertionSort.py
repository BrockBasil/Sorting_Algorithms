#!/usr/bin/env python3

#Parse through list and inserts each element into correct position
def insertionSort(array): 
	i = 0

	while i < len(array): 
		holder = array[i] 

		j = i - 1
		while j >= 0 and holder < array[j] : 
				array[j + 1] = array[j] 
				j = j - 1
		array[j + 1] = holder
		i = i + 1

#Main driver function. Reads integers from text file into list to be sorted.
def main():
	array = []
	with open("data.txt", "r") as f:
		for line in f:
			array.append(int(line))
	f.close()

	insertionSort(array)

#Executes main function
if __name__ == "__main__":
	main()