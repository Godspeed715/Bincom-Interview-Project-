import psycopg2
import os
from dotenv import load_dotenv
load_dotenv()

DB_PASSWORD = os.getenv("DB_PASSWORD")
DB_URI = f"postgresql://postgres:{DB_PASSWORD}@localhost:5432/postgres"

class Task:
    def __init__(self, title, status="Pending"):
        with psycopg2.connect(DB_URI) as conn:
            with conn.cursor() as cur:
                add_task_query = """
                INSERT INTO todos (title, status)
                VALUES (%s, %s)
                """
                cur.execute(add_task_query, (title, status))
                conn.commit()
        self.title = title
        self.status = status

    def complete(id):
        with psycopg2.connect(DB_URI) as conn:
            with conn.cursor() as cur:
                complete_query = """
                UPDATE todos SET status = 'Done' WHERE id = %s
                """
                cur.execute(complete_query, (id,))
                conn.commit()
        print(f"Task '{get_task_title(id)[0]}' marked Done.")

    def show_info(self):
        print(f"[{self.title}] - {self.status}")

def create_table():
    with psycopg2.connect(DB_URI) as conn:
        with conn.cursor() as cur:
            create_table_query = '''
            CREATE TABLE IF NOT EXISTS todos (
                id INT GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
                title TEXT NOT NULL,
                status TEXT NOT NULL DEFAULT 'Pending',
                created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
            )
            '''

            cur.execute(create_table_query)
            conn.commit()

def show_tasks():
    with psycopg2.connect(DB_URI) as conn:
        with conn.cursor() as cur:
            show_tasks_query = """
            SELECT * FROM todos
            """
            cur.execute(show_tasks_query)
            tasks = cur.fetchall()
    return tasks

def get_task_title(id):
    with psycopg2.connect(DB_URI) as conn:
        with conn.cursor() as cur:
            show_tasks_query = """
            SELECT title FROM todos WHERE id = %s
            """
            cur.execute(show_tasks_query, (id,))
            task = cur.fetchone()
    return task

if __name__ == '__main__':
    create_table()


    session_tasks = []

    while True:
        print("\nTODO APP: Select an option: ")
        print("1. Add a Task")
        print("2. View Session Tasks")
        print("3. Complete a Task")
        print("4. Exit")
        choice = input("Enter your choice: ")
        print()

        # Add a task using Task.__init__
        if choice == "1":
            title_input = input("Title: ")
            new_task = Task(title=title_input)
            session_tasks.append(new_task)
            print(f"Task '{title_input}' added to the database!")

        # View tasks using Task.show_info
        elif choice == "2":
            tasks = show_tasks()
            if len(tasks) > 0:
                for task in tasks:
                    print(f"ID: {task[0]} | Title: {task[1]} | Status: {task[2]}" )
            else:
                print("You don't have any tasks.")


        # Complete a task using Task.complete
        elif choice == "3":
            try:
                task_id = int(input("Enter the List ID of the task to complete: "))
                if task_id > 0:
                    Task.complete(task_id)
                else:
                    print("Invalid Task ID.")
            except ValueError:
                print("Please enter a valid number.")

        # Exit the Application
        elif choice == "4":
            print("Thank you for using my application 🤗")
            break

        else:
            print("Invalid choice. Please enter 1, 2, 3, or 4.")