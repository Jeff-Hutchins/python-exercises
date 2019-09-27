# Create a notebook or python script named pandas_exercises to do your work in for this exercise.

# For the following exercises, you'll need to load several datasets using the pydataset library. 
# (If you get an error when trying to run the import below, use pip to install the pydataset 
# package.)

from pydataset import data
import pandas as pd
import numpy as np

# When the instructions say to load a dataset, you can pass the name of the dataset as a string 
# to the data function to load the dataset. You can also view the documentation for the data set 
# by passing the show_doc keyword argument.

mpg = data('mpg') # load the dataset and store it in a variable
# data('mpg', show_doc=True) # view the documentation for the dataset

# 1. Load the mpg dataset. Read the documentation for it, and use the data to answer these questions:

#   a. On average, which manufacturer has the best miles per gallon?
mpg
mpg['manufacturer'].unique().size

mpg['average_mileage'] = (mpg['cty'] + mpg['hwy'])/2

manufacturers = mpg.groupby(['manufacturer']).mean()

manufacturers['average_mileage'].idxmax()

#   b. How many different manufacturers are there?

mpg['manufacturer'].unique().size

#   c. How many different models are there?

# models = mpg.groupby(['model']).mean()

mpg.model.unique().size

#   d. Do automatic or manual cars have better miles per gallon?

# fruits[fruits.apply(lambda x: 'berry' in x)]
auto_trans_grouped = mpg[mpg['trans'].str.contains('auto')].groupby(['trans']).mean()
manual_trans_grouped = mpg[mpg['trans'].str.contains('manual')].groupby(['trans']).mean()

auto_mpg = auto_trans_grouped.average_mileage.mean() # 21.66
manual_mpg = manual_trans_grouped.average_mileage.mean() #20.77


# 2. Joining and Merging

#   a. Copy the users and roles dataframes from the examples above. What do you think a right join 
#      would look like? An outer join? What happens if you drop the foreign keys from the dataframes 
#      and try to merge them?

users = pd.DataFrame({
    'id': [1, 2, 3, 4, 5, 6],
    'name': ['bob', 'joe', 'sally', 'adam', 'jane', 'mike'],
    'role_id': [1, 2, 3, 3, np.nan, np.nan]
})
users

roles = pd.DataFrame({
    'id': [1, 2, 3, 4],
    'name': ['admin', 'author', 'reviewer', 'commenter']
})
roles

pd.merge(users, roles, left_on='role_id', right_on='id', how='right')
pd.merge(users, roles, left_on='role_id', right_on='id', how='left')
pd.merge(users, roles, left_on='role_id', right_on='id', how='inner')
pd.merge(users, roles, left_on='role_id', right_on='id', how='outer')


# 3. Getting data from SQL databases

#   a. Create a function named get_db_url. It should accept a username, hostname, password, and 
#      database name and return a url formatted like in the examples in this lesson.

# def get_db_url(user, password, host, database_name):
#     from env import host, user, password
#     return url = f'mysql+pymysql://{user}:{password}@{host}/{database_name}'

import pandas as pd
from env import host, user, password

database_name = "employees"
query = """SELECT * FROM employees"""

url = f'mysql+pymysql://{user}:{password}@{host}/{database_name}'


#   b. Use your function to obtain a connection to the employees database.

df = pd.read_sql(query, url)
df

#   c. Once you have successfully run a query:

#      Intentionally make a typo in the database url. What kind of error message do you see?

database_name = "employee"  # operational error

#      Intentionally make an error in your SQL query. What does the error message look like?

query = """SELECT * FROM employee""" # ProgrammingError

#   d. Read the employees and titles tables into two separate dataframes

employees_query = """SELECT * FROM employees"""
titles_query = """SELECT * FROM titles"""
employees = pd.read_sql(employees_query, url)
titles = pd.read_sql(titles_query, url)
titles

#   e. Visualize the number of employees with each title.

employees_and_titles.groupby(['title']).count()

#   f. Join the employees and titles dataframes together.

employees_and_titles = pd.merge(employees, titles)

#   g. Visualize how frequently employees change titles.

employees_and_titles[['first_name', 'last_name', 'title']]

#   h. For each title, find the hire date of the employee that was hired most recently with that title.

employees_and_titles.groupby(['hire_date']).max().tail(1)
 
# i. Write the code necessary to create a cross tabulation of the number of titles by department. 
#      (Hint: this will involve a combination of SQL and python/pandas code)

departments_and_dept_emp_query = """SELECT * FROM departments join dept_emp on dept_emp.dept_no = departments.dept_no"""
departments_and_dept_emp = pd.read_sql(departments_query, url)
departments_and_dept_emp
titles_departments_dept_emp = pd.merge(titles, departments_and_dept_emp)
titles_dept_name = titles_departments_dept_emp[['title', 'dept_name']]
titles_dept_name.groupby('dept_name').count()

# 4. Use your get_db_url function to help you explore the data from the chipotle database. Use the 
#    data to answer the following questions:

database_name = "chipotle"
orders_query = """SELECT * FROM orders"""

url = f'mysql+pymysql://{user}:{password}@{host}/{database_name}'

orders = pd.read_sql(orders_query, url)
orders

#   a. What is the total price for each order?

order_id_and_price['price'] = order_id_and_price['item_price'].str.replace('$',' ').str.strip().str.replace(',','_').astype(float)
order_id_and_price

orders[['order_id', 'item_price']].groupby(['order_id']).sum()

order_price = order_id_and_price[['order_id', 'price']]
order_price.groupby(['order_id']).sum()

#   b. What are the most popular 3 items?
orders_by_item_name = orders[['item_name', 'quantity']].groupby(['item_name']).count()
orders_by_item_name['quantity']

#   c. Which item has produced the most revenue?



# More Practice

# For even more practice with pandas, you can do the exercises from the SQL module, but 
# instead of using SQL to do the aggregation, sorting, joining, etc, use pandas. That is, 
# read the data from all of the tables into pandas dataframes and manipulate the dataframes