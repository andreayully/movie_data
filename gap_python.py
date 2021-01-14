import psycopg2
import pandas as pd

"""
Clean the data from CSV files
INSERT data intro database tables 
"""

conn = psycopg2.connect(
    host="localhost",
    database="GAPInterviews",
    user="postgres",
    password="postgres")
cursor = conn.cursor()


def print_connection():
    print('PostgreSQL database version:')
    cursor.execute('SELECT version()')
    db_version = cursor.fetchone()
    print(db_version)


data_crew = pd.read_csv('crew.csv')
data_title = pd.read_csv('titles.csv')
data_names = pd.read_csv('names.csv')

"""remove characters"""
column_tt = data_crew.tconst.apply(
    lambda const: const.replace('tt', '') if type(const) == str else const
)

column_director = data_crew.directors.apply(
    lambda const: const.replace('nm', ' ') if type(const) == str else const
)

column_writers = data_crew.writers.apply(
    lambda const: const.replace('nm', ' ') if type(const) == str else const
)

column_tt_title = data_title.tconst.apply(
    lambda const: const.replace('tt', '') if type(const) == str else const
)
column_nconst_names = data_names.nconst.apply(
    lambda const: const.replace('nm', '') if type(const) == str else const
)

column_knownForTitles_names = data_names.knownForTitles.apply(
    lambda const: const.replace('tt', ' ') if type(const) == str else const
)
"""column replacement"""
data_crew_copy = data_crew.copy()
data_crew_copy.tconst = column_tt
data_crew_copy.directors = column_director
data_crew_copy.writers = column_writers

data_title_copy = data_title.copy()
data_title_copy.tconst = column_tt_title

data_names_copy = data_names.copy()
data_names_copy.nconst = column_nconst_names
data_names_copy.knownForTitles = column_knownForTitles_names


def insert_data(data, table_name):
    """
    Function to insert data into table
    :param data: datafrane
    :param table_name:
    :return: None
    """
    title_cols = ", ".join([str(i) for i in data.columns.tolist()])
    for i, row in data.iterrows():
        sql = "INSERT INTO {} (" + title_cols + ") VALUES (" + "%s," * (len(row) - 1) + "%s)".format(table_name)
        cursor.execute(sql, tuple(row))
        conn.commit()
    print("END")


title_cols = ", ".join([str(i) for i in data_names_copy.columns.tolist()])

for i, row in data_names_copy.iterrows():
    sql = "INSERT INTO names (" + title_cols + ") VALUES (" + "%s," * (len(row) - 1) + "%s)"
    cursor.execute(sql, tuple(row))
    conn.commit()
print("END")
