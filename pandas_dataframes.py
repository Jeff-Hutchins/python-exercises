import pandas as pd
import numpy as np

np.random.seed(123)

students = ['Sally', 'Jane', 'Suzie', 'Billy', 'Ada', 'John', 'Thomas',
            'Marie', 'Albert', 'Richard', 'Isaac', 'Alan']

# randomly generate scores for each student for each subject
# note that all the values need to have the same length here
math_grades = np.random.randint(low=60, high=100, size=len(students))
english_grades = np.random.randint(low=60, high=100, size=len(students))
reading_grades = np.random.randint(low=60, high=100, size=len(students))

df = pd.DataFrame({'name': students,
                   'math': math_grades,
                   'english': english_grades,
                   'reading': reading_grades})

type(df)
df
df.info()
df.describe()
df.dtypes
df.shape
df.columns
df.index
df.columns = [col.upper() for col in df.columns]
df.columns = [col.lower() for col in df.columns]

# We can see multiple columns in the dataframe by subsetting the dataframe with a list of strings. 
# The following two code samples are functionally equivalent.
df[['name', 'english']]
# functionally the same thing
columns = ['name', 'english']
df[columns]

# Each column in a dataframe is a Series that we discussed in the previous lesson. 
# These values can be accessed in one of two ways:

df.math
df['math']

df.head(2)
df.tail(4)
df.sample(3)

df[df.math < 80]

df.drop(columns=['english','reading'])
df.rename(columns={'name':'student'})
df.drop(columns=['english','reading']).rename(columns={'name':'student'})
df['passing_math'] = df.math >= 70
df.assign(passing_english = df.english >= 70)

df.sort_values(by='reading', ascending=False)

df[df.english > 90].sort_values(by='english').head(1).name

# Exercises

# When the instructions say to load a dataset, you can pass the name of the dataset
# as a string to the data function to load the dataset. You can also view the 
# documentation for the data set by passing the show_doc keyword argument.

from pydataset import data

# All the datasets loaded from the pydataset library will be pandas dataframes.

# 1. Copy the code from the lesson to create a dataframe full of student grades.

np.random.seed(123)

students = ['Sally', 'Jane', 'Suzie', 'Billy', 'Ada', 'John', 'Thomas',
            'Marie', 'Albert', 'Richard', 'Isaac', 'Alan']

# randomly generate scores for each student for each subject
# note that all the values need to have the same length here
math_grades = np.random.randint(low=60, high=100, size=len(students))
english_grades = np.random.randint(low=60, high=100, size=len(students))
reading_grades = np.random.randint(low=60, high=100, size=len(students))

df = pd.DataFrame({'name': students,
                   'math': math_grades,
                   'english': english_grades,
                   'reading': reading_grades})

#   a. Create a column named passing_english that indicates whether each student has 
#      a passing grade in english.

df.assign(passing_english = df.english >= 70)
df['passing_english'] = df.english >= 70
df

#   b. Sort the english grades by the passing_english column. How are duplicates handled?

df.sort_values(by='english')

#   c. Sort the english grades first by passing_english and then by student name. 
#      All the students that are failing english should be first, and within the 
#      students that are failing english they should be ordered alphabetically. 
#      The same should be true for the students passing english. 
#      (Hint: you can pass a list to the .sort_values method)

df.sort_values(by='name').sort_values(by='passing_english')

#   d. Sort the english grades first by passing_english, and then by the actual english
#      grade, similar to how we did in the last step.

df.sort_values(by='english').sort_values(by='passing_english')

#   e. Calculate each students overall grade and add it as a column on the dataframe.
#      The overall grade is the average of the math, english, and reading grades.

df['overall_grade'] = round((df.english + df.reading + df.math) / 3)
df

# 2. Load the mpg dataset. Read the documentation for the dataset and use it for the
#    following questions:

data('mpg', show_doc=True)
mpg = data('mpg')
mpg
#   a. How many rows and columns are there?

mpg.shape

#   b. What are the data types of each column?

mpg.dtypes

#   c. Summarize the dataframe with .info and .describe

mpg.info()
mpg.describe()

#   d. Rename the cty column to city.

mpg.rename(columns={'cty':'city'}, inplace=True)

#   e. Rename the hwy column to highway.

mpg.rename(columns={'hwy':'highway'}, inplace=True)


#   f. Do any cars have better city mileage than highway mileage?

mpg[mpg['city'] > mpg['highway']]

#No

#   g. Create a column named mileage_difference this column should contain 
#      the difference between highway and city mileage for each car.

mpg['mileage_difference'] = mpg['highway'] - mpg['city']

#   h. Which car (or cars) has the highest mileage difference?

mpg[mpg['mileage_difference'] > 11]

#   i. Which compact class car has the lowest highway mileage? The best?

mpg[mpg['class'] == 'compact']

#   j. Create a column named average_mileage that is the mean of the city and
#      highway mileage.

# mpg['average_mileage'] = mpg['city'].append(mpg['highway']).mean()
# mpg['city'].append(mpg['highway']).mean()

mpg['average_mileage'] = (mpg['city'] + mpg['highway'])/2
mpg

#   k. Which dodge car has the best average mileage? The worst?

mpg[mpg['average_mileage'] == 39.5]

# 3. Load the Mammals dataset. Read the documentation for it, and use the data to answer these questions:

mammals = data('Mammals')

#   a. How many rows and columns are there?

mammals.shape

#   b. What are the data types?

mammals.dtypes

#   c. Summarize the dataframe with .info and .describe

mammals.info()
mammals.describe()

#   d. What is the the weight of the fastest animal?

mammals.sort_values(by='speed', ascending=False).head(1)

#   e. What is the overal percentage of specials?

((mammals['specials'][mammals['specials'] == 1].count()) / mammals['specials'].count()) * 100

#   f. How many animals are hoppers that are above the median speed? What percentage
#      is this?

# mammals.sort_values(by=above_median_speed).sort_values(by=hoppers)

mammals['speed'].median()
mammals['speed'][mammals['speed'] > 48.0]

hoppers = pd.Series(mammals[mammals['hoppers']])

hoppers[hoppers['speed'] > 48.0]
pandas is awesome

