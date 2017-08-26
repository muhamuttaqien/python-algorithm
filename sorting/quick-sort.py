
def quick_sort(collection):

    length = len(collection)

    if (length <= 1):
        return collection
    else:
        pivot = collection[0]
        greater = [item for item in collection[1:] if item > pivot]
        lesser = [item for item in collection[1:] if item <= pivot]

        return quick_sort(lesser) + [pivot] + quick_sort(greater)

def main():
    print("=== Quick Sort (Algorithm) - An efficient sorting algorithm, serving as a systematic method for placing the elements of an array in order. It is still commonly used algorithm for sorting which is faster than its main competitors, merge-sort and heap-sort")
    numbers = raw_input("Enter numbers separated by a comma: ")
    unsorted = [int(item) for item in numbers.split(',')]
    print(quick_sort(unsorted))

if __name__=='__main__':
	main()