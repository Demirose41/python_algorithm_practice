def recursive_binary_search(list, target):
    if (len(list) == 0):
        return False
    else:
        midpoint= (len(list))//2
        if list[midpoint] == target:
            return True
        else:
            if list[midpoint] < target:
                return recursive_binary_search(list[midpoint+1:], target) # [midpoint+1:] will pass a new array from the list at midpoint index to the end of the list. ':' is python shorthand for 'up to the end'
            else: 
                return recursive_binary_search(list[:midpoint], target)

def verify(result):
    print("Target Found: ", result)

numbers = [1,2,3,4,5,6,7,8,9,10]
result = recursive_binary_search(numbers, 10)
verify(result)