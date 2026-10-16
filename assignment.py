total_weight = 0
below_range = 0
in_range = 0
above_range = 0 

def classify(value):
    if value < 498:
        return "Below range"
    elif value >= 498 and value <= 502:
        return "In range"
    elif value > 502:
        return "Above range"

def calculate_average(total, count):
    average = total / count
    return average

number_bags = int(input("Enter the number of rice bags: "))

for i in range(number_bags):
    weight = int(input("Enter the rice bag weight: "))

    category = classify(weight)
    print(category)

    total_weight = total_weight + weight

    if category == "Below range":
        below_range += 1
    elif category == "In range":
        in_range += 1
    elif category == "Above range":
        above_range += 1

average_weight = calculate_average(total_weight, number_bags)
print(f"Total weight: {total_weight} g")
print(f"Average weight: {average_weight} g")
print(f"Below range: {below_range}")
print(f"In range: {in_range}")
print(f"Above range: {above_range}") 
