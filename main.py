from tasks import load_tasks, add_task, delete_task, toggle_task_status

def main():
    # بارگذاری اولیه تسک‌ها
    tasks = load_tasks()
    
    # شرط اولیه: اگر چیزی در داده‌ها نبود
    if not tasks:
        print("\n[!] there is no task. Please enter your first task")
    
    while True:
        print("\n=== Task Manager ===")
        print("1. View Tasks")
        print("2. Add Task")
        print("3. Toggle Task Status")
        print("4. Delete Task")
        print("5. Exit")
        
        choice = input("\nChoose an option (1-5): ").strip()
        
        if choice == "1":
            tasks = load_tasks()
            if not tasks:
                print("\nTask list is empty.")
            else:
                print("\n--- Task List ---")
                for t in tasks:
                    status = "[Done]" if t["completed"] else "[Pending]"
                    print(f"ID: {t['id']} | {t['title']} {status}")
                    
        elif choice == "2":
            title = input("Enter task title: ").strip()
            if title:
                msg = add_task(title)
                print(f"\n{msg}")
            else:
                print("\nTitle cannot be empty.")
                
        elif choice == "3":
            try:
                task_id = int(input("Enter task ID to toggle status: "))
                success, msg = toggle_task_status(task_id)
                print(f"\n{msg}")
            except ValueError:
                print("\nPlease enter a valid number.")
                
        elif choice == "4":
            try:
                task_id = int(input("Enter task ID to delete: "))
                success, msg = delete_task(task_id)
                print(f"\n{msg}")
            except ValueError:
                print("\nPlease enter a valid number.")
                
        elif choice == "5":
            print("\nGoodbye!")
            break
        else:
            print("\nInvalid choice. Please try again.")

if __name__ == "__main__":
    main()