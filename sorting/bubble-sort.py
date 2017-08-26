
def bubble_sort(collection):

    length = len(collection)
    for i in range(length-1, -1, -1):
        for j in range(i):
            if collection[j] > collection[j+1]:
                collection[j], collection[j+1] = (
                    collection[j+1], collection[j]
                )

    return collection

def main():
    print("=== Bubble Sort (Algorithm) - A simple algorithm that repeatedly steps through the list to be sorted. The algorithm is named for the way smaller or larger elements 'bubble' to the top of the list")
    user_input = raw_input("Enter numbers separated by a comma: ")
    unsorted = [int(item) for item in user_input.split(',')]
    print(bubble_sort(unsorted))

if __name__=='__main__':
	main()