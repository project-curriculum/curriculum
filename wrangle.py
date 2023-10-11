from env import get_connection
import pandas as pd
import os


def sql_query(db='None', query='None'):
    """ This function is used to quickly create a SQL query! """
    if db == 'None':
        print('Database not specified.')
    elif query == 'None':
        print('No query!')
    else:
        db_url = get_connection(db)
        df = pd.read_sql(query, db_url)
        return df
