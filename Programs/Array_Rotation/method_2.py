# This method uses the rotation by one
# Time Complexity: O(d*n) n -> length of array
# Space Complexity: O(1)
def rotate_array_left(arr,d):
    n = len(arr)
    for i in range(0,d):
        temp = arr[0]
        for j in range(0,n-1):
            arr[j] = arr[j+1]
        arr[n-1] = temp
    return arr

originalArray = [1,2,3,4,5,6,7,8]
d=2
print('Origninal array: {}\n'.format(originalArray))
resultArray = rotate_array_left(originalArray,2)
print('Array after rotatation of {} elements towards left:{}\n'.format(d,resultArray))