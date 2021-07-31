
def gcd(a,b):
    if b == 0:
        return a
    else:
       return gcd(b,a%b)

def array_rotate_left(arr,d):
    n = len(arr)
    for i in range(gcd(n,d)):
        temp = arr[i]
        j = i
        while 1:
            k = j + d
            if k >= n:
                k = k-n
            if k == i:
                break
            arr[j] = arr[k]
            j = k
            arr[j] = temp
    return arr

array = [1,2,3,4,5,6,7,8,9,10,11,12,13,14]
print('Orginal Array :{}'.format(array))

result_array = array_rotate_left(array,13)
print('Result Array :{}'.format(result_array))

