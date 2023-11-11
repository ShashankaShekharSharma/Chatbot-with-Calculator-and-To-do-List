'''
# Chatbot Implementation

This code represents a sophisticated implementation of a chatbot that combines pattern matching techniques akin to ELIZA with modern features, such as sentiment analysis.
It engages users in text-based conversations while providing emotional insights.
It harnesses the TextBlob library to gauge sentiment in user inputs, fostering self-reflection and sharing of feelings.
The code is designed for future enhancement through data analysis, particularly the content stored in CSV files (feedback_data and conversation_data).
This accumulation of user interactions is essential for refining the chatbot's responses and making it more personalized.
Furthermore, the code includes mechanisms to keep records, timestamps, and even invites user feedback, ensuring that it evolves to cater to the users' needs.
The professional and responsive nature of this code signifies a powerful tool for simulating human-like interactions with users, paving the way for potential advancements in the field of conversational AI. The code encompasses elements such as date and time retrieval, user data logging, sentiment analysis, and user feedback integration, offering a comprehensive conversational experience.

## Key Features
- Pattern-based responses to user input
- Sentiment analysis of user's emotional state
- Date and time retrieval
- User feedback collection
- Conversation history recording

### Usage:
- Input "bye" to exit the conversation.
- Input "date and time" to get the current date and time.
- The program saves user prompts for feedback and analysis.

Developed By<br>
Shashanka Shekhar Sharma<br>
12.10.2023
'''
#Importing all Necessary Libraries
import re
import random
from textblob import TextBlob
import datetime
import time
import csv
import os
import math
import numpy as np
import matplotlib.pyplot as plt
import calendar

#Field Names
fieldnames = ['Type', 'Text']
tasks = []
# Creating a list that will store the user's history
conversation_history = []
# This code is implemented to record the time spent by the code
start_time = time.time()
# CSV Files are created to store the feedback and conversations given by the user
csv_filename = 'feedback_data.csv'
conversation_csv_filename = 'conversation_data.csv'
history_file = "calculator_history.csv"
FILE_NAME = "tasks.csv"
def print_calendar(year):
    for month in range(1, 13):
        # Display the month and year
        print(calendar.month_name[month], year)
        print("-----------------------------")
        
        # Display the calendar for the month
        cal = calendar.monthcalendar(year, month)
        print("Mo\tTu\tWe\tTh\tFr\tSa\tSu")
        for week in cal:
            for day in week:
                if day == 0:
                    print("\t", end="")
                else:
                    print(f"{day:2}", end="\t")
            print()

        print()
def calendardate():
    if __name__ == "__main__":
        try:
            year = int(input("Enter the year for the calendar: "))
            print_calendar(year)
        except ValueError:
            print("Invalid input. Please enter a valid year.")
#Function to Save Calculations of the CSV File
def save_to_csv(operation, result):
    with open(history_file, mode="a", newline="") as file:
        writer = csv.writer(file)
        writer.writerow([operation, result])
#Loading the csv file for Calculations
def load_from_csv():
    if os.path.exists(history_file):
        with open(history_file, mode="r") as file:
            reader = csv.reader(file)
            for row in reader:
                print(row)
    else:
        print("No history found.")
# Function to get current date and time
def get_date_and_time():
    now = datetime.datetime.now()
    return now.strftime("Current date and time: %Y-%m-%d %H:%M:%S")
# Function to analyze sentiment
def analyze_sentiment(text):
    analysis = TextBlob(text)
    sentiment_score = analysis.sentiment.polarity
    if sentiment_score > 0:
        return "Sentiment Analysis: You seem to be feeling positive."
    elif sentiment_score <= 0:
        return "Sentiment Analysis: Let's talk more. You will feel better."
