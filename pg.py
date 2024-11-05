# Elijah Gertsch
# Lab Section 11
# Submission Date 11/04/2024
# Sources, help given to/received from:

def leap_yr(year):
    if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
        return True
    return False

def jan_first_weekday(year):
    y = year - 1
    weekday = (36 + y + (y // 4) - (y // 100) + (y // 400)) % 7
    return weekday

def days_in_month(month, year):
    days_in_months = {
        1: 31, 2: 28, 3: 31, 4: 30, 5: 31, 6: 30,
        7: 31, 8: 31, 9: 30, 10: 31, 11: 30, 12: 31
    }
    if month == 2 and leap_yr(year):
        return 29
    return days_in_months.get(month, 0)

def valid_date(month, day, year):
    if month < 1 or month > 12:
        return False
    if day < 1 or day > days_in_month(month, year):
        return False
    if year < 1000 or year > 9999:
        return False
    return True

def day_of_week(month, day, year):
    if not valid_date(month, day, year):
        return "Invalid Date"
    start_day = jan_first_weekday(year)
    days_in_previous_months = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    if leap_yr(year):
        days_in_previous_months[1] = 29
    days_passed = sum(days_in_previous_months[:month - 1]) + (day - 1)
    weekday = (start_day + days_passed) % 7
    days_of_week = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"] 
    return days_of_week[weekday]

def main():
    date_input = input("Enter date with the format (MM/DD/YYYY): ").strip()
    try:
        month, day, year = map(int, date_input.split('/')) 
        result = day_of_week(month, day, year)
        print(f"{date_input} {result}")
    except ValueError:
        print("Invalid Date")

if __name__ == "__main__":
    main()
