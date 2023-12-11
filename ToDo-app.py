from random import *

RANDOM_TASKS = ['do homework', 'feed my dog', 'wash up', 'cook dinner', 'build house']
run = True
tasks = {}

def add_todo(tasks):
    if date in tasks: #if date in dictionary tasks - we will add new task for this date
        tasks[date].append(task)
    else:    #if tasks don't have date - we will add new date and new task
        tasks[date] = []
        tasks[date].append(task)
    return tasks

while run:
    command = input('Input command: ')
    if command == 'add':
        date = input('Input date, which you wanna add: ')
        task = input('Input task, which you wanna add: ')
        print(add_todo(tasks))
    elif command == 'random': #we will choose task from list 'RANDOM_TASKS'
        random_task = choice(RANDOM_TASKS)
        print(f'Today you will need to {random_task}')
    elif command == 'show':
        show_tasks = input('Input date for showing list of tasks: ')
        if show_tasks in tasks:
            print(tasks[show_tasks])
        else:
            print('This date does not exists!!!')
    else:
        print('Unknown command! Goodbye!')
        break