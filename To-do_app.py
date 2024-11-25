def task():
    tasks = []
    # empty list
    print("---Welcome to The Task Management App---")

    total_tasks = int(input("Enter how many tasks you want to add: "))
    for i in range(1, total_tasks+1):
        task_name = input(f"Enter the task {i}: ")
        tasks.append(task_name)

    print(f"Today's tasks are {tasks}")

    while True:
        operation = input("Enter the number..\n1-Add\n2-Update\n3-Delete\n4-View\n5-Exit(stop)\nEnter here: ")
        if operation == "1":
            add = input("Enter task you want to add: ")
            tasks.append(add)
            print(f"Task {add} has been added successfully..")

        elif operation == "2":
            update = input("Enter task name you want to update: ")
            if update in tasks:
                up = input("Enter new task: ")
                ind = tasks.index(update)
                tasks[ind] = up
                print(f"Updated task {up}.")

        elif operation == "3":
            delete = input("Enter the task you want to delete: ")
            if delete in tasks:
                ind = tasks.index(delete)
                del tasks[ind]
                print(f"Task {delete} has been deleted..")

        elif operation == "4":
            print(f"Today's total tasks: {tasks}")

        elif operation == "5":
            print("Closing the program...")
            break

        else:
            print("Invalid input!")


task()
