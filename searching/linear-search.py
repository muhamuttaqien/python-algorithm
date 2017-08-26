
def linear_search(sequence, target):

    for index, item in enumerate(sequence):
        if item == target:
            return index

    return None

def main():
    print("=== Linear Search (Algorithm) - An efficient, general-purpose, comparison-based sorting algorithm which most implementations produce a stable sort. Merge-sort is a divide and conquer algorithm")
    user_input = raw_input("Enter numbers separated by a comma: ")
    sequence = [int(item) for item in user_input.split(',')]

    target_input = input("Enter single number to be found in the list: ")
    target = int(target_input)

    result = linear_search(sequence, target)

    if result is not None:
        print("{} found at position: {}".format(target, result))
    else:
        print("Not found")

if __name__=='__main__':
	main()