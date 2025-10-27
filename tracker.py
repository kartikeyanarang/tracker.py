"""
This mini 
project aims to help them build a Python-based CLI (Command Line Interface) tool where they 
can log their meals and keep track of total calories consumed, compare against a personal daily 
limit, and save session logs for future tracking
Made by: Kartikeya Narang
Date: 17/10/25
Title: Daily Calorie Intake Tracker
"""
print("Welcome to the Daily Calorie Tracker")
print("This tool helps you record your meals, calculate total and average calorie intake")
meal_names = []
calorie_values = []
num_meals = int(input("How many meals would you like to Eat"))
for i in range(num_meals):
    print(f"\nMeal no. {i + 1}")
    meal = input("Enter meal name: ")
    calories = float(input("Enter calorie amount: "))
    meal_names.append(meal)
    calorie_values.append(calories)
total_calories = sum(calorie_values)
average_calories = total_calories / len(calorie_values)
daily_limit = float(input("\nEnter your daily calorie limit: "))
if total_calories > daily_limit:
    current = "You exceeded your daily calorie limit"
elif total_calories == daily_limit:
    current = "You hit your exact calorie limit"
else:
    current = "You're under your calorie limit"
for meal, cal in zip(meal_names, calorie_values):
    print(f"{meal:<15}\t{cal:.2f}")

print("-------------------------------------------")
print(f"Total Calories:\t\t{total_calories:.2f}")
print(f"Average per Meal:\t{average_calories:.2f}")
print(f"Daily Limit:\t\t{daily_limit:.2f}")