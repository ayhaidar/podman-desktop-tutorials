import pyodbc
import pandas as pd
import time
import os

# Configuration (Best practice: use environment variables from your compose file)
DB_CONFIG = {
    'server': os.getenv('DB_SERVER', 'your-corp-sql-server'),
    'database': os.getenv('DB_NAME', 'SalesDB'),
    'table': os.getenv('TB_NAME', 'SalesTB'),
    'user': os.getenv('DB_USER', 'your_user'),
    'pass': os.getenv('DB_PASS', 'your_password')
}

# The internal path we mapped in the Dockerfile, specified in services --> data-puller --> volumes
OUTPUT_PATH = "/var/lib/exports/data.csv"

def fetch_data():
    conn_str = (
        f"DRIVER={{ODBC Driver 18 for SQL Server}};"
        f"SERVER={DB_CONFIG['server']};"
        f"DATABASE={DB_CONFIG['database']};"
        f"UID={DB_CONFIG['user']};"
        f"PWD={DB_CONFIG['pass']};"
        "Encrypt=yes;"
        "TrustServerCertificate=yes;"
    )
    
    print("Connecting to MSSQL...")
    with pyodbc.connect(conn_str) as conn:
        table= DB_CONFIG['table']
        query = f"SELECT TOP 100 * FROM {table} ORDER BY DateRead DESC"
        df = pd.read_sql(query, conn)
        
        # Save to the shared volume
        df.to_csv(OUTPUT_PATH, index=False)
        print(f"Data refreshed at {time.ctime()} and saved to {OUTPUT_PATH}")

if __name__ == "__main__":
    fetch_data()
