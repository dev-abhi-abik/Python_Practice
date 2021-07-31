# This method uses the temp array to rotate the array by 'd' elements towards left
# Time Complexity: O(n) n -> length of array
# Space Complexity: O(d) d -> elements to be rotated
def rotate_array_left(arr,d):
    n = len(arr)
    temp = list()
    for i in range(0,d):
        temp.append(arr[i])
    i = 0
    while d<n:
        arr[i] = arr[d]
        i += 1
        d += 1
    arr = arr[:i] + temp
    return arr 


originalArray = [1,2,3,4,5,6,7,8]
d=2
print('Origninal array: {}\n'.format(originalArray))
resultArray = rotate_array_left(originalArray,2)
print('Array after rotatation of {} elements towards left:{}\n'.format(d,resultArray))