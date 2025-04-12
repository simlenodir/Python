# Task 1
import math    

class Cyrcle:
    def __init__(self, radius: int):
        self.radius = radius

    def circumferences(self):
        return round(2* self.radius * math.pi, 2)
    
    def area(self): 
        return round(math.pi * self.radius ** 2, 2)
    
c = Cyrcle(5)
print(f"area: {c.area()}, primetr: {c.circumferences()}")

from datetime import date    

class Person:
    def __init__(self, name, country, date_of_birth):
        self.name = name
        self.country = country
        self.date_of_birth = date_of_birth

    def age_person(self):
        birth_year = self.date_of_birth.split('-')[0]
        birth_month = self.date_of_birth.split('-')[1]
        birth_day = self.date_of_birth.split('-')[2]


        today = date.today()
        year = today.year
        month = today.month
        day = today.day

        age = 0
        if int(day) - int(birth_day) > 0 and int(month) - int(birth_month) > 0:
            age = int(year) - int(birth_year)
        else:
            age = int(year) - int(birth_year) - 1 

        # today - '1993-08-29'
        return  age
    
Nodir = Person('Nodir', 'Uzb', '1993-08-29')
print(f'{Nodir.name} your age: {Nodir.age_person()}')

from datetime import date, datetime

class Person1:
    def __init__(self, name, country, date_of_birth):
        self.name = name
        self.country = country
        # converting string typ to datetime type
        self.date_of_birth = datetime.strptime(date_of_birth, "%Y-%m-%d").date()

    def age_of_person(self):
    # Get today's time
        today = date.today()
    # calculate age of person
        age = today.year - self.date_of_birth.year
        if (today.month, today.day) < (self.date_of_birth.month, self.date_of_birth.day):
            age -= 1
        return age
    
Nodir = Person1('Nodir', 'Uzb', '1993-08-29')
print(f"{Nodir.name} age: {Nodir.age_of_person()}")

# Task 3
# Write a Python program to create a Calculator class. Include methods for basic arithmetic operations.

class Calculator:
    def __init__(self, x:int, y:int):
        self.x = x
        self.y = y
    def add_nums(self):
        return self.x + self.y
    def minus_nums(self):
        return self.x - self.y
    def multiply_nums(self):
        return self.x * self.y
    def devide_nums(self): 
        return self.x / self.y
re = Calculator(10, 2)
print(re.add_nums(), re.minus_nums(), re.multiply_nums(), re.devide_nums())

# Task 4
# Write a Python program to create a class that represents a shape. Include methods to calculate its area and perimeter.
#  Implement subclasses for different shapes like Circle, Triangle, and Square.

import math

class Shapes:
    def __init__(self, a_side:int):
        self.a_side = a_side
        # self.b_side = b_side

    def calc_square_primetr(self, b_side: int):
        return (self.a_side + b_side) * 2
    
    def calc_square_area(self, b_side):
        return self.a_side * b_side
    
    def calc_triangle_primetr(self, c_side: int):
        return self.a_side + self.b_side + c_side
    
    def calc_triangle_area(self, c_side: int):
        s = (self.a_side + self.b_side + c_side) / 2
        area = float((s*((s - self.a_side )*(s - self.b_side)*(s- c_side))) ** 0.5)
        return area
    
    def calc_circle_primetr(self):
        return round(2 * math.pi * self.a_side, 2)
    
    def calc_circle_area(self): 
        return round(math.pi * self.a_side **2, 2)

p_of_square = Shapes(3)
print(p_of_square.calc_circle_area())

# Task 6
# Write a Python program to create a class representing a stack data structure.
#  Include methods for pushing and popping elements
class Stack:
    def __init__(self):
        self.stack = []

    # using pushing methods
    def insert_data(self, item):
        self.stack.append(item)
        print(f'{item} pushed stack')

    def pop_data(self):
        if not self.is_empty():
            poped_data = self.stack.pop()
            print(f'{poped_data} is poped from stack')
            return poped_data
        else:
            print('Stack is empty')
            return None
        
    # Peek the top element of the stack without removing it
    def peek_element(self):
        if not self.is_empty():
            return self.stack[-1]
        else:
            print('Stack is empty')

    # check if stack is empty
    def is_empty(self):
        return len(self.stack) == 0
       
    
    # check size stack 
    def size_stack(self):
        return len(self.stack)

# Usage of stack methods
if __name__ == "__main__":
    stack = Stack()

    stack.insert_data(10)
    stack.insert_data(20)
    stack.insert_data(30)

    print(f"Top element is: {stack.peek_element()}")
    print(f"Stack size: {stack.size_stack()}")

    stack.pop_data()
    print(f"Stack size after pop: {stack.size_stack()}")

    stack.pop_data()
    stack.pop_data()
    stack.pop_data()  # This will show "Stack is empty"

class ShoppingCart:
    def __init__(self):
        self.cart ={}
    
    # Add item into cart
    def add_item(self, item_name, price, quantity):
        if item_name in self.cart:
            self.cart[item_name]['quantity'] += quantity
        else:
            self.cart[item_name] = {'price': price, 'quantity': quantity}
            print(f'Added {quantity}: {item_name} into cart')

    # Remove item from cart
    def remove_item(self, item_name, quantity = 1):
        if item_name in self.cart:
            if self.cart[item_name]['quantity'] <= quantity:
                del self.cart[item_name]
            else:
                self.cart[item_name]['quantity'] -=quantity
            print(f"Removed {quantity} x {item_name} from the cart.")
        else:
            print(f"{item_name} not found in the cart.")

    
            
# Calculate items cart
    def calculate_cart(self):
        total = sum(item['price'] * item['quantity'] for item in self.cart.values())
        return total

# Show cart info
    def display_cart(self):
        if not self.cart:
            print("Your cart is empty.")
        else:
            for item_name, item_info in self.cart.items():
                print(f'{item_name}: {item_info['quantity']} x ${item_info['price']} =  ${item_info['quantity'] * item_info['price']}')
                print(f'Total: ${self.calculate_total()}')
if __name__ == "__main__":
    cart = ShoppingCart()
    
    cart.add_item("Apple", 1.5, 3)
    cart.add_item("Banana", 0.8, 5)
    cart.add_item("Laptop", 999.99, 2)
    cart.remove_item("Laptop")
    cart.calculate_cart()

    
    print(f"Total price: ${cart.calculate_cart()}")
    
