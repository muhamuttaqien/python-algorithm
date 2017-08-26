
def selection_sort(collection):

    length = len(collection)
    for i in range(length):
        least = i

        for k in range(i + 1, length):
            if collection[k] < collection[least]:
                least = k

        collection[least], collection[i] = (
            collection[i], collection[least]
        )

    return collection

def main():
    print("=== Selection Sort (Algorithm) - A sorting algorithm that has thime complexity, making it inefficient on large lists, and generally performs worse than the other similar sort")
    user_input = raw_input("Enter numbers separated by a comma: ")
    unsorted = [int(item) for item in user_input.split(',')]
    print(selection_sort(unsorted))

if __name__=='__main__':
	main()