import sqlite3 

class dbadapter:  # Allows connection to the database

    def createdb(self, name):
        # Connect to the database (or create it if it doesn't exist)
        conn = sqlite3.connect(f"{name}.db")
        cursor = conn.cursor()

        # Create transactions table if it doesn't exist
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS transactions (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                date TEXT NOT NULL, 
                amount REAL NOT NULL,
                description TEXT
            )
        ''')

        conn.commit()
        conn.close()

        # Print success message after creating the database and table
        print(f"Database and '{name}' created successfully.")  # Correctly placed inside the method

    def buy(self):
        # Insert a new transaction (buy)
        conn = sqlite3.connect('transactions.db') 
        cursor = conn.cursor()

        # Properly formatted SQL query
        cursor.execute("INSERT INTO transactions (date, amount, description) VALUES ('2025-01-20', 3.10, 'rome')")
        conn.commit()

        conn.close()
        print("Transaction added successfully.")

    def read(self):
        # Read all transactions from the database
        conn = sqlite3.connect('transactions.db')
        cursor = conn.cursor()

        cursor.execute("SELECT * FROM transactions")
        transactions = cursor.fetchall()  # Corrected typo from ferchall() to fetchall()

        # Create a list of transactions as dictionaries
        transaction_list = []
        for transaction in transactions:
            transaction_data = {
                'id': transaction[0],
                'date': transaction[1],
                'amount': transaction[2],
                'description': transaction[3]
            }
            transaction_list.append(transaction_data)

        conn.close()
        return transaction_list

    def sell(self, transaction_id):
        """מכירת נייר ערך (מחיקת עסקה)"""
        conn = sqlite3.connect('transactions.db')
        cursor = conn.cursor()

        cursor.execute("DELETE FROM transactions WHERE id = ?", (transaction_id,))
        conn.commit()
        conn.close()
        print(f"Transaction with ID {transaction_id} has been deleted.")

    def update(self, transaction_id, new_amount, new_description):
        conn = sqlite3.connect('transactions.db')
        cursor = conn.cursor()

        cursor.execute("UPDATE transactions SET amount = ?, description = ? WHERE id = ?",
                   (new_amount, new_description, transaction_id))
        conn.commit()
        conn.close()
        print(f"Transaction with ID {transaction_id} has been updated.")

    # Placeholder for sell logic
       
