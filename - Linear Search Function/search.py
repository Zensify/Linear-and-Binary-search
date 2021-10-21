def linearSearch(anArray, anItem):
    for i in range(len(anArray)):
        if anArray[i] == anItem:
            return i
    return -1 

nums = [10, 30, 40, 45, 70, 80, 90, 100]
print(linearSearch(nums, 40))
print(linearSearch(nums, 75))