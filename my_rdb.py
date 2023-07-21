import mysql.connector

def read_database(host, database, user, password, table, field):
    # Connect to the MySQL database
    db_connection = mysql.connector.connect(
        host=host,
        database=database,
        user=user,
        password=password
    )

    # Get all the rows of the specified field from the table
    cursor = db_connection.cursor()
    cursor.execute(f"SELECT {field} FROM {table} LIMIT 100000")
    results = cursor.fetchall()

    # Write the results to a text file
    with open("../out/news.txt", "w") as f:
      for row in results:
         if row[0] is not None:
             f.write(row[0] + "\n")
         else:
             f.write("-" + "\n")

if __name__ == "__main__":
    # Set the connection parameters
    host = ""
    database = "news"
    user = "abi"
    password = ""
    table = "text"
    field = "article"

    # Read the database and write the results to a text file
    read_database(host, database, user, password, table, field)

