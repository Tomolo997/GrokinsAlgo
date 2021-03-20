# binary searchđ
def binarySearch(mylist, item):
    # initial parameters
    low = 0
    high = len(mylist) - 1
    # while loop, dokler, low ni večja od higha
    while low <= high:
        mid = (low + high) / 2
        # mid je premikajoči se index
        # guess je pa številka tega indexa
        guess = mylist[round(mid)]
        # če je guess enaki itemu, potem returnaj guess
        if guess == item:
            return round(mid)
        # če je guess večji od itema, potem je high mid -1
        if guess > item:
            high = mid - 1
        else:
            low = mid + 1
    return None


my_list = [1, 3, 5, 7, 8, 9]
print(binarySearch(my_list, 7))
