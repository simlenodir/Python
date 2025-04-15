import math_functions as mf
import string_utils as su
from connect_postgres import get_connection
from geometry import calculate_circumference, calculate_area
from file_operations import read_file, write_file

conn = get_connection()
cur = conn.cursor()

# cur.execute(
#     "INSERT INTO users (name, email, password, age) VALUES (%s, %s, %s, %s)",
#     ('Nodir', 'ashjngfbvd@gmail.com', '134', 32)
# )

# conn.commit()
# print("New user inserted!")

radius = 5
area = calculate_area(radius)
circumference = calculate_circumference(radius)

output = f"Radius: {radius} circle's \narea: {area} and circumference: {circumference}"
write_file('circle_data.txt', output)

print(read_file('circle_data.txt'))


    
cur.execute("SELECT * from users;")
posts = cur.fetchall()
print(posts)

# def add_users()

cur.close()
conn.close()

print(mf.add_numbers(20, 10))
print(su.reverse_string('Hello world'))
print(su.count_wovels('Assalomu aleykum Xalq'))
