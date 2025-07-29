"""
Personal Finance Calculator
Student: [Your Name]
Date: July 26, 2025
Purpose: Calculate monthly budget and savings based on user's income and expenses.
"""

# --- Input Data ---
# This section prompts the user to enter their financial information.

# Get monthly income from the user (in THB)
monthly_income = float(input("Enter your monthly income (THB): "))

# Get monthly rent/housing cost
rent_cost = float(input("Enter your monthly rent/housing cost (THB): "))

# Get monthly food budget (as an integer)
food_budget = int(input("Enter your monthly food budget (THB): "))

# Get monthly transportation expenses
transportation_cost = float(input("Enter your monthly transportation expenses (THB): "))

# Get monthly entertainment budget (as an integer)
entertainment_budget = int(input("Enter your monthly entertainment budget (THB): "))

# Get the percentage of income to save for emergencies
emergency_fund_percent = float(input("Enter the percentage of income to save for emergencies (e.g., 10.5): "))

# Get the percentage of income to invest
investment_percent = float(input("Enter the percentage of income to invest (e.g., 15.0): "))

# --- Calculations ---
# This section performs all the necessary financial calculations.

# Calculate total fixed expenses (rent + transportation)
total_fixed_expenses = rent_cost + transportation_cost

# Calculate total variable expenses (food + entertainment)
total_variable_expenses = food_budget + entertainment_budget

# Calculate total expenses (fixed + variable expenses)
total_expenses = total_fixed_expenses + total_variable_expenses

# Calculate remaining income after all expenses
remaining_income = monthly_income - total_expenses

# Calculate the emergency fund amount based on the given percentage of income
emergency_fund_amount = monthly_income * (emergency_fund_percent / 100)

# Calculate the investment amount based on the given percentage of income
investment_amount = monthly_income * (investment_percent / 100)

# Calculate the amount available for additional savings after emergency fund and investment
available_for_savings = remaining_income - emergency_fund_amount - investment_amount

expense_ratio = (total_expenses / monthly_income) * 100

# --- Output ---

print("\n=== MONTHLY BUDGET REPORT ===")
print(f"Income: {monthly_income:.2f} THB")
print(f"Fixed Expenses: {total_fixed_expenses:.2f} THB")
print(f"Variable Expenses: {total_variable_expenses:.2f} THB")
print(f"Total Expenses: {total_expenses:.2f} THB")
print(f"Remaining: {remaining_income:.2f} THB")

print("\n=== SAVINGS BREAKDOWN ===")
print(f"Emergency Fund ({emergency_fund_percent:.0f}%): {emergency_fund_amount:.2f} THB")
print(f"Investment ({investment_percent:.0f}%): {investment_amount:.2f} THB")
print(f"Available for Savings: {available_for_savings:.2f} THB")

print("\n=== ANALYSIS ===")
print(f"Expense Ratio: {expense_ratio:.2f}%")