days_input = int(input("please enter the days: "))
year = days_input // 365
remaining_days = days_input % 365
month = remaining_days // 30
remaining_days = remaining_days % 30
print(f"{days_input} equals {year} year، {month}months and{remaining_days} days.")
