"""
This program reads a list of numbers from the user, computes their sum, average, and maximum,
and then prints these values.
Changes: 
- 260205: Added functionality to compute average and maximum.
"""

numbers = []
while True:
	num = int(input("Enter a number (0 to stop): "))
	if num == 0:
		break
	numbers.append(num)

# Compute the sum
total = sum(numbers)

# Compute the average
if numbers:
	average = total / len(numbers)
else:
	average = 0

# Find the maximum
if numbers:
	maximum = max(numbers)
else:
	maximum = None

print(f"Sum: {total}")
print(f"Average: {average}")
print(f"Maximum: {maximum}")
