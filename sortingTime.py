#!/usr/bin/env python3
import time
import random
import insertionSort
import quickSortFirst
import mergeSort

def randomize_data():
	array = []
	with open("data.txt", "r") as f:
		for line in f:
			array.append(int(line))
	f.close()

	random.shuffle(array)
	
	with open('data.txt', 'w') as f:
		for num in array:
			f.write("%i\n" % num)
	f.close()

	print("Data in data.txt randomized")

def main():
	randomize_data()

	start = time.time() 
	insertionSort.main()
	end = time.time()
	print("Insertion Sort: {:.5f} seconds".format(end - start))

	start = time.time() 
	mergeSort.main()
	end = time.time()
	print("Merge Sort: {:.5f} seconds".format(end - start))	

	start = time.time() 
	quickSortFirst.main()
	end = time.time()
	print("Quick Sort: {:.5f} seconds".format(end - start))

if __name__ == "__main__":
	main()