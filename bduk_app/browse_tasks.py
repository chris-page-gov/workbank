import csv

DATA_FILE = 'bduk_app/bduk_tasks.csv'

def load_tasks():
    with open(DATA_FILE, newline='') as f:
        reader = csv.DictReader(f)
        return list(reader)

def display_tasks(tasks):
    print("Available tasks:\n")
    for idx, task in enumerate(tasks, 1):
        print(f"{idx}. {task['task']}")


def get_selection(num_tasks):
    while True:
        try:
            choice = int(input("\nEnter task number to view research findings (0 to exit): "))
            if 0 <= choice <= num_tasks:
                return choice
            print("Invalid selection. Try again.")
        except ValueError:
            print("Please enter a valid number.")


def main():
    tasks = load_tasks()
    if not tasks:
        print("No tasks available.")
        return
    while True:
        display_tasks(tasks)
        choice = get_selection(len(tasks))
        if choice == 0:
            print("Goodbye!")
            break
        task = tasks[choice - 1]
        print("\n" + "="*60)
        print(f"RESEARCH FINDINGS FOR: {task['task']}")
        print("="*60)
        print(f"{task['research_finding']}")
        print("="*60)
        input("\nPress Enter to continue...")


if __name__ == '__main__':
    main()
