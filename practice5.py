data = [10, 20, 30, 40, 50] 


def calculate_moving_average(data, window_size):
    result = []
    if window_size > len(data):
        print('Window size must be less than data integers number')
        return []
    for start in range(0, len(data) - window_size + 1):
        window_sum = 0
        for i in range(start, window_size + start):
            window_sum += data[i]
        average = window_sum / window_size
        result.append(average)


    return result
         
        
    

print(calculate_moving_average([10, 20, 30, 40, 50], 3))
print(calculate_moving_average([1, 2, 3, 4, 5], 2))

print(calculate_moving_average([5, 10, 15], 5))
print(calculate_moving_average([8, 12], 1))