import mysql.connector
import os
import time
import tqdm

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
    cursor.execute(f"SELECT {field} FROM {table} WHERE src IN ('nst', 'thestar', 'theedge', 'thesundaily','malaysianow','newsarawaktribune', 'borneopost', 'fmt', 'agendadaily', 'airtimes','antarapos','astroawani','amanahdaily','beritaharian','bernama', 'harakah', 'hmetro', 'hmetro', 'kosmo', 'malaysiadateline', 'sinarharian','sarawakvoice', 'umnoonline', 'utusan') LIMIT 700")
    results = cursor.fetchall()

    # Use tqdm to display a progress bar
    with tqdm.tqdm(total=cursor.rowcount, mininterval=0.5, leave=True) as pbar:
        for row in results:
            pbar.update()

    return results

    # Write the results to a text file
    with open("/home/abi/minutes/out/news.txt", "w") as f:
      for row in results:
         if row[0] is not None:
             f.write(row[0] + "\n")
         else:
             f.write("-" + "\n")

if __name__ == "__main__":
    # Read the connection parameters from the environment
    host = os.environ["HOST"]
    database = os.environ["DATABASE"]
    user = os.environ["USER"]
    password = os.environ["PASSWORD"]
    table = "text"
    field = "article"

    # Read the database and write the results to a text file
    results = read_database(host, database, user, password, table, field)

