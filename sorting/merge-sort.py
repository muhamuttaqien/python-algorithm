
def merge_sort(collection):

    length = len(collection)

    if length > 1:
        midpoint = length // 2
        left_half = merge_sort(collection[:midpoint])
        right_half = merge_sort(collection[midpoint:])
        i = 0
        j = 0
        k = 0
        left_length = len(left_half)
        right_length = len(right_half)

        while i < left_length and j < right_length:
            if left_half[i] < right_half[j]:
                collection[k] = left_half[i]
                i += 1
            else:
                collection[k] = right_half[j]
                j += 1
            k += 1

        while i < left_length:
            collection[k] = left_half[i]
            i += 1
            k += 1

        while j < right_length:
            collection[k] = right_half[j]
            j += 1
            k += 1

    return collection


def main():
    print("=== Merge Sort (Algorithm) - An efficient, general-purpose, comparison-based sorting algorithm which most implementations produce a stable sort. Merge-sort is a divide and conquer algorithm")
    numbers = raw_input("Enter numbers separated by a comma: ")
    unsorted = [int(item) for item in numbers.split(',')]
    print(merge_sort(unsorted))

if __name__=='__main__':
	main()