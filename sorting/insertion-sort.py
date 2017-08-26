
def insertion_sort(collection):

    length = len(collection)

    for index in range(1, length):
        while 0 < index and collection[index] < collection[index-1]:
            collection[index], collection[index-1] = (
                collection[index-1], collection[index]
            )
            index -= 1
            
    return collection


def main():
    print("=== Insertion Sort (Algorithm) - An efficient, general-purpose, comparison-based sorting algorithm which most implementations produce a stable sort. Merge-sort is a divide and conquer algorithm")
    user_input = raw_input("Enter numbers separated by a comma: ")
    unsorted = [int(item) for item in user_input.split(',')]
    print(insertion_sort(unsorted))

if __name__=='__main__':
	main()