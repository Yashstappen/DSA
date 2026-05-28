arr = [5,7,3,2,6,1,5,9]
left = 2
right = 5

def func(array, l, r):
    if l>=r:
        return 
    array[l], array[r] = array[r],array[l]
    func(array, l+1, r-1)

def reverse(arr, left, right):
    func(arr, left, right)
    return arr

print(reverse(arr, left, right))