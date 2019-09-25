# Create a notebook or python script named pandas_exercises to do your work in for this exercise.

# For the following exercises, you'll need to load several datasets using the pydataset library. 
# (If you get an error when trying to run the import below, use pip to install the pydataset 
# package.)

from pydataset import data

# When the instructions say to load a dataset, you can pass the name of the dataset as a string 
# to the data function to load the dataset. You can also view the documentation for the data set 
# by passing the show_doc keyword argument.

mpg = data('mpg') # load the dataset and store it in a variable
# data('mpg', show_doc=True) # view the documentation for the dataset

# 1. Load the mpg dataset. Read the documentation for it, and use the data to answer these questions:

#   a. On average, which manufacturer has the best miles per gallon?

mpg['manufacturer'].unique().size

mpg['average_mileage'] = (mpg['cty'] + mpg['hwy'])/2

mpg['average_mileage'][mpg['manufacturer'] == 'audi'].mean()
mpg['average_mileage'][mpg['manufacturer'] == 'chevrolet'].mean()
mpg['average_mileage'][mpg['manufacturer'] == 'dodge'].mean()
mpg['average_mileage'][mpg['manufacturer'] == 'ford'].mean()
mpg['average_mileage'][mpg['manufacturer'] == 'honda'].mean()
mpg['average_mileage'][mpg['manufacturer'] == 'hyundai'].mean()
mpg['average_mileage'][mpg['manufacturer'] == 'jeep'].mean()
mpg['average_mileage'][mpg['manufacturer'] == 'land rover'].mean()
mpg['average_mileage'][mpg['manufacturer'] == 'lincoln'].mean()
mpg['average_mileage'][mpg['manufacturer'] == 'mercury'].mean()
mpg['average_mileage'][mpg['manufacturer'] == 'nissan'].mean()
mpg['average_mileage'][mpg['manufacturer'] == 'pontiac'].mean()
mpg['average_mileage'][mpg['manufacturer'] == 'subaru'].mean()
mpg['average_mileage'][mpg['manufacturer'] == 'toyota'].mean()
mpg['average_mileage'][mpg['manufacturer'] == 'volkswagen'].mean()

mpg['average_mileage'][mpg['manufacturer']]

mpg['average_mileage'].describe()

mpg['average_mileage'][mpg['manufacturer'].mean().unique()]

#   b. How many different manufacturers are there?



#   c. ow many different models are there?



#   d. Do automatic or manual cars have better miles per gallon?



# 2. Joining and Merging

#   a. Copy the users and roles dataframes from the examples above. What do you think a right join 
#      would look like? An outer join? What happens if you drop the foreign keys from the dataframes 
#      and try to merge them?



# 3. Getting data from SQL databases

#   a. Create a function named get_db_url. It should accept a username, hostname, password, and 
#      database name and return a url formatted like in the examples in this lesson.


#   b. Use your function to obtain a connection to the employees database.



#   c. Once you have successfully run a query:

#      Intentionally make a typo in the database url. What kind of error message do you see?


#      Intentionally make an error in your SQL query. What does the error message look like?



#   d. Read the employees and titles tables into two separate dataframes
#   e. Visualize the number of employees with each title.
#   f. Join the employees and titles dataframes together.
#   g. Visualize how frequently employees change titles.
#   h. For each title, find the hire date of the employee that was hired most recently with that title.
#   i. Write the code necessary to create a cross tabulation of the number of titles by department. 
#      (Hint: this will involve a combination of SQL and python/pandas code)



# 4. Use your get_db_url function to help you explore the data from the chipotle database. Use the 
#    data to answer the following questions:

#   a. What is the total price for each order?



#   b. What are the most popular 3 items?



#   c. Which item has produced the most revenue?



# More Practice

# For even more practice with pandas, you can do the exercises from the SQL module, but 
# instead of using SQL to do the aggregation, sorting, joining, etc, use pandas. That is, 
# read the data from all of the tables into pandas dataframes and manipulate the dataframes