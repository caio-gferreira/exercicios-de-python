array = [3,5,4,1,2]

def odernaArray(array):
    for i in range(len(array)):
        for j in range(len(array) - 1):
            if array[j] > array[j+1]:
                array[j], array[j+1] = array[j+1], array[j]
    return array

print(odernaArray(array))
            
    