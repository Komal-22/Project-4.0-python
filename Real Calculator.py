#!/usr/bin/env python
# coding: utf-8

# In[18]:


def add(a,b):
    addition = a + b
    print(f"The sum of {a} and {b} is {addition}") #formatted strings

def subtract(a,b):
    subtraction = b - a
    print(f"The result of subtracting {b} from {a} is {subtraction}")

def multiply(a,b):
    multiplication = a * b
    print(f"The multiplication of {a} and {b} is {multiplication}")

def division(a,b):
    divide = a / b
    print(f"The sum of {a} and {b} is {divide}")
    
def modulus(a,b):
    modulusValue = a % b
    print(f"The sum of {a} and {b} is {modulusValue}")

# accepting multiple inputs in a single
number1,operator,number2 = map(str, input("Enter your equation: ").split()) # 8 / 9
number1 = int(number1)
number2 = int(number2)

# shift+alt+down

if operator == "+":
    add(number1,number2)
    
elif operator == "-":
    subtract(number1,number2)
    
elif operator == "*":
    multiply(number1,number2)
    
elif operator == "/":
    division(number1,number2)
    
elif operator == "%":
    modulus(number1,number2)
    
else:
    print("Invalid Typo Error! Type something like - 8 / 4")
    


# In[ ]:





# In[ ]:




