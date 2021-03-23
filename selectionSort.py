def findSmallest(arr):
    # najmanši je prvi index
    smallest = arr[0]
    # najmanjpi index je 0
    smallestIndex = 0
    for i in range(1, len(arr)):
        # če je v arrayu trenutni element manjši od tvojega
        if arr[i] < smallest:
            # potem postavimo najmanšega kot ta trenuten element
            smallest = arr[i]
            smallestIndex = i
    return smallestIndex


def selectionSort(arr):
    newArr = []
    for i in range(len(arr)):
        # najdemo najmanšega v trenutnem arrayu
        smallets = findSmallest(arr)
        newArr.append(arr.pop(smallets))
    return newArr


print(selectionSort([5, 3, 6, 2, 10]))
