#!/usr/bin/env python3
import time
import insertionSort
import quickSortFirst

def main():
	start = time.time() 
	insertionSort.main()
	end = time.time()
	print("Insertion Sort: {:.5f} seconds".format(end - start))

	start = time.time() 
	quickSortFirst.main()
	end = time.time()
	print("Quick Sort: {:.5f} seconds".format(end - start))

if __name__ == "__main__":
	main()