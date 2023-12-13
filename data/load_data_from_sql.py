
import logging
import pandas as pd
import psycopg2

# Setting up logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

def log_decorator(func):
    def wrapper(*args, **kwargs):
        try:
            result = func(*args, **kwargs)
            logger.info(f"{func.__name__} executed successfully.")
            return result
        except Exception as e:
            logger.error(f"Error in {func.__name__}: {str(e)}")
            raise
    return wrapper

@log_decorator
def connect_to_database(db_params: dict) -> psycopg2.extensions.connection:
    """Connect to the PostgreSQL database."""
    conn = psycopg2.connect(**db_params)
    return conn

@log_decorator
def execute_query(conn: psycopg2.extensions.connection, query: str) -> list:
    """Execute a query and return the results."""
    cursor = conn.cursor()
    cursor.execute(query)
    results = cursor.fetchall()
    cursor.close()
    return results

@log_decorator
def read_sql_to_dataframe(conn: psycopg2.extensions.connection, query: str) -> pd.DataFrame:
    """Read SQL query results into a Pandas DataFrame."""
    df = pd.read_sql_query(query, conn)
    return df

@log_decorator
def close_connection(conn: psycopg2.extensions.connection) -> None:
    """Close the database connection."""
    conn.close()

@log_decorator
def get_dataframe(table_name: str) -> pd.DataFrame:
    """Main function to get the DataFrame."""
    db_params = {
        'dbname': 'week-1',
        'user': 'postgres',
        'password': 'postgres',
        'host': 'localhost',
        'port': '5432',
    }

    # Example query
    query = f"SELECT * FROM {table_name};"

    # Connect to the database
    conn = connect_to_database(db_params)

    # Read results into a Pandas DataFrame
    df = read_sql_to_dataframe(conn, query)

    # Close the database connection
    close_connection(conn)

    return df
