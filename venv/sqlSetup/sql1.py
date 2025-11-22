import mysql.connector

# Connect to MySQL
conn = mysql.connector.connect(
    host="localhost",
    user="root",       # replace with your MySQL username
    password="shika",  # replace with your MySQL password
    database="mysql"  # replace with your database name
)

cursor = conn.cursor()

# Run a query
cursor.execute("SELECT DATABASE();")
print("Connected to:", cursor.fetchone())

# Create a sample table and insert data
cursor.execute("""
CREATE TABLE IF NOT EXISTS users (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(100),
    email VARCHAR(100)
)
""")

cursor.execute("INSERT INTO users (name, email) VALUES (%s, %s)", ("Alice", "alice@example.com"))
cursor.execute("INSERT INTO users (name, email) VALUES (%s, %s)", ("Bob", "bob@example.com"))

conn.commit()  # save changes

cursor.execute("SELECT * FROM users")
for row in cursor.fetchall():
    print(row)


# Clean up
cursor.close()
conn.close()
