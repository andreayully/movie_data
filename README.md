# Repository for Movie data 

- Make sure to create a Python virtual enviroment
[Virtual Environments for more info](https://docs.python.org/3/tutorial/venv.html)
  
- Postgres was used as a database
- Python and the Pandas library were used for cleaning and presenting the data
  
### Purpose
Create tables from CSV files  
Use python to retrieve data from the tables

* Create the tables in a postgresql database 
~~~
python gap_create_tables.py
~~~

* Clean the data and insert the data into the tables

~~~
python gap_python.py
~~~

* Perform SQL queries, convert data to dataframes
~~~
python gap_querys.py
~~~
