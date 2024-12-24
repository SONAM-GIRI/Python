import sqlite3

# Connect to the database (or create it if it doesn't exist)
connection = sqlite3.connect("database_name.db")

# Create a cursor object
cursor = connection.cursor()

# Create the table if it doesn't exist
create_table_query = """
CREATE TABLE IF NOT EXISTS user_data (
    id INTEGER PRIMARY KEY,
    phone TEXT NOT NULL,
    name TEXT NOT NULL
);
"""
cursor.execute(create_table_query)


# Insert Data Function
def insert_data():
    n = int(input("Enter the number of data you want to enter: "))
    for i in range(1, n + 1):
        print(f"\nEnter user data to insert into the table (Record {i}):")
        user_id = int(input("Enter ID: "))
        user_phone = input("Enter Phone Number: ")
        user_name = input("Enter Name: ")

        # SQL insert query
        insert_query = """
        INSERT INTO user_data (id, phone, name)
        VALUES (?, ?, ?);
        """
        data = (user_id, user_phone, user_name)

        # Execute the query
        cursor.execute(insert_query, data)

    # Commit the transaction
    connection.commit()
    print("\nData inserted successfully!")


# Delete Data Function
def delete_data():
    # Display existing data before deletion
    cursor.execute("SELECT * FROM user_data")
    result = cursor.fetchall()

    if not result:
        print("\nNo data available to delete.")
        return

    print("\nCurrent Data in Table:")
    for row in result:
        print(row)

    delete_id = int(input("\nEnter the ID of the user to delete: "))

    # SQL delete query
    delete_query = """
    DELETE FROM user_data
    WHERE id = ?;
    """
    cursor.execute(delete_query, (delete_id,))

    # Commit the transaction
    connection.commit()
    print(f"\nData with ID {delete_id} has been deleted successfully.")


# Display Data Function
def display_data():
    cursor.execute("SELECT * FROM user_data")
    result = cursor.fetchall()

    if not result:
        print("\nNo data available in the table.")
    else:
        print("\nCurrent Data in Table:")
        for row in result:
            print(row)


# Main Menu
while True:
    print("\nOptions:")
    print("1. Insert Data")
    print("2. Delete Data")
    print("3. Display Data")
    print("4. Exit")

    choice = int(input("\nEnter your choice: "))
    if choice == 1:
        insert_data()
    elif choice == 2:
        delete_data()
    elif choice == 3:
        display_data()
    elif choice == 4:
        print("\nExiting the program.")
        break
    else:
        print("\nInvalid choice. Please try again.")

# Close the connection
connection.close()
