tasks = []

def add_task():
  task = input("Enter new task: ")
  tasks.append(task)
  print("Task added successfully!")

def view_tasks():
  if not tasks:
    print("Your to-do list is empty.")
  else:
    print("Your To-Do List:")
    for index, task in enumerate(tasks):
      print(f"{index+1}. {task}")

def mark_complete():
  view_tasks()
  if tasks:
    try:
      task_index = int(input("Enter number of task to mark complete: ")) - 1
      if 0 <= task_index < len(tasks):
        completed_task = tasks.pop(task_index)
        print(f"Task '{completed_task}' marked as complete!")
      else:
        print("Invalid task number.")
    except ValueError:
      print("Invalid input. Please enter a number.")

def main():
  while True:
    print("\nChoose an action:")
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Mark Complete")
    print("4. Exit")

    choice = input("Enter your choice (1-4): ")

    if choice == '1':
      add_task()
    elif choice == '2':
      view_tasks()
    elif choice == '3':
      mark_complete()
    elif choice == '4':
      print("Exiting To-Do List. Goodbye!")
      break
    else:
      print("Invalid choice. Please enter a number between 1 and 4.")

if __name__ == "__main__":
  main()