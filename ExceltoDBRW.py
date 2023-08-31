import pandas as pd
from sqlalchemy import create_engine
import pyodbc

def load_data_to_database(file_path: str, table_name: str, if_exists: str = 'replace'):
    """
    if_exists: Options are 'fail', 'replace', and 'append'.
    """
    # Read data from file
    if file_path.endswith('.xls'):
        df = pd.read_excel(file_path)
    elif file_path.endswith('.csv'):
        df = pd.read_csv(file_path)
    else:
        raise ValueError(f"Unsupported file type: {file_path}")
    
    # Connect to database
    conn = pyodbc.connect('Driver={SQL Server};'
                          'Server=DESKTOP-3U1VJ9P;'
                          'Database=TestDB;'
                          'Trusted_Connection=yes;')
    engine = create_engine('sqlite:///:memory:')
    
    # Load data into table
    df.to_sql(table_name, engine, index=False, if_exists=if_exists)

def read_data_from_database(table_name: str):

    # Connect to database
    conn = pyodbc.connect('Driver={SQL Server};'
                          'Server=DESKTOP-3U1VJ9P;'
                          'Database=TestDB;'
                          'Trusted_Connection=yes;')
    engine = create_engine('sqlite:///:memory:')
    
    # Read data from table
    df = pd.read_sql(f'select * from {table_name}', engine)
    
    return df

load_data_to_database(file_path='data/iris.csv', table_name='iris',if_exists='append')



df = read_data_from_database(table_name='iris')
print(df)
