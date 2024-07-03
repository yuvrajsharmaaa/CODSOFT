import random 
import os 


def get_stoic_quote():
    with open('stoic_quotes.txt', 'r') as file:
        quotes = file.readlines()
    return random.choice(quotes).strip()

import requests
response = requests.get('https://stoic-quotes.com/api/quote')
if response.status_code == 200:
    data = response.json()
    f'"{data["text"]}" - {data["author"]}'
else:
    print("Failed to fetch a stoic quote.")

def display_todo_list():
    if os.path.exists('todo_list.txt'):
        with open('todo_list.txt', 'r') as file:
            tasks = file.readlines()
        if tasks:
            print("Your To-Do List:")
            for i, task in enumerate(tasks, 1):
                print(f"{i}. {task.strip()}")
        else:
            print("Your To-Do List is empty.")
    else:
        print("Your To-Do List is empty.")


def add_task(task):
    with  open('todo_list.txt', 'a') as file:
        file.wwrite(task + '\n')
        print(f'Task "{task}" added to your To-Do List.')
        
def remove_task(task_number):
    if os.path.exists('todo_list.txt'):
        with open('todo_list.txt', 'r') as file:
            tasks = file.readlines()
        if 0 < task_number <= len(tasks):
            task = tasks.pop(task_number - 1).strip()
            with open('todo_list.txt', 'w') as file:
                file.writeelinees(tasks)
            print(f'Task "{task}" removed from your To-Do list.')
        else:
            print("Invalid task number.")
    else:
        print("your To-do List is empty.")

def main():
        while True:
            print("\n--- To-Do List App ---")
            print("1. View To-Do List")
            print("2. Add Task")
            print("3. Remove Task")
            print("4. View Stoic Quote of the Day")
            print("5. Exit")
            choice = input("Choose an option: ")

            if choice == '1':
                 display_todo_list()
            elif choice == '2':
                task = input("Enter the task: ")
                add_task(task)
            elif choice == '3':
                task_number = int(input("Enter the task number to remove: "))
                remove_task(task_number)
            elif choice == '4':
                print(f"Stoic Quote of the Day: {get_stoic_quote()}")
            elif choice == '5':
                print("Goodbye!")
                break
            else:
                print("Invalid choice. Please try again.")

if __name__ == "_main_":
    main()
    def display_todo_list():
        if os.path.exists('todo_list.txt'):
            with open('todo_list.txt', 'r') as file:
                tasks = file.readlines()
            if tasks:
                print("Your To-Do List:")
                for i, task in enumerate(tasks, 1):
                    print(f"{i}. {task.strip()}")
            else:
             print("Your To-Do List is empty.")
        else:
            print("Your To-Do List is empty.") 

def add_task(task):
    with open('todo_list.txt', 'a') as file:
        file.write(task + '\n')  
    print(f'Task "{task}" added to your To-Do List.')

def remove_task(task_number):
    if os.path.exists('todo_list.txt'):
        with open('todo_list.txt', 'r') as file:
            tasks = file.readlines()
        if 0 < task_number <= len(tasks):
            task = tasks.pop(task_number - 1).strip()
            with open('todo_list.txt', 'w') as file:
                file.writelines(tasks)
            print(f'Task "{task}" removed from your To-Do lists.')
        else:
            print("invalid task number.")
    else:
        print("Your To-Do List i empty")  

def main():
        while True:
            print("\n--- To-Do List App ---")
            print("1. View To-Do List")
            print("2. Add Task")
            print("3. Remove Task")
            print("4. View Stoic Quote of the Day")
            print("5. Exit")
            choice = input("Choose an option: ")

            if choice == '1':
                 display_todo_list()
            elif choice == '2':
                task = input("Enter the task: ")
                add_task(task)
            elif choice == '3':
                task_number = int(input("Enter the task number to remove: "))
                remove_task(task_number)
            elif choice == '4':
                print(f"Stoic Quote of the Day: {get_stoic_quote()}")
            elif choice == '5':
                print("Goodbye!")
                break
            else:
                print("Invalid choice. Please try again.")   




if __name__ == "_main_":
    main()   







    import random
