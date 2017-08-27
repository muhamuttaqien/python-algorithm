
def binary_search(sorted_collection, item):

    left = 0
    right = len(sorted_collection) -1

    while left <= right:
        midpoint = (left + right) // 2
        current_item = sorted_collection[midpoint]
        if current_item == item:
            return midpoint
        else:
            if item < current_item:
                right = midpoint - 1
            else:
                left = midpoint + 1
    
    return None


def __assert_sorted(collection):

    if collection != sorted(collection):
        raise ValueError('Collection must be sorted')

    return True


def main():
    print("=== Binary Search (Algorithm) - A half-interval search, logarithmic search, or binary search that finds the position of a target value within a sorted array. Binary search compares the target value to the middle element of the array")
    
    import sys

    user_input = raw_input("Enter numbers separated by a comma: ")
    collection = [int(item) for item in user_input.split(',')]

    try:
        __assert_sorted(collection)
    except ValueError:
        sys.exit('Sequence must be sorted to apply binary search')


    target_input = input("Enter single number to be found in the list: ")
    target = int(target_input)

    result = binary_search(collection, target)

    if result is not None:
        print("{} found at position: {}".format(target, result))
    else:
        print("Not found")


if __name__=='__main__':
	main()