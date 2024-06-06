numbers = [2,3,4]
target = 6
target=9
numbers_index = list(enumerate(numbers))
left, right = 0, len(numbers) - 1

while left < right:
    sum = numbers_index[left][1] + numbers_index[right][1]
    if sum == target:
        print([numbers_index[left][0]+1, numbers_index[right][0]+1]) 
        break
    elif sum < target:
        left += 1
    else:
        right -= 1

