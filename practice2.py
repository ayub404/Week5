def remove_outliers(data, min_val, max_val):
    
    for i in data:
        if i < min_val or i > max_val:
            data.remove(i)
        

    return data

measurements = [8, 5, 12, 1, 9, 20, 15]
print(f"Original measurements: {measurements}")
cleaned_list = remove_outliers(measurements, 5,15)
print(f"Cleaned measurements: {cleaned_list}")

measurements = [8, 0, 15, 29, 20, 9]
print(f"Original measurements: {measurements}")
cleaned_list = remove_outliers(measurements, 5,15)
print(f"Cleaned measurements: {cleaned_list}")

measurements = [7, 5, 12, 11, 10, 9]
print(f"Original measurements: {measurements}")
cleaned_list = remove_outliers(measurements, 5,15)
print(f"Cleaned measurements: {cleaned_list}")