def create_csv_file():
    if not os.path.exists(FILE_NAME):
        with open(FILE_NAME, 'w', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(['Task', 'Deadline'])
def save_tasks_to_csv():
    with open(FILE_NAME, mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(['Task', 'Deadline'])
        for task in tasks:
            if 'deadline' in task:
                writer.writerow([task['name'], task['deadline']])
            else:
                writer.writerow([task, ""])
def load_tasks_from_csv():
    create_csv_file()
    tasks.clear()  # Clear the existing tasks before loading from CSV
    with open(FILE_NAME, mode='r') as file:
        reader = csv.reader(file)
        next(reader)  # Skip header
        for row in reader:
            if row[1] != "":
                tasks.append({'name': row[0], 'deadline': row[1]})
            else:
                tasks.append({'name': row[0]})
def show_tasks():
    if not tasks:
        print("No tasks in the to-do list.")
    else:
        print("Tasks:")
        tasks_with_deadline = [task for task in tasks if 'deadline' in task]
        tasks_without_deadline = [task for task in tasks if 'deadline' not in task]

        if tasks_with_deadline:
            print("\nTasks with Deadline:")
            for i, task in enumerate(sorted(tasks_with_deadline, key=lambda x: x['deadline']), start=1):
                print(f"{i}. {task['name']} - Deadline: {task['deadline']}")

        if tasks_without_deadline:
            print("\nTasks without Deadline:")
            for i, task in enumerate(tasks_without_deadline, start=len(tasks_with_deadline) + 1):
                print(f"{i}. {task['name']}")
show_tasks()
def add_task(task):
    has_deadline = input("Does the task have a deadline? (yes/no): ").lower()
    if has_deadline == 'yes':
        deadline = input("Enter the deadline for the task: ")
        tasks.append({'name': task, 'deadline': deadline})
    else:
        tasks.append({'name': task})
    print(f"Task '{task}' added.")
def delete_task(task_index):
    if 1 <= task_index <= len(tasks):
        deleted_task = tasks.pop(task_index - 1)['name']
        print(f"Task '{deleted_task}' deleted.")
    else:
        print("Invalid task index.")
def update_task(task_index):
    if 1 <= task_index <= len(tasks):
        print("1. Edit Task\n2. Edit Deadline")
        sub_choice = input("Enter your sub-choice: ")
        if sub_choice == '1':
            updated_task = input("Enter the updated task: ")
            tasks[task_index - 1]['name'] = updated_task
            print(f"Task {task_index} updated to '{updated_task}'.")
        elif sub_choice == '2':
            updated_deadline = input("Enter the updated deadline: ")
            tasks[task_index - 1]['deadline'] = updated_deadline
            print(f"Task {task_index} deadline updated to '{updated_deadline}'.")
        else:
            print("Invalid sub-choice.")
        save_tasks_to_csv()
    else:
        print("Invalid task index.")
load_tasks_from_csv()
def todo():
    while True:
        print("\nMain Menu\n1. Show Tasks\n2. Add Task\n3. Delete Task\n4. Update Task\n5. Quit")
        choice = input("Enter your choice: ")

        if choice == '1':
            show_tasks()
        elif choice == '2':
            task = input("Enter the task to add: ")
            add_task(task)
            save_tasks_to_csv()
        elif choice == '3':
            show_tasks()
            task_index = int(input("Enter the index of the task to delete: "))
            delete_task(task_index)
            save_tasks_to_csv()
        elif choice == '4':
            show_tasks()
            task_index = int(input("Enter the index of the task to update: "))
            update_task(task_index)
        elif choice == "5":
                print("Exiting the to-do. Gooodbye!")
                break
        else:
            print("Invalid choice. Please try again.")
# Function to match user's input to a pre-defined response
def match_response(input_text):
    for pattern, response_list in response.items():
        matches = re.match(pattern, input_text.lower())
        if matches:
            choosen_response = random.choice(response_list)
            return choosen_response.format(*matches.groups())
    return "I am sorry. I am unable to understand what you are saying."
  #Calculator
#Addition
result_flag = False
def add_numbers(result):
    if result_flag:
        operation = str(result) + "+"
        temp = []
        print(f"Adding numbers to : {result}")
        count = int(input("How many numbers do you want to add? "))
        for i in range(count):
            num = float(input("Enter the number: "))
            result += num
            temp.append(num)
        for i in range(len(temp)):
            if i != len(temp) - 1:
                operation += str(temp[i])
                operation += "+"
            else:
                operation += str(temp[i])
                operation += "="
        print(f"Sum: {result}")
        save_to_csv(operation, result)
        return result
    else:
        num1 = float(input("Enter number 1 : "))
        num2 = float(input("Enter number 2 : "))
        result = num1 + num2
        operation = str(num1) + "+" + str(num2)
        save_to_csv(operation, result)
        print(f"Sum : {result}")
        return result
#Subtraction
def subtract_numbers(result):
    if result_flag:
        operation = str(result) + "-"
        temp = []
        print(f"Adding numbers to : {result}")
        count = int(input("How many numbers do you want to subtract? "))
        for i in range(count):
            num = float(input("Enter the number: "))
            result -= num
            temp.append(num)
        for i in range(len(temp)):
            if i != len(temp) - 1:
                operation += str(temp[i])
                operation += "-"
            else:
                operation += str(temp[i])
                operation += "="
        print(f"Sum: {result}")
        save_to_csv(operation, result)
        return result
    else:
        operation = " "
        n1 = float(input("Enter number to subtract from : "))
        n2 = float(input("Enter number to subtract "))
        result = n1 - n2
        operation = str(n1) + "-" + str(n2)
        print(f"Difference : {result}")
        save_to_csv(operation, result)
        return result
#Multiplication
def multiply_numbers(result):
    if result_flag:
        operation = str(result) + "*"
        temp = []
        print(f"Adding numbers to : {result}")
        count = int(input("How many numbers do you want to multiply? "))
        for i in range(count):
            num = float(input("Enter the number: "))
            result *= num
            temp.append(num)
        for i in range(len(temp)):
            if i != len(temp) - 1:
                operation += str(temp[i])
                operation += "*"
            else:
                operation += str(temp[i])
                operation += "="
        print(f"Sum: {result}")
        save_to_csv(operation, result)
        return result
    else:
        n1 = float(input("Enter number 1 : "))
        n2 = float(input("Enter number 2 : "))
        result = n1 * n2
        operation = str(n1) + "x" + str(n2)
        print(f"Product : {result}")
        save_to_csv(operation, result)
        return result
#Division
def divide_numbers(result):
    if result_flag:
        print(f"Dividing from(dividend) : {result}")
        num = float(input("Enter the number to divide: "))
        result1 = result
        if num == 0:
            print("Error: Division by zero")
            return result
        result /= num
        operation = str(result) + "/" + str(num)
        print(f"Quotient: {result}")
        save_to_csv(operation, result)
        return result
    else:
        n1 = float(input("Enter dividend : "))
        n2 = float(input("Enter divisor : "))
        result = n1 / n2
        operation = str(n1) + "/" + str(n2)
        print(f"Quotient : {result}")
        save_to_csv(operation, result)
        return result
#Quadratic Equation
def solve_quadratic_equation(result):
    print("Enter the coefficients of the quadratic equation (ax^2 + bx + c = 0):")
    a = float(input("Enter coefficient a: "))
    b = float(input("Enter coefficient b: "))
    c = float(input("Enter coefficient c: "))
    discriminant = b * b - 4 * a * c
    operation = 'Solving the equation: '+str(a)+'x^2'+str(b)+'x+'+str(c)+'=0'
    if discriminant > 0:
        root1 = (-b + math.sqrt(discriminant)) / (2 * a)
        root2 = (-b - math.sqrt(discriminant)) / (2 * a)
        print(f"The roots are real and distinct: {root1} and {root2}")
        ans=[root1,root2]
    elif discriminant == 0:
        root1 = root2 = -b / (2 * a)
        print(f"The roots are real and equal: {root1} and {root2}")
        ans=[root1,root2]
    else:
        realPart = -b / (2 * a)
        imaginaryPart = math.sqrt(-discriminant) / (2 * a)
        print(f"The roots are complex and different: {realPart}+{imaginaryPart}i and {realPart}-{imaginaryPart}i")
        ans = [str(realPart)+'i'+str(imaginaryPart)+'j',str(realPart)+'i-'+str(imaginaryPart)+'j']
    save_to_csv(operation, ans)
#Cubic Function
def solve_cubic_equation(result):
    print("Enter the coefficients of the cubic equation (ax^3 + bx^2 + cx + d = 0):")
    a = float(input("Enter coefficient a: "))
    b = float(input("Enter coefficient b: "))
    c = float(input("Enter coefficient c: "))
    d = float(input("Enter coefficient d: "))
    operation = 'Solving the equation: ' + str(a) + 'x^3' + str(b) + 'x^2+' + str(c)+'x+'+str(d) + '=0'
    p = (3 * a * c - b ** 2) / (3 * a ** 2)
    q = (2 * b ** 3 - 9 * a * b * c + 27 * a ** 2 * d) / (27 * a ** 3)

    discriminant = q ** 2 / 4 + p ** 3 / 27
    if discriminant > 0:
        S = (q / 2 + math.sqrt(discriminant)) ** (1 / 3)
        T = (q / 2 - math.sqrt(discriminant)) ** (1 / 3)
        root1 = -b / (3 * a) - (S + T)
        print(f"The real root is: {root1}")
        imaginary = (S - T) * math.sqrt(3) / 2
        root2 = -b / (3 * a) + (S + T) / 2 + imaginary
        root3 = -b / (3 * a) + (S + T) / 2 - imaginary
        print(f"The complex roots are: {root2} and {root3}")
        ans=[str(root1),str(root2)+'j'+str(root3)+'j']
        save_to_csv(operation,ans)
    elif discriminant == 0:
        if q < 0:
            A = (abs(q) / 2) ** (1 / 3)
            root1 = -b / (3 * a) - 2 * A
            root2 = -b / (3 * a) + A
            print(f"The real root is: {root1} and the complex root is: {root2} + {root2}i")
            ans=[str(root1),str(root2)+'i'+str(root2)+'j']
            save_to_csv(operation,ans)
        else:
            A = (-q / 2) ** (1 / 3)
            root1 = -b / (3 * a) - 2 * A
            root2 = -b / (3 * a) + A
            print(f"The real root is: {root1} and the complex root is: {root2} - {root2}i")
            ans=[str(root1),str(root2)+'i-'+str(root2)+'j']
            save_to_csv(operation,ans)
    else:
        x = math.sqrt((q ** 2 / 4) - discriminant)
        θ = math.acos(-q / (2 * math.sqrt(discriminant)))
        root1 = 2 * math.sqrt(-p / 3) * math.cos(θ / 3) - b / (3 * a)
        root2 = 2 * math.sqrt(-p / 3) * math.cos((θ + 2 * math.pi) / 3) - b / (3 * a)
        root3 = 2 * math.sqrt(-p / 3) * math.cos((θ + 4 * math.pi) / 3) - b / (3 * a)
        print(f"The roots are: {root1}, {root2}, and {root3}")
        ans=[root1,root2,root3]
        save_to_csv(operation,ans)
#Polynomial Graph
def polynomial_graph(result):
    degree = int(input("Enter the degree of the polynomial: "))
    coefficients = []
    for i in range(degree + 1):
        coefficient = float(input(f"Enter the coefficient for x^{i}: "))
        coefficients.append(coefficient)
    y = 0
    for i in range(len(coefficients)):
        y += coefficients[i] * x**i
    return y
    x = np.linspace(-10, 10, 400)
    y = polynomial(x, coefficients)
    plt.figure(figsize=(8, 6))
    plt.plot(x, y, label='Polynomial Equation', color='b')
    plt.title('Graph of the Polynomial Equation')
    plt.xlabel('X-axis')
    plt.ylabel('Y-axis')
    plt.legend()
    plt.grid()
    plt.show()
#Factorial of number
def factorial_of_number(result):
    operation = ""
    temp = []
    num = int(input("Enter number to factorial : "))
    fact = 1
    for i in range(1, num + 1):
        temp.append(i)
        fact *= i
    print(f"Factorial: {fact}")
    for i in range(len(temp)):
        if i < (len(temp)-1):
            operation += str(temp[i])
            operation += "x"
        else:
            operation += str(temp[i])
    result = fact
    save_to_csv(operation, result)
    return result
#Logarithm
def log(result):
    if result_flag:
        print("taking log of ",result)
        num = input("Enter the base: (type 'e' for natural log)")
        num = int(num)
        if num == 'e':
            result = math.log(result)
            print(result)
        elif num > 0:
            result = math.log(result,num)
            print(result)
        else:
            result("invalid")
        operation = 'log of'+str(result)+'base'+str(num)
        save_to_csv(operation,result)
    else:
        a = int(input("enter the number "))
        num = int(input("Enter the base "))
        if a>0 and num>0:
            result=math.log(a,num)
            operation='log of '+str(a)+ 'base'+ str(num)
            save_to_csv(operation,result)
            print(result)
        else:
            print("invalid")
#Polynomial Function Plot
def plot_polynomial(degree, coefficients):
    # Function to evaluate the polynomial equation
    def polynomial(x, coefficients):
        y = 0
        for i in range(len(coefficients)):
            y += coefficients[i] * x**i
        return y

    # Generate x values
    x = np.linspace(-10, 10, 400)

    # Compute corresponding y values
    y = polynomial(x, coefficients)

    # Plot the graph
    plt.figure(figsize=(8, 6))
    plt.plot(x, y, label='Polynomial Equation', color='b')
    plt.title('Graph of the Polynomial Equation')
    plt.xlabel('X-axis')
    plt.ylabel('Y-axis')
    plt.legend()
    plt.grid()
    plt.show()
#Trigonometric Function
def trigonometric_submenu(result):
    while True:
        print("\nTrigonometric functions:")
        print("1. Sin")
        print("2. Cos")
        print("3. Tan")
        print("4. Sec")
        print("5. Cosec")
        print("6. Cot")
        print("7. Sin inverse")
        print("8. Cos inverse")
        print("9. Tan inverse")
        print("10. Cosec inverse")
        print("11. Sec inverse")
        print("12. Cot inverse")
        print("13. Back to Main Menu")
        choice = input("Enter your choice: ")

        if choice == "13":
            break

        if not choice.isdigit() or int(choice) < 1 or int(choice) > 12:
            print("Invalid choice. Please choose again.")
            continue

        if result_flag:
            radian_val = math.radians(result)
            if choice == "1":
                result=round(math.sin(radian_val),3)
                operations="sine :"+str(radian_val)
            elif choice == "2":
                result=round(math.cos(radian_val),3)
                operations="cosine : "+str(radian_val)
            elif choice == "3":
                result=round(math.tan(radian_val),3)
                operations="tangent : "+str(radian_val)
            elif choice == "4":
                result=round(1/math.cos(radian_val),3)
                operations="secant : "+str(radian_val)
            elif choice == "5":
                result=round(1/math.sin(radian_val),3)
                operations="cosecant : "+str(radian_val)
            elif choice == "6":
                result=round(1/math.tan(radian_val),3)
                operations="cotangent : "+str(radian_val)
            elif choice == "7":
                result=round(math.asin(result),3)
                operations="sine inverse : "+str(radian_val)
            elif choice == "8":
                result=round(math.acos(result),3)
                operations="cosine inverse : "+str(radian_val)
            elif choice == "9":
                result=round(math.atan(result),3)
                operations="tangent inverse : "+str(radian_val)
            elif choice == "10":
                result=round(math.asin(1/result),3)
                operations="cosecant inverse : "+str(radian_val)
            elif choice == "11":
                result=round(math.acos(1/result),3)
                operations="secant inverse : "+str(radian_val)
            elif choice == "12":
                result=round(math.atan(1/result),3)
                operations="cotangent inverse : "+str(radian_val)
            save_to_csv(operations,result)

        else:
            deg = float(input("Enter values in degrees : "))
            radian_val = math.radians(deg)
            if choice == "1":
                result=round(math.sin(radian_val),3)
                operations="sine :"+str(radian_val)
            elif choice == "2":
                result=round(math.cos(radian_val),3)
                operations="cosine : "+str(radian_val)
            elif choice == "3":
                result=round(math.tan(radian_val),3)
                operations="tangent : "+str(radian_val)
            elif choice == "4":
                result=round(1/math.cos(radian_val),3)
                operations="secant : "+str(radian_val)
            elif choice == "5":
                result=round(1/math.sin(radian_val),3)
                operations="cosecant : "+str(radian_val)
            elif choice == "6":
                result=round(1/math.tan(radian_val),3)
                operations="cotangent : "+str(radian_val)
            elif choice == "7":
                result=round(math.asin(result),3)
                operations="sine inverse : "+str(radian_val)
            elif choice == "8":
                result=round(math.acos(result),3)
                operations="cosine inverse : "+str(radian_val)
            elif choice == "9":
                result=round(math.atan(result),3)
                operations="tangent inverse : "+str(radian_val)
            elif choice == "10":
                result=round(math.asin(1/result),3)
                operations="cosecant inverse : "+str(radian_val)
            elif choice == "11":
                result=round(math.acos(1/result),3)
                operations="secant inverse : "+str(radian_val)
            elif choice == "12":
                result=round(math.atan(1/result),3)
                operations="cotangent inverse : "+str(radian_val)
            save_to_csv(operations,result)
        return result
#Function of the calculator which includes the logic
def calculator():
    print("Hi! I can perform simple calculations. I can add, multiply, and subtract.")
    result_flag = False
    result = 0
    while True:
        while True:
            print("\nChoose the operation:")
            print("Type history to see previous calculations")
            print("1. Addition")
            print("2. Subtraction")
            print("3. Multiplication")
            print("4. Division")
            print("5. Trigonometric submenu")
            print("6. Factorial")
            print("7. Solve Quadratic Equation")
            print("8. Solve Cubic Equations")
            print("9. Logarithms")
            print("10. Graph of Polynomial Equation")
            print("11. Exit")

            choice = input("Enter your choice: ")

            if choice == "11":
                print("Exiting the calculator. Goodbye!")
                break

            if not choice.isdigit() or int(choice) < 1 or int(choice) > 11:
                print("Invalid choice. Please choose again.")
                continue

            if choice == "1":
                result = add_numbers(result)
            elif choice == "2":
                result = subtract_numbers(result)
            elif choice == "3":
                result = multiply_numbers(result)
            elif choice == "4":
                result = divide_numbers(result)
            elif choice == "5":
                result = trigonometric_submenu(result)
            elif choice == "6":
                result = factorial_of_number(result)
            elif choice == "7":
                result = solve_quadratic_equation(result)
            elif choice == "8":
                result = solve_cubic_equation(result)
            elif choice == "9":
                result = log(result)
            elif choice == "10":
                degree = int(input("Enter the degree of the polynomial: "))
                coefficients = []
                for i in range(1,degree + 1):
                    coefficient = float(input(f"Enter the coefficient for x^{i}: "))
                    coefficients.append(coefficient)
                const=int(input("Enter the value of constant term "))
                coefficients.append(const)
                plot_polynomial(degree, coefficients)
            elif choice == "history":
                load_from_csv()
                continue

            choice = input(
                "Do you want to perform another operation on this result? (yes/no): "
            )
            if choice.lower() == "history":
                print("Displaying history:")
                load_from_csv()
                continue
            elif choice.lower() != "yes":
                result = 0

                break
            else:
                result_flag = True
                continue
        choice = input("Do you want to start a new operation? (yes/no): ")
        if choice.lower() != "yes":
            print("Exiting the calculator. Goodbye!")
            break
# Creating a list of predefined responses similar to that of Eliza using dictionary
response = {
    "hello": ["Hello how can I help you"],
    "hi": ["Hey there! How can I help you"],
    "how do you do?": ["I am fine. What about you?"],
    "i am (sad|feeling sad|depressed|anxious)": [
        "Do something you enjoy. When you're feeling sad, it can be helpful to do something that you enjoy and that makes you feel good. This could be anything from reading a book to taking a walk to spending time with loved ones. If you want to talk I am always here"],
    "(i'm having problems with my partner|how can i improve my relationship with my family)": [
        "It's normal to have problems in relationships from time to time. All relationships require work and effort to maintain. Try talking to them about the problem to reduce communication gaps",
        "Would you like to share more about it?"],
    "what can you do(.*)": [
        "I can do the follwing: 1. Be your Psychotherapist 2. Get you date and time 3. Give your sentiment analysis"],
    "how are you": ["I am fine. What about you?"],
    "i feel (.*)": ["Why do you feel {}?", "How long have you been feeling {}"],
    "i am (.*)": ["Why do you say you are {}?", "How long have you been {}"],
    "i (.*) you": ["Why do you {} me?", "What makes you think you {} me"],
    "i (.*) myself": ["Why do you {} yourself?", "What makes you think you {} yourself?"],
    "(.*) sorry (.*)": ["There no need to apologize.", "What are you apologizing for?"],
    "(.*) friend (.*)": ["Tell me more about your friend", "How do your friend make you feel?"],
    "yes": ["You seem quite sure. Can you elaborate?", "Ok,but can you elaborate."],
    "no": ["Why not?", "Ok, Can you elaborate a bit?"],
    "i am happy": ["I am glad that you are. What makes you feel so?"],
    "i want to talk (.*)": ["Sure just go on. I am listening."],
    "i am sad": ["I am sorry to hear that. What makes you feel so."],
    "i like to (.*)": ["Well that's great. What makes you like it."],
    "i like (.*)": ["Well I see, why do you like (.*)"],
    "(.*)i failed (.*)": ["I can imagine how disappointed you must be feeling right now.Do you want to talk about it"],
    "i am not sure about (.*)": ["It is okay to not have answers about some things",
                                 "Okay, what's causing the uncertainity."],
    "what should I do about (.*)": [
        "It's important to conisder your own feelings and priority before taking a decision. What's bothering you about (.*)"],
    "i love (.*)": ["I get that. Love is a powerful emotion. Tell me more about (.*)"],
    "i (don't know|can't decide) what to do with my life": [
        "Many people feel that way at times. Even I did! All you need to do is divert your focus to your hobbies and passion. What are yours?",
        "It's okay to feel like that. Many people do. What are your interests and passion?"],
    "i want to (visit|go) (.*)": ["I am glad that you have such plans", "I wish I could go too"],
    "my (boyfriend|girlfriend|father|mother|brothers|brother|sister|sister)": [
        "Oh I see. Tell more about how the relationship was like"],
    "i (dream to|want to|aspire to|will) (.*)": ["It's good to have dreams", "What motivates you to be that?"],
    "i (love|hate) my (job|school)": ["Many people (love|hate) their (school|jobs). What's your reason?"],
    "i feel stressed": ["Dealing with stress is a pretty diffcult task. Try taking some break",
                        "Why don't you take a break?"],
    "what (do you think|are your thoughts) about (.*)": ["We are here to talk about you. Not me.",
                                                         "I would like to focus on you rather than my opinions. Tell me how was your day?"],
    "i am (frustrated|annoyed) with (.*)": ["I am sorry for how you feel. What makes you feel so?"],
    "i lost (.*)": ["In am sorry for your loss. How are you coping up with your loss?"],
    "i am struggling with (.*)": ["I can understand that. It's a part of life.",
                                  "I am sorry to hear that. I hope things will be alright soon"],
    "what is your name": ["My name is ELiza and I am a Rogerian Psychotherapist"],
    " (.*) ": ["Please tell me more",
               "Can you share more about your feelings? It will help you to loosen up your mind.",
               "Can you elaborate on that?"],
    "": ["Why do you think that?", "Please tell me more.",
         "Let's change the focus a bit...tell me more about your family", "Can you elaborate on that?"],
}
# Printing the Historic ELIZA Deisgn
print('''Welcome to
EEEEEEE     LL        IIIIIIII  ZZZZZ     AAAA 
EEE         LL           II        ZZ    AA  AA
EEEEEEE     LL           II       ZZ    AAAAAAAA  
EEE         LL           II      ZZ     AA    AA
EEEEEEE     LLLLLLLLL IIIIIIII  ZZZZZZ  AA    AA''')
#Introduction
print("Welcome. I am Eliza. A Rogerian psychotherapist")
print("Your prompts will be saved in order to make improvements in the code")
print("Type Calculator to open Calculator")
print("Type date and time to get date and time")
print("Type bye to exit")
#Logical Part of Eliza
#Includes conversation counter, history note maker, sentiment analysis, feedback receiver and date and time
#Write programmer's data to get history of chats
conversation_counter = 0
if not os.path.exists(csv_filename):
    with open(csv_filename, 'w', newline='') as csvfile:
        fieldnames = ['Type', 'Text']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()
if not os.path.exists(conversation_csv_filename):
    with open(conversation_csv_filename, 'w', newline='') as csvfile:
        fieldnames = ['Type', 'Text']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()
while True:
    user_input = input("You: ")
    conversation_history.append({"user": user_input})
    with open(conversation_csv_filename, 'a', newline='') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writerow({'Type': 'User', 'Text': user_input})

    # Increment the conversation counter
    conversation_counter += 1
    if conversation_counter % 5 == 0:
        # Analyze sentiment after every 5 conversations
        sentiment_response = analyze_sentiment(user_input)
        print(f"Eliza: {sentiment_response}")
    if user_input.lower() == "bye":
        feedback = input("Would you like to provide feedback (yes/no)? ")
        if feedback.lower() == "yes":
            user_feedback = input("Eliza: Please provide your feedback: ")
            feedback = []
            feedback.append({"user": user_feedback})
            for_feedback = ["Thank you for your valuable feedback", "Thank you for your time", "Thank you",
                            "Thanks for being here. We will meet again"]
            print(random.choice(for_feedback))
            end_time = time.time()
            time_spent = end_time - start_time
            print(f"Time spent with Eliza: {time_spent:.2f} seconds")
            print(f"Number of lines of conversations: {conversation_counter}")

            # Append feedback to the CSV file
            with open(csv_filename, 'a', newline='') as csvfile:
                writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
                writer.writerow({'Type': 'Feedback', 'Text': user_feedback})
        else:
            print("Goodbye")
            end_time = time.time()
            time_spent = end_time - start_time
            print(f"Time spent with Eliza: {time_spent:.2f} seconds")
            print(f"Number of lines of conversations: {conversation_counter}")
        break
    elif "programmer's data" in user_input.lower():
        print("Eliza: Here are your past conversations:")
        if os.path.exists(conversation_csv_filename):
            with open(conversation_csv_filename, 'r', newline='') as csvfile:
                reader = csv.DictReader(csvfile)
                for row in reader:
                    print(f"Type: {row['Type']}, Text: {row['Text']}")
        if os.path.exists(csv_filename):
            with open(csv_filename, 'r', newline='') as csvfile:
                reader = csv.DictReader(csvfile)
                print("Eliza: Here are your feedbacks:")
                for row in reader:
                    print(f"Type: {row['Type']}, Text: {row['Text']}")
    elif "date and time" in user_input.lower():
        date_time = get_date_and_time()
        print(f"Eliza: {date_time}")
    elif "calculator" in user_input.lower():
        calculator()
    elif "todo" in user_input.lower():
        print("Welcome to To-do List")
        todo()
    elif "calendar" in user_input.lower():
        calendardate()
    else:
        print("Eliza: " + match_response(user_input))
