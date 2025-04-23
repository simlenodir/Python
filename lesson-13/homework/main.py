# Bismilah
# Task 1
from datetime import time, date, datetime

birthday = input('Enter your birthday as "08-29-1993": ')
birth_date = datetime.strptime(birthday, "%d-%m-%Y")
today = datetime.today()
age = today.year - birth_date.year
month = today.month - birth_date.month
day = today.day - birth_date.day

if(birth_date.month, birth_date.day) > (today.month, today.day):
    age -= 1
if(month < 0):
    month += 12

if day < 0:
    day = 31 + day
    month -= 1

print(f'Your age:{age} month: {month}, day: {day}')
print(month)

# Task 1 2-way solution
#  Task 2 Calculate next birthday
birth_date = input("Enter your birthday like (YYYY-MM-DD): ")
try:
    birth_day = datetime.strptime(birth_date, "%Y-%m-%d").date()
    today = datetime.today().date()

    last_month = birth_day.month - today.month
    last_day = birth_day.day - today.day
    
    if last_month < 0:
        last_month = 12 + last_month
    if last_day < 0:
        last_day += 30

    print(f"Your next birthay comes after month: {last_month}, after day: {last_day}")
except ValueError:
    
# Task 2 2-way of solution
  birth_date = input("Enter your birthday like (YYYY-MM-DD): ")
try:
    birth_day = datetime.strptime(birth_date, "%Y-%m-%d").date()
    today = date.today()

    next_birthday = birth_day.replace(year=today.year)
    if(next_birthday) < today:
        next_birthday = birth_day.replace(year=today.year + 1)
    
    time_remaining = relativedelta(next_birthday,  today)
    print(next_birthday)
    
    print(f"Your next birthay comes after month: {time_remaining.months}, after day: {time_remaining.days}")
except ValueError:
    print("Invalid date format. Please use YYYY-MM-DD.")

from datetime import datetime, timedelta

# Get current date and time from the user
current_dt_str = input("Enter the current date and time (YYYY-MM-DD HH:MM): ")

try:
    current_dt = datetime.strptime(current_dt_str, "%Y-%m-%d %H:%M")

    # Get duration from user
    hours = int(input("Enter meeting duration - Hours: "))
    minutes = int(input("Enter meeting duration - Minutes: "))

    # Calculate end time
    duration = timedelta(hours=hours, minutes=minutes)
    end_time = current_dt + duration

    print(f"The meeting will end at: {end_time.strftime('%Y-%m-%d %H:%M')}")
except ValueError:
    print("Invalid input. Please use the correct formats.")

from datetime import datetime
import pytz

def timezone_converter():
    print("Timezone Converter")
    print("------------------")
    
    # Get user input
    date_str = input("Enter date (YYYY-MM-DD): ")
    time_str = input("Enter time (HH:MM:SS): ")
    original_timezone_str = input("Enter your current timezone (e.g., America/New_York, Europe/London): ")
    target_timezone_str = input("Enter target timezone (e.g., Asia/Tokyo, Australia/Sydney): ")
    
    try:
        # Combine date and time
        datetime_str = f"{date_str} {time_str}"
        naive_datetime = datetime.strptime(datetime_str, "%Y-%m-%d %H:%M:%S")
        
        # Get timezone objects
        original_timezone = pytz.timezone(original_timezone_str)
        target_timezone = pytz.timezone(target_timezone_str)
        
        # Localize the datetime to the original timezone
        localized_datetime = original_timezone.localize(naive_datetime)
        
        # Convert to target timezone
        target_datetime = localized_datetime.astimezone(target_timezone)
        
        # Format the output
        print("\nConversion Result:")
        print(f"Original time: {localized_datetime.strftime('%Y-%m-%d %H:%M:%S %Z%z')}")
        print(f"Converted time: {target_datetime.strftime('%Y-%m-%d %H:%M:%S %Z%z')}")
        
    except ValueError as e:
        print(f"\nError: {e}")
        print("Please check your input format and timezone names.")
    except pytz.exceptions.UnknownTimeZoneError:
        print("\nError: Unknown timezone. Please use the format 'Continent/City' (e.g., 'America/New_York')")

