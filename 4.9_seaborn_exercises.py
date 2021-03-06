from pydataset import data
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

from env import host, user, password

def get_db_url(user, host, password, database_name):
    url = f'mysql+pymysql://{user}:{password}@{host}/{database_name}'
    return url

iris_db_url = get_db_url(user, host, password, 'iris')
iris_db_url

query = "select * from iris"
pd.read_sql(query, iris_db_url)

# Exercises
# Create a file named 4.9_seaborn_exercises.py for this exercise.

# Use the iris database to answer the following quesitons:

iris = sns.load_dataset('iris')
iris.describe()

# 1. What does the distribution of petal lengths look like?

sns.distplot(iris.petal_length) # bi-modal
plt.show()

r = iris.corr().loc['petal_length', 'petal_width']
plt.text(1.5, 2, f'r = {r:.2}')

# 2. Is there a correlation between petal length and petal width?

sns.relplot(x='petal_length', y='petal_width', hue='species', data=iris)
plt.show()

# 3. Would it be reasonable to predict species based on sepal width and sepal length?

sns.relplot(x='sepal_width', y='sepal_length', col='species', data=iris)
plt.show()

# 4. Which features would be best used to predict species?

sns.relplot(x='petal_length', y='petal_width', col='species', hue='species', data=iris)
plt.show()

sns.pairplot(data=iris, hue='species')

# 1. Using the lesson as an example, use seaborn's load_dataset function to load the anscombe 
# data set. Use pandas to group the data by the dataset column, and calculate summary 
# statistics for each dataset. What do you notice?

anscombe = pd.DataFrame(sns.load_dataset('anscombe'))
anscombe
anscombe.groupby('dataset').describe()

# Plot the x and y values from the anscombe data. Each dataset should be in a separate column.

sns.relplot(x='x', y='y', col='dataset', data=anscombe)
plt.show()

# 2. Load the InsectSprays dataset and read it's documentation. Create a boxplot that shows 
# the effectiveness of the different insect sprays.

data('InsectSprays', show_doc=True)
insect_sprays = data('InsectSprays')

insect_sprays

sns.boxplot(data=insect_sprays, y = 'count', x='spray')
plt.show()

# 3. Load the swiss dataset and read it's documentation. Create visualizations to answer 
# the following questions:

data('swiss', show_doc=True)
swiss = data('swiss')
swiss
swiss.describe()

#   Create an attribute named is_catholic that holds a boolean value of whether or not the 
#   province is Catholic. (Choose a cutoff point for what constitutes catholic).
#   Takes continuous variable and treats it as a categorical variable.

swiss['Catholic'].mean()
swiss['Catholic'] > swiss['Catholic'].mean()


#chose the mean of the 'Catholic' column as the cutoff point.  Greater than the mean = True.
swiss['is_catholic'] = swiss['Catholic'] > swiss['Catholic'].mean()
swiss

# Zach's way, cut off at 70.

swiss.Catholic.apply(lambda n: 'Catholic' if n > 70 else)
sns.boxplot(data=swiss, x='is_catholic', y='Fertility')

#   Does whether or not a province is Catholic influence fertility?

swiss.count()
swiss[swiss['is_catholic']].is_catholic.count()
sns.boxplot(x='is_catholic', y='Fertility', data=swiss)
sns.relplot(x='is_catholic', y='Fertility', data=swiss)
(x='is_catholic', y='Fertility', data=swiss)



#   What measure correlates most strongly with fertility?

swiss.corr().Fertility

sns.relplot(x='Education', y='Fertility', data=swiss)
plt.show()

# sns.relplot(x='Agriculture', y='Fertility', data=swiss)
# sns.relplot(x='Examination', y='Fertility', data=swiss)
# sns.relplot(x='Catholic', y='Fertility', data=swiss)
# sns.relplot(x='Infant.Mortality', y='Fertility', data=swiss)
# sns.relplot(x='is_catholic', y='Fertility', data=swiss)

# 4. Using the chipotle dataset from the previous exercise, create a bar chart that shows 
#    the 4 most popular items and the revenue produced by each.

def get_db_url(database_name, table):
    import pandas as pd
    from env import host, user, password
    url = f'mysql+pymysql://{user}:{password}@{host}/{database_name}'
    query = f"SELECT * FROM {database_name}"
    database_name = pd.read_sql(table, url)
    return database_name

get_db_url("chipotle", "orders")
orders = get_db_url("chipotle", "orders")
orders

        #4 most popular items
four_most_popular_items = orders[['item_name', 'quantity', 'revenue']].groupby(['item_name']).sum().sort_values(by='quantity', ascending=False).head(4)
four_most_popular_items

        #Revenue of 4 most popular items
orders['price'] = orders['item_price'].str.replace('$',' ').str.strip().str.replace(',','_').astype(float)
orders

orders['revenue'] = orders['quantity'] * orders['price']
orders

orders[['item_name', 'revenue']].sort_values(by='revenue', ascending=False).head(4)
orders

        # Re-indexed in order to use 'item_name' in bar graph
four_most_popular_items = four_most_popular_items.reset_index()
four_most_popular_items

        # Two barplot graphs of item_name vs revenue and item_name vs quantity
plt.subplot(211)
sns.barplot(data=four_most_popular_items, x='item_name', y= 'revenue')
plt.title('revenue')

plt.subplot(212)
sns.barplot(data=four_most_popular_items, x='item_name', y='quantity')
plt.title('quantity')
plt.show()

# 5. Load the sleepstudy data and read it's documentation. Use seaborn to create a line 
# chart of all the individual subject's reaction times and a more prominant line showing 
# the average change in reaction time.

sleepstudy = data('sleepstudy')
sleepstudy

sleepstudy[['Reaction', 'Days', 'Subject']].groupby(['Subject']).sum()
sleepstudy[sleepstudy['Subject'] == 308]
sleepstudy.Subject.astype(str)
sleepstudy.Subject = 'subject_' + sleepstudy.Subject.astype(str)

sns.relplot(data=sleepstudy, x='Days', y='Reaction', kind='line', hue='Subject')
sns.relplot(data=sleepstudy, x='Days', y='Reaction', kind='line')

sns.lineplot(data=sleepstudy, x='Days', y='Reaction', hue='Subject')
sns.lineplot(data=sleepstudy, x='Days', y='Reaction', color='navy')

