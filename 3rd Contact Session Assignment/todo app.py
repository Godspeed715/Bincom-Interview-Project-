import psycopg
import os
from dotenv import load_dotenv
load_dotenv()

DB_PASSWORD = os.getenv("DB_PASSWORD")
DB_URI = f"postgresql://postgres:{DB_PASSWORD}@localhost:5432/postgres"

def create_table():
    with psycopg.connect(DB_URI) as conn:
        with conn.cursor() as cur:
            create_table_query = '''
            CREATE TABLE IF NOT EXISTS todos (
                id INT GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
                title TEXT NOT NULL,
                description TEXT,
                created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
            )
            '''

            cur.execute(create_table_query)
            conn.commit()

def insert_todo(title, description):
    with psycopg.connect(DB_URI) as conn:
        with conn.cursor() as cur:
            insert_query = '''
            INSERT INTO todos (title, description)
            VALUES (%s, %s)
                           '''
            cur.execute(insert_query, (title, description))
            conn.commit()
    print("Task inserted")

def get_all_todos():
    with psycopg.connect(DB_URI) as conn:
        with conn.cursor() as cur:
            get_query = '''
            SELECT id,title FROM todos'''
            todos = cur.execute(get_query).fetchall()
            return todos

def get_todo(id):
    with psycopg.connect(DB_URI) as conn:
        with conn.cursor() as cur:
            get_query = '''
            SELECT * FROM todos WHERE id = %s
                        '''
            todo = cur.execute(get_query, (id,)).fetchone()
            return todo

def delete_todo(id):
    with psycopg.connect(DB_URI) as conn:
        with conn.cursor() as cur:
            delete_query = '''
            DELETE FROM todos WHERE id = %s'''
            cur.execute(delete_query, (id,))
            conn.commit()
    print("Task deleted")
    print()


def update_todo(id, title, description):
    with psycopg.connect(DB_URI) as conn:
        with conn.cursor() as cur:
            update_query = """
            UPDATE todos SET title = %s, description = %s WHERE id = %s
            """
            cur.execute(update_query, (title, description,id))
            conn.commit()
    print("Task updated")

def display_tasks(todos):
    print("Your tasks")
    for task in todos:
        print(task[0], task[1])
    print()

if __name__ == '__main__':
    create_table()
    while True:
        print("This is a TODO app, you can perform the following actions:\n1. View All Tasks\n2. Add Tasks\n3. View a Task and Details\n4. Delete Tasks\n5. Update Tasks\n6. Exit")
        choice = input("Enter your choice: ")
        print()
        # View All Tasks
        if choice == "1":
            todos = get_all_todos()
            display_tasks(todos)
        # Add a task
        elif choice == "2":
            insert_todo(title=input("Title: "), description=input("Description: "))
        # View a Task
        elif choice =="3":
            print("Enter the id of the task:")
            task = get_todo(input("id: "))
            print()
            print(f"ID: {task[0]}\nTitle: {task[1]}\nDescription: {task[2]}")
            print()
        #   Delete a Task
        elif choice == "4":
            delete_todo(input("Enter the id of the task to delete: "))
        #     Update Todo
        elif choice == "5":
            todo_id = input("Enter the id of the task to update: ")
            todo = get_todo(todo_id)
            print("Title: ", todo[1]," => ", end=" ")
            new_title = input("")
            print()
            print("Description: ", todo[2]," => ", end=" ")
            new_description = input("")
            update_todo(todo_id, new_title, new_description)
        # Exit the Application
        elif choice == "6":
            exit()

print("Thank you for using my application🤗")