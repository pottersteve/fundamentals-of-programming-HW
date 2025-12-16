import sys
import os

def Append():
    try:
        task = sys.argv[2]
        try:
            file = open("todo.txt", "a")
            file.write(f"{task}\n")
            print("Task added.")
            file.close()
        except FileNotFoundError:
            print("Empty")       
    except Exception as e:
        print(f"Failed to add task: {e}")

def Show():
    try:
        file = open("todo.txt", "r")
        tasks = file.readlines()
        file.close()
        i = 1
        for task in tasks:
            print(f"{task.strip()}")
            i += 1
        file.close()
    except FileNotFoundError:
        print("No tasks.")

def Delete():  
    try:
        index = int(sys.argv[2])
        try:
            file_read = open("todo.txt", "r")        
            tasks = file_read.readlines()
        except FileNotFoundError:
            print("Empty read file.")
            return

        if index < 1 or index > len(tasks):
            print(f"Error: Task {index} does not exist.")
            return
        
        cleanfuckkingfuck = []
        for line in tasks:
            if line.strip()!="":
                cleanfuckkingfuck.append(line.rstrip("\n"))

        newFile = []
        i = 1

        for task in cleanfuckkingfuck:
            if i != index:
                if ". " in task:
                    parts = task.split(". ", 1)
                    task_text = parts[1]
                else:
                    task_text = task
                newFile.append(task_text)
            i += 1

        file_write = open("todo.txt", "w")

        i = 1
        for task in newFile:
            file_write.write(f"{i}. {task}\n")
            i += 1

        print("Task deleted.")

        file_read.close()
        file_write.close()

    except FileNotFoundError:
        print("Empty")

def main():
    command = sys.argv[1]
    if command == "add":
        Append()
    elif command == "list":
        Show()
    elif command == "delete":
        Delete()

if __name__ == "__main__":
    
    main()