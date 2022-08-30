#Write a program to implement Binary Search
#Creating a function s
def binarySearch(arr, key):
    start = 0
    end = len(arr) - 1
    while start <= end:
        mid = (start + end)//2
        if(arr[mid] == key):
            return mid
        elif(arr[mid] < key):
            start = mid + 1
        else:
            end = mid - 1
    return -1

arr = [12,23,26,29,30,100,198]
print("Enter the number which you want to find in the array: ")
num = int(input())
index = binarySearch(arr, num)
if(index == -1):
    print("Element which you entered was not found.")
else:
    print("Element is present at index", index)