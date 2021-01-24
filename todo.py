import os
import argparse
from datetime import datetime

today_date = datetime.today().strftime('%Y-%m-%d')

def add(args):
    try:
        text = args.task[1]
        with open("todo.txt", 'a') as f:
            f.write(text)
            f.write("\n")
        print(f'Added todo : "{text}"')
    except:
        print("Error : no task given")


def show():
    with open("todo.txt", 'r') as f:
        works = f.readlines()
        works = [x for x in works if x != "\n"]
        if len(works) != 0:
            works = works[::-1]
            length = len(works)
            for count, i in enumerate(works):
                print(f"[{length - count}] {i}")
        else:
            print("No any todos")

def delete(args):
    try:
        index = args.task[1]
        num = index
        index = int(index)-1
        with open("todo.txt", "r") as f:
            lines = f.readlines()
            try:
                lines.pop(index)
                with open("todo.txt", "w") as new_f:
                    for line in lines:
                        new_f.write(line)
                print(f"Deleted todo #{num}")
            except:
                print(f"Error: todo #{num} does not exist. Nothing deleted.")
    except:
            print("Error : no index given")

def done(args):
    try:
        index = args.task[1]
        num = index
        index = int(index) - 1
        with open("todo.txt", "r") as f:
            lines = f.readlines()
            try:
                completed = lines.pop(index)
                with open("todo.txt", "w") as new_f:
                    for line in lines:
                        new_f.write(line)
                with open("done.txt", "a") as done_f:
                    done_f.write(f"x {today_date} {completed}")
                print(f"Marked todo #{num} as done.")
            except:
                print(f"Error: todo #{num} does not exist.")
    except:
        print("Error : no index given")

def report():
    with open("todo.txt", "r") as pend_f:
        lines = pend_f.readlines()
        pending = len(lines)
    with open("done.txt", "r") as done_f:
        lines = done_f.readlines()
        lines = [x for x in lines if x != "\n"]
        completed = len(lines)
    print(f"{today_date} Pending : {pending}, Completed : {completed}")

def helpp():
    print('$ ./todo add "todo item"  # Add a new todo \n \
./todo ls               # Show remaining todos \n \
./todo del NUMBER       # Delete a todo \n \
./todo done NUMBER      # Complete a todo \n \
./todo help             # Show usage \n \
./todo report           # Statistics')


def main():

    parser = argparse.ArgumentParser(description="A text file manager!")

    parser.add_argument("task", type=str, nargs="+", default=None, help='Type suitable command to complete the task')

    args = parser.parse_args()

    given_task = args.task[0]
    if given_task == "add":
        add(args)
    elif given_task == "ls":
        show()
    elif given_task == "del":
        delete(args)
    elif given_task == "done":
        done(args)
    elif given_task == "report":
        report()
    elif given_task == "help":
        helpp()
    elif given_task == " ":
        helpp()

if __name__ == "__main__":
    main()
