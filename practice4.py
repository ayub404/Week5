def find_longest_run(data):
    if not data:
        return 0
    current = 1
    longest = 1
    char = []
    for i in range(1, len(data)):
        if data[i] == data[i-1]:
            current += 1
            longest = max(current, longest)
            
            
        else:
            current = 1
  
    return longest
    
        
data = [1,2,2,2,2,2,2,2,5,5,5,5,5]
print(find_longest_run(data))


