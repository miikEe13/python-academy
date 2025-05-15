numbers = [15, 22, 8, 19, 31, 7, 42]

biggest = numbers[0]
lowest = numbers[0]

for number in numbers:
    if number > biggest:
        biggest = number
    if number < lowest:
        lowest = number

print(f"The lowest number is: {lowest}")
print(f"The biggest number is: {biggest}")