#A function to close connection with databases.
def close_db(conn, cursor):
    conn.commit()
    cursor.close()
    conn.close()