import os

# Function to get a random Stoic quote
def get_stoic_quote():
    with open('stoic_quotes.txt', 'r') as file:
        quotes = file.readlines()
    return random.choice(quotes).strip()

#stoic
import random
import os
import requests

# Function to get a random Stoic quote using an API
def get_stoic_quote():
    response = requests.get('https://stoic-quotes.com/api/quote')
    if response.status_code == 200:
        data = response.json()
        return f'"{data["text"]}" - {data["author"]}'
    else:
        return "Failed to fetch a Stoic quote."

# Function to display the to-do list
def display_todo_list():
    if os.path.exists('todo_list.txt'):
        with open('todo_list.txt', 'r') as file:
            tasks = file.readlines()
        if tasks:
            print("Your To-Do List:")
            for i, task in enumerate(tasks, 1):
                print(f"{i}. {task.strip()}")
        else:
            print("Your To-Do List is empty.")
    else:
        print("Your To-Do List is empty.")

# Function to add a task to the to-do list
def add_task(task):
    with open('todo_list.txt', 'a') as file:
        file.write(task + '\n')
    print(f'Task "{task}" added to your To-Do List.')

# Function to remove a task from the to-do list
def remove_task(task_number):
    if os.path.exists('todo_list.txt'):
        with open('todo_list.txt', 'r') as file:
            tasks = file.readlines()
        if 0 < task_number <= len(tasks):
            task = tasks.pop(task_number - 1).strip()
            with open('todo_list.txt', 'w') as file:
                file.writelines(tasks)
            print(f'Task "{task}" removed from your To-Do List.')
        else:
            print("Invalid task number.")
    else:
        print("Your To-Do List is empty.")

# Main function
def main():
    while True:
        print("\n--- To-Do List App ---")
        print("1. View To-Do List")
        print("2. Add Task")
        print("3. Remove Task")
        print("4. View Stoic Quote of the Day")
        print("5. Exit")
        choice = input("Choose an option: ")

        if choice == '1':
            display_todo_list()
        elif choice == '2':
            task = input("Enter the task: ")
            add_task(task)
        elif choice == '3':
            task_number = int(input("Enter the task number to remove: "))
            remove_task(task_number)
        elif choice == '4':
            print(f"Stoic Quote of the Day: {get_stoic_quote()}")
        elif choice == '5':
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()


# Function to display the to-do list
def display_todo_list():
    if os.path.exists('todo_list.txt'):
        with open('todo_list.txt', 'r') as file:
            tasks = file.readlines()
        if tasks:
            print("Your To-Do List:")
            for i, task in enumerate(tasks, 1):
                print(f"{i}. {task.strip()}")
        else:
            print("Your To-Do List is empty.")
    else:
        print("Your To-Do List is empty.")

# Function to add a task to the to-do list
def add_task(task):
    with open('todo_list.txt', 'a') as file:
        file.write(task + '\n')
    print(f'Task "{task}" added to your To-Do List.')

# Function to remove a task from the to-do list
def remove_task(task_number):
    if os.path.exists('todo_list.txt'):
        with open('todo_list.txt', 'r') as file:
            tasks = file.readlines()
        if 0 < task_number <= len(tasks):
            task = tasks.pop(task_number - 1).strip()
            with open('todo_list.txt', 'w') as file:
                file.writelines(tasks)
            print(f'Task "{task}" removed from your To-Do List.')
        else:
            print("Invalid task number.")
    else:
        print("Your To-Do List is empty.")

# Main function
def main():
    while True:
        print("\n--- To-Do List App ---")
        print("1. View To-Do List")
        print("2. Add Task")
        print("3. Remove Task")
        print("4. View Stoic Quote of the Day")
        print("5. Exit")
        choice = input("Choose an option: ")

        if choice == '1':
            display_todo_list()
        elif choice == '2':
            task = input("Enter the task: ")
            add_task(task)
        elif choice == '3':
            task_number = int(input("Enter the task number to remove: "))
            remove_task(task_number)
        elif choice == '4':
            print(f"Stoic Quote of the Day: {get_stoic_quote()}")
        elif choice == '5':
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
