# data.py

import pandas as pd
import psycopg2

def connect_to_database(db_params):
    """Connect to the PostgreSQL database."""
    conn = psycopg2.connect(**db_params)
    return conn

def execute_query(conn, query):
    """Execute a query and return the results."""
    cursor = conn.cursor()
    cursor.execute(query)
    results = cursor.fetchall()
    cursor.close()
    return results

def read_sql_to_dataframe(conn, query):
    """Read SQL query results into a Pandas DataFrame."""
    df = pd.read_sql_query(query, conn)
    return df

def close_connection(conn):
    """Close the database connection."""
    conn.close()

def get_dataframe():
    """Main function to get the DataFrame."""
    # Replace these with your actual database connection details
    db_params = {
        'dbname': 'week-1',
        'user': 'postgres',
        'password': 'postgres',
        'host': 'localhost',
        'port': '5432',
    }

    # Example query
    query = "SELECT * FROM xdr_data;"

    # Connect to the database
    conn = connect_to_database(db_params)

    # Read results into a Pandas DataFrame
    df = read_sql_to_dataframe(conn, query)

    # Close the database connection
    close_connection(conn)

    return df
