def binarySearch(anArray, anItem):
    low = 0
    high = len(anArray) -1

    while low <= high:
        mid = (low + high) //2
        if anArray[mid] == anItem:
            return mid
        elif anItem < anArray[mid]:
            high = mid - 1
        else:
            low = mid + 1
    return -1

nums = [10, 30, 40, 45, 70, 80, 85, 90, 100]
words = ["at", "ball", "cat", "dog", "eye", "fish", "good"]
print(binarySearch(nums, 80))        
print(binarySearch(words, "ball"))    