if __name__ == "__main__":
    timezone_converter()

import time
from datetime import datetime

# Ask user to enter the future date and time
user_input = input("Enter the future date and time (YYYY-MM-DD HH:MM:SS): ")

# Convert the input string into a datetime object
try:
    future_time = datetime.strptime(user_input, "%Y-%m-%d %H:%M:%S")
except ValueError:
    print("Invalid format. Please use YYYY-MM-DD HH:MM:SS")
    exit()

# Check if the entered time is in the future
if future_time <= datetime.now():
    print("The entered time is not in the future.")
    exit()

# Countdown loop
print("\nCountdown started:")
while True:
    now = datetime.now()
    remaining = future_time - now
    
    if remaining.total_seconds() <= 0:
        print("Countdown complete!")
        break

    # Format remaining time
    days = remaining.days
    hours, remainder = divmod(remaining.seconds, 3600)
    minutes, seconds = divmod(remainder, 60)
    
    print(f"\rTime remaining: {days}d {hours:02}h {minutes:02}m {seconds:02}s", end="")
    time.sleep(1)

import re

# Regular expression pattern for a basic email validation
email_pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'

# Ask the user to input an email address
email = input("Enter an email address to validate: ")

# Validate using regex
if re.match(email_pattern, email):
    print("Valid email address.")
else:
    print("Invalid email address.")

def format_phone_number(phone):
    # Remove any non-digit characters
    digits = ''.join(filter(str.isdigit, phone))

    if len(digits) != 9:
        return "Invalid phone number. Please enter exactly 9 digits."

    # Format: (12) 345-67-89
    formatted = f"({digits[0:2]}) {digits[2:5]}-{digits[5:7]}-{digits[7:9]}"
    return formatted

# Get user input
user_input = input("Enter a 9-digit phone number: ")
formatted_number = format_phone_number(user_input)

print("Formatted number:", formatted_number)


import re

def check_password_strength(password):
    # Criteria checks
    length_ok = len(password) >= 8
    has_upper = re.search(r'[A-Z]', password) is not None
    has_lower = re.search(r'[a-z]', password) is not None
    has_digit = re.search(r'\d', password) is not None

    print("\nPassword Strength Check:")
    print(f"✔ Minimum length (8): {'OK' if length_ok else 'Missing'}")
    print(f"✔ At least one uppercase letter: {'OK' if has_upper else 'Missing'}")
    print(f"✔ At least one lowercase letter: {'OK' if has_lower else 'Missing'}")
    print(f"✔ At least one digit: {'OK' if has_digit else 'Missing'}")

    if all([length_ok, has_upper, has_lower, has_digit]):
        print("\n✅ Your password is strong.")
    else:
        print("\n❌ Your password is weak. Please improve it.")

# Ask the user for a password
user_password = input("Enter a password to check its strength: ")
check_password_strength(user_password)

# Task 9 
import re 

# Sample text to search in
sample_text = """
Python is a powerful programming language. Python can be used for web development,
data analysis, artificial intelligence, and more. Many developers love Python for its simplicity.
"""

# Users word for search
word = input("Enter the word to search fro: ")

# Use regular expression for whole word matching, case-insensitive
pattern = r'\b' + re.escape(word) + r'\b'
matches = list(re.finditer(pattern, sample_text, flags=re.IGNORECASE))

# Show matches
if matches:
    print(f"Found '{word}': {len(matches)} time(s):")
    for match in matches:
        print(f"- At index {match.start()}: '{match.group()}'")
else:
    print(f"No occurences of '{word}' found.")



# 10 task
import re 

text = """ 
    Our meetings are scheduled on 12/05/2024, 15-06-2024 and 2025-04-23.
"""

# Regular expression to match dates
date_pattern = r'\b(?:\d{1,2}[/-]\d{1,2}[/-]\d{2,4}|\d{4}-\d{1,2}-\d{1,2})\b'

# Find all matching dates
dates = re.findall(date_pattern, text)

# Print results
if dates:
    print("Dates found in the text: ")
    for date in dates:
        print(f" - {date}")
else:
    print("No dates found in the text")
