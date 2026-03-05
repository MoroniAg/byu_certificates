"""
Title: Life Expectancy Data Analysis
Program: CSEPC110 - Introduction to Programming
Author: Moroni Aguilera

This code reads a CSV file containing life expectancy data, processes the data to find the minimum and maximum life expectancy values, and then prints those values. 
The CSV file is expected to have a header row, which is skipped during processing.

Changes:
- 260210: Initial implementation of life expectancy data analysis.
- 260214: Added functionality to find the largest drop in life expectancy between consecutive years for each country.

"""
print("|-------------------------------|\n| Life Expectancy Data Analysis |\n|-------------------------------|\n")


with open('1_certificate/csepc110/w6/life-expectancy.csv', 'r') as file:
	lines = file.readlines()

data_lines = lines[1:]

min_life_expectancy = float('inf')
max_life_expectancy = float('-inf')
min_details = None
max_details = None

all_data = []

for line in data_lines:
	parts = line.strip().split(',')
	country = parts[0]
	year = parts[2]
	life_expectancy = float(parts[3])
	all_data.append((country, year, life_expectancy))
	if life_expectancy < min_life_expectancy:
		min_life_expectancy = life_expectancy
		min_details = (country, year)
	if life_expectancy > max_life_expectancy:
		max_life_expectancy = life_expectancy
		max_details = (country, year)

print(f"Lowest life expectancy: {min_life_expectancy} ({min_details[0]}, {min_details[1]})")
print(f"Highest life expectancy: {max_life_expectancy} ({max_details[0]}, {max_details[1]})")

largest_drop = 0
drop_country = None
drop_year = None
prev_values = {}

for country, year, life_expectancy in all_data:
	if country in prev_values:
		drop = prev_values[country] - life_expectancy
		if drop > largest_drop:
			largest_drop = drop
			drop_country = country
			drop_year = year
	prev_values[country] = life_expectancy
if largest_drop > 0:
	print(f"Largest drop: {drop_country} in {drop_year} ({largest_drop:.2f} years)")

year_of_interest = input("Enter the year of interest: ").strip()
year_data = [(country, float(life)) for country, year, life in all_data if year == year_of_interest]
if year_data:
	avg_life = sum(life for country, life in year_data) / len(year_data)
	max_country, max_life = max(year_data, key=lambda x: x[1])
	min_country, min_life = min(year_data, key=lambda x: x[1])
	print(f"\nFor the year {year_of_interest}:")
	print(f"The average life expectancy across all countries was {avg_life:.2f}")
	print(f"The max life expectancy was in {max_country} with {max_life:.2f}")
	print(f"The min life expectancy was in {min_country} with {min_life:.3f}")
else:
	print(f"No data found for year {year_of_interest}.")
