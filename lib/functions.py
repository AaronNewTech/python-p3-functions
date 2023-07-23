#!/usr/bin/env python3

def greet_programmer():
    print("Hello, programmer!")
    pass

def greet(name):
    print("Hello, " + name + "!")
    pass

def greet_with_name(name):
    print(f"Hello, {name}!")
    pass

def greet_with_default(name="programmer"):
    print(f"Hello, {name}!")
    pass

def add(num1, num2):
    num1 = 45
    num2 = 55
    return num1 + num2
    pass

def halve(number):
    return number / 2
    pass
