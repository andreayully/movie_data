import psycopg2
import pandas as pd
from sqlalchemy import create_engine

conn = psycopg2.connect(
    host="localhost",
    database="GAPInterviews",
    user="postgres",
    password="postgres")
cursor = conn.cursor()


def _dict_helper(desc, row):
    # Returns a dictionary for the given cursor.description and result row.
    return dict([(desc[col[0]][0], col[1]) for col in enumerate(row)])


def dictfetchall(cursor):
    # Returns all rows from a cursor as a dict
    desc = cursor.description
    return [_dict_helper(desc, row) for row in cursor.fetchall()]


query_writters = """
SELECT t.tconst, t.primarytitle as primaryTitle, n.primaryName as Writername
FROM public.titles t, crew cr, names n
WHERE t.tconst = cr.tconst
AND n.nconst IN (SELECT split_part(writers,', ', 2) FROM crew)
limit 100
"""

query_directors = """
SELECT t.tconst, t.primarytitle as primaryTitle, n.primaryName as Directorname
FROM public.titles t, crew cr, names n
WHERE t.tconst = cr.tconst
AND n.nconst IN (SELECT split_part(directors,', ', 2) FROM crew)
limit 100
"""

cursor.execute(query_writters)
data_wirters = dictfetchall(cursor)
df_writers = pd.DataFrame(data_wirters)

cursor.execute(query_directors)
data_directors = dictfetchall(cursor)
df_directors = pd.DataFrame(data_directors)
print("###WRITERS####")
print(df_writers.head())
print("###DIRECTORS####")
print(df_directors.head())
