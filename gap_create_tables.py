import psycopg2
"""
Create tables from files structure
"""


conn = psycopg2.connect(
    host="localhost",
    database="GAPInterviews",
    user="postgres",
    password="postgres")
cursor = conn.cursor()

create_title_table = """
    CREATE TABLE titles (
    tconst varchar(255) NOT NULL,
    titleType varchar(255),
    primaryTitle varchar(255),
    originalTitle varchar(255),
    isAdult varchar(255),
    startYear varchar(255),
    endYear varchar(255),
    runtimeMinutes varchar(255),
    genres varchar(255),
    PRIMARY KEY (tconst)
);
"""

create_names_table = """
    CREATE TABLE names (
    nconst varchar(255) NOT NULL,
    primaryName varchar(255),
    birthYear varchar(255),
    deathYear varchar(255),
    primaryProfession varchar(255),
    knownForTitles varchar(255),
    PRIMARY KEY (nconst));
"""

create_crew_table = """
    CREATE TABLE crew (
    tconst varchar(255) NOT NULL,
    directors varchar(500),
    writers varchar(500),
    PRIMARY KEY (tconst));
"""

cursor.execute(create_title_table)
cursor.execute(create_names_table)
cursor.execute(create_crew_table)
conn.commit()
