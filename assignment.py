def replace_value(values, index, new_value):
    values[index] = new_value
    return None

def find_first(values, target):
    for i in range(len(values)):
        if values[i] == target:
            return i
    return -1

def summarize(values):
    stats_record = (min(values), max(values), sum(values))
    return stats_record


num_days = int(input("Enter the number of days: "))

original = []
for i in range(num_days):
    sleep_time = int(input("Enter sleep time in hours: "))
    original.append(sleep_time)
updated = original[:]
index_correct = int(input("Enter the index to correct: "))
new_time = int(input("Enter the new sleep time: "))
replace_value(updated, index_correct, new_time)
target = int(input("Enter the sleep time to search for: "))
first_index = find_first(updated, target)
target_count = updated.count(target)
stats_record = summarize(updated)
minimum, maximum, total = stats_record
sorted_updated = sorted(updated)
print(f"Original: {original}")
print(f"Updated: {updated}")
print(f"Sorted: {sorted_updated}")
print(f"Minimum sleep time: {minimum} hours")
print(f"Maximum sleep time: {maximum} hours")
print(f"Total sleep time: {total} hours")
    
if first_index != -1:
    print(f"First matching index: {first_index}")
else:
    print("Target not found")
        
print(f"Matching values: {target_count}")
