def binary_search(list,target):
    first = 0
    last = len(list) - 1
    count = 1
    while first <= last:
        midpoint = (first + last)//2 
        if list[midpoint] == target:
            print('It took this many steps:', count)
            return midpoint
        elif list[midpoint] < target:
            first = midpoint + 1
            count +=1 
        else:
            last = midpoint - 1
            count +=1

def verify(index):
    return print('the value was found at index:',index)

numbers=[1,2,3,4,5,6,7,8,9,10]

result = binary_search(numbers,8)
verify(result  )


