# Wrangle Data With pandas

#======================================================================================================
# Install numpy and pandas

pip install numpy
pip install pandas

#======================================================================================================
# Import numpy and pandas

import numpy as np
import pandas as pd

#======================================================================================================
# Build DataFrame from scratch

transactions = pd.DataFrame({
    'TransactionID': np.arange(10)+1,
    'TransactionDate': pd.to_datetime(['2010-08-21', '2011-05-26', '2011-06-16', '2012-08-26', '2013-06-06', 
                              '2013-12-23', '2013-12-30', '2014-04-24', '2015-04-24', '2016-05-08']).date,
    'UserID': [7, 3, 3, 1, 2, 2, 3, np.nan, 7, 3],
    'ProductID': [2, 4, 3, 2, 4, 5, 4, 2, 4, 4],
    'Quantity': [1, 1, 1, 3, 1, 6, 1, 3, 3, 4]
})

#======================================================================================================
# Read data from a CSV file

# Load transactions
transactions = pd.read_csv('https://raw.githubusercontent.com/ben519/DataWrangling/master/Data/transactions.csv')

#======================================================================================================
# Meta info

# Q1 Full summary


# Q2 How many rows?


# Q3 How many columns?


# Q4 Get the row names


# Q5 Get the column names


# Q6 Change the name of column "Quantity" to "Quant"


# Q7 Change the name of columns ProductID and UserID to PID and UID respectively


#======================================================================================================
# Q8 Ordering the rows of a DataFrame

# Q9 Order the rows of transactions by TransactionID descending


# Q10 Order the rows of transactions by Quantity ascending, TransactionDate descending


#======================================================================================================
# Q11 Ordering the columns of a DataFrame

# Q12 Set the column order of transactions as ProductID, Quantity, TransactionDate, TransactionID, UserID


# Q13 Make UserID the first column of transactions


#======================================================================================================
# Q14 Extracting arrays from a DataFrame

# Q15 Get the 2nd column


# Q16 Get the ProductID array


# Q17 Get the ProductID array using a variable


#======================================================================================================
# Row subsetting

# Q18 Subset rows 1, 3, and 6


# Q19 Subset rows exlcuding 1, 3, and 6


# Q20 Subset the first 3 rows


# Q21 Subset rows excluding the first 3 rows


# Q22 Subset the last 2 rows


# Q23 Subset rows excluding the last 2 rows


# Q24 Subset rows where Quantity > 1


# Q25 Subset rows where UserID = 2


# Q26 Subset rows where Quantity > 1 and UserID = 2


# Q27 Subset rows where Quantity + UserID is > 3


# Q28 Subset rows where an external array, foo, is True

# Q29 Subset rows where an external array, bar, is positive


# Q30 Subset rows where foo is TRUE or bar is negative


# Q31 Subset the rows where foo is not TRUE and bar is not negative


#======================================================================================================
# Column subsetting

# Q32 Subset by columns 1 and 3


# Q33 Subset by columns TransactionID and TransactionDate


# Q34 Subset rows where TransactionID > 5 and subset columns by TransactionID and TransactionDate


# Q35 Subset columns by a variable list of columm names



# Q36 Subset columns excluding a variable list of column names
#======================================================================================================
# Inserting and updating values

# Q37 Convert the TransactionDate column to type Date


# Q38 Insert a new column, Foo = UserID + ProductID


# Q39 Subset rows where TransactionID is even and set Foo = NA


# Q40 Add 100 to each TransactionID

# Q41 Insert a column indicating each row number


# Q42 Insert columns indicating the rank of each Quantity, minimum Quantity and maximum Quantity

# Q43 Remove column Foo


# Q44 Remove multiple columns RowIdx, QuantityRk, and RowIdx


#======================================================================================================
# Grouping the rows of a DataFrame

#--------------------------------------------------
# Group By + Aggregate

# Q45 Group the transations per user, measuring the number of transactions per user
# 46 Group the transactions per user, measuring the transactions and average quantity per user



#======================================================================================================
# Joining DataFrames

# Q 47 Load datasets from CSV


# Q48 Convert date columns to Date type


#--------------------------------------------------
# Basic Joins

# Q49 Join users to transactions, keeping all rows from transactions and only matching rows from users (left join)


# Q50 Which transactions have a UserID not in users? (anti join)


# Q51 Join users to transactions, keeping only rows from transactions and users that match via UserID (inner join)


# Q52 Join users to transactions, displaying all matching rows AND all non-matching rows (full outer join)


# Q53 Determine which sessions occured on the same day each user registered


# Q54 Build a dataset with every possible (UserID, ProductID) pair (cross join)


# Q55 Determine how much quantity of each product was purchased by each user


# Q56 For each user, get each possible pair of pair transactions (TransactionID1, TransactionID2)


# Q57 Join each user to his/her first occuring transaction in the transactions table



#======================================================================================================
# Reshaping a data.table

# Q58 Read datasets from CSV
users = pd.read_csv('https://raw.githubusercontent.com/ben519/DataWrangling/master/Data/users.csv')
transactions = pd.read_csv('https://raw.githubusercontent.com/ben519/DataWrangling/master/Data/transactions.csv')

# Q59 Convert date columns to Date type


# Q60 Add column TransactionWeekday as Categorical type with categories Sunday through Saturday


##################################################################
## Answers are here
##################################################################

# Wrangle Data With pandas

#======================================================================================================
# Install numpy and pandas

pip install numpy
pip install pandas

#======================================================================================================
# Import numpy and pandas

import numpy as np
import pandas as pd

#======================================================================================================
# Build DataFrame from scratch

transactions = pd.DataFrame({
    'TransactionID': np.arange(10)+1,
    'TransactionDate': pd.to_datetime(['2010-08-21', '2011-05-26', '2011-06-16', '2012-08-26', '2013-06-06', 
                              '2013-12-23', '2013-12-30', '2014-04-24', '2015-04-24', '2016-05-08']).date,
    'UserID': [7, 3, 3, 1, 2, 2, 3, np.nan, 7, 3],
    'ProductID': [2, 4, 3, 2, 4, 5, 4, 2, 4, 4],
    'Quantity': [1, 1, 1, 3, 1, 6, 1, 3, 3, 4]
})

#======================================================================================================
# Read data from a CSV file

# Load transactions
transactions = pd.read_csv('https://raw.githubusercontent.com/ben519/DataWrangling/master/Data/transactions.csv')

#======================================================================================================
# Meta info

# Q1 Full summary
transactions.info()

# Q2 How many rows?
transactions.shape[0]

# Q3 How many columns?
transactions.shape[1]

# Q4 Get the row names
transactions.index.values

# Q5 Get the column names
transactions.columns.values

# Q6 Change the name of column "Quantity" to "Quant"
transactions.rename(columns={'Quantity': 'Quant'})  # use argument inplace=TRUE to keep the changes

# Q7 Change the name of columns ProductID and UserID to PID and UID respectively
transactions.rename(columns={'ProductID': 'PID', 'UserID': 'UID'})  # use argument inplace=TRUE to keep the changes

#======================================================================================================
# Q8 Ordering the rows of a DataFrame

# Q9 Order the rows of transactions by TransactionID descending
transactions.sort_values('TransactionID', ascending=False)

# Q10 Order the rows of transactions by Quantity ascending, TransactionDate descending
transactions.sort_values(['Quantity', 'TransactionDate'], ascending=[True, False])

#======================================================================================================
# Q11 Ordering the columns of a DataFrame

# Q12 Set the column order of transactions as ProductID, Quantity, TransactionDate, TransactionID, UserID
transactions[['ProductID', 'Quantity', 'TransactionDate', 'TransactionID', 'UserID']]

# Q13 Make UserID the first column of transactions
transactions[pd.unique(['UserID'] + transactions.columns.values.tolist()).tolist()]

#======================================================================================================
# Q14 Extracting arrays from a DataFrame

# Q15 Get the 2nd column
transactions[[1]].values[:, 0]

# Q16 Get the ProductID array
transactions.ProductID.values

# Q17 Get the ProductID array using a variable
col = "ProductID"
transactions[[col]].values[:, 0]

#======================================================================================================
# Row subsetting

# Q18 Subset rows 1, 3, and 6
transactions.iloc[[0,2,5]]

# Q19 Subset rows exlcuding 1, 3, and 6
transactions.drop([0,2,5], axis=0)

# Q20 Subset the first 3 rows
transactions[:3]
transactions.head(3)

# Q21 Subset rows excluding the first 3 rows
transactions[3:]
transactions.tail(-3)

# Q22 Subset the last 2 rows
transactions.tail(2)

# Q23 Subset rows excluding the last 2 rows
transactions.tail(-2)

# Q24 Subset rows where Quantity > 1
transactions[transactions.Quantity > 1]

# Q25 Subset rows where UserID = 2
transactions[transactions.UserID == 2]

# Q26 Subset rows where Quantity > 1 and UserID = 2
transactions[(transactions.Quantity > 1) & (transactions.UserID == 2)]

# Q27 Subset rows where Quantity + UserID is > 3
transactions[transactions.Quantity + transactions.UserID > 3]

# Q28 Subset rows where an external array, foo, is True
foo = np.array([True, False, True, False, True, False, True, False, True, False])
transactions[foo]

# Q29 Subset rows where an external array, bar, is positive
bar = np.array([1, -3, 2, 2, 0, -4, -4, 0, 0, 2])
transactions[bar > 0]

# Q30 Subset rows where foo is TRUE or bar is negative
transactions[foo | (bar < 0)]

# Q31 Subset the rows where foo is not TRUE and bar is not negative
transactions[~foo & (bar >= 0)]

#======================================================================================================
# Column subsetting

# Q32 Subset by columns 1 and 3
transactions.iloc[:, [0, 2]]

# Q33 Subset by columns TransactionID and TransactionDate
transactions[['TransactionID', 'TransactionDate']]

# Q34 Subset rows where TransactionID > 5 and subset columns by TransactionID and TransactionDate
transactions.loc[transactions.TransactionID > 5, ['TransactionID', 'TransactionDate']]

# Q35 Subset columns by a variable list of columm names
cols = ["TransactionID", "UserID", "Quantity"]
transactions[cols]

# Q36 Subset columns excluding a variable list of column names
cols = ["TransactionID", "UserID", "Quantity"]
transactions.drop(cols, axis=1)

#======================================================================================================
# Inserting and updating values

# Q37 Convert the TransactionDate column to type Date
transactions['TransactionDate'] = pd.to_datetime(transactions.TransactionDate)

# Q38 Insert a new column, Foo = UserID + ProductID
transactions['Foo'] = transactions.UserID + transactions.ProductID

# Q39 Subset rows where TransactionID is even and set Foo = NA
transactions.loc[transactions.TransactionID % 2 == 0, 'Foo'] = np.nan

# Q40 Add 100 to each TransactionID
transactions.TransactionID = transactions.TransactionID + 100
transactions.TransactionID = transactions.TransactionID - 100  # revert to original IDs

# Q41 Insert a column indicating each row number
transactions['RowIdx'] = np.arange(transactions.shape[0])

# Q42 Insert columns indicating the rank of each Quantity, minimum Quantity and maximum Quantity
transactions['QuantityRk'] = transactions.Quantity.rank(method='average')
transactions['QuantityMin'] = transactions.Quantity.min()
transactions['QuantityMax'] = transactions.Quantity.max()

# Q43 Remove column Foo
transactions.drop('Foo', axis=1, inplace=True)

# Q44 Remove multiple columns RowIdx, QuantityRk, and RowIdx
transactions.drop(['QuantityRk', 'QuantityMin', 'QuantityMax'], axis=1, inplace=True)

#======================================================================================================
# Grouping the rows of a DataFrame

#--------------------------------------------------
# Group By + Aggregate

# Q45 Group the transations per user, measuring the number of transactions per user
transactions.groupby('UserID').apply(lambda x: pd.Series(dict(
    Transactions=x.shape[0]
))).reset_index()

# 46 Group the transactions per user, measuring the transactions and average quantity per user
transactions.groupby('UserID').apply(lambda x: pd.Series(dict(
    Transactions=x.shape[0],
    QuantityAvg=x.Quantity.mean()
))).reset_index()



#======================================================================================================
# Joining DataFrames

# Q 47 Load datasets from CSV
users = pd.read_csv('https://raw.githubusercontent.com/ben519/DataWrangling/master/Data/users.csv')
sessions = pd.read_csv('https://raw.githubusercontent.com/ben519/DataWrangling/master/Data/sessions.csv')
products = pd.read_csv('https://raw.githubusercontent.com/ben519/DataWrangling/master/Data/products.csv')
transactions = pd.read_csv('https://raw.githubusercontent.com/ben519/DataWrangling/master/Data/transactions.csv')

# Q48 Convert date columns to Date type
users['Registered'] = pd.to_datetime(users.Registered)
users['Cancelled'] = pd.to_datetime(users.Cancelled)
transactions['TransactionDate'] = pd.to_datetime(transactions.TransactionDate)

#--------------------------------------------------
# Basic Joins

# Q49 Join users to transactions, keeping all rows from transactions and only matching rows from users (left join)
transactions.merge(users, how='left', on='UserID')

# Q50 Which transactions have a UserID not in users? (anti join)
transactions[~transactions['UserID'].isin(users['UserID'])]

# Q51 Join users to transactions, keeping only rows from transactions and users that match via UserID (inner join)
transactions.merge(users, how='inner', on='UserID')

# Q52 Join users to transactions, displaying all matching rows AND all non-matching rows (full outer join)
transactions.merge(users, how='outer', on='UserID')

# Q53 Determine which sessions occured on the same day each user registered
pd.merge(left=users, right=sessions, how='inner', left_on=['UserID', 'Registered'], right_on=['UserID', 'SessionDate'])

# Q54 Build a dataset with every possible (UserID, ProductID) pair (cross join)
df1 = pd.DataFrame({'key': np.repeat(1, users.shape[0]), 'UserID': users.UserID})
df2 = pd.DataFrame({'key': np.repeat(1, products.shape[0]), 'ProductID': products.ProductID})
pd.merge(df1, df2,on='key')[['UserID', 'ProductID']]

# Q55 Determine how much quantity of each product was purchased by each user
df1 = pd.DataFrame({'key': np.repeat(1, users.shape[0]), 'UserID': users.UserID})
df2 = pd.DataFrame({'key': np.repeat(1, products.shape[0]), 'ProductID': products.ProductID})
user_products = pd.merge(df1, df2,on='key')[['UserID', 'ProductID']]
pd.merge(user_products, transactions, how='left', on=['UserID', 'ProductID']).groupby(['UserID', 'ProductID']).apply(lambda x: pd.Series(dict(
    Quantity=x.Quantity.sum()
))).reset_index().fillna(0)

# Q56 For each user, get each possible pair of pair transactions (TransactionID1, TransactionID2)
pd.merge(transactions, transactions, on='UserID')

# Q57 Join each user to his/her first occuring transaction in the transactions table
pd.merge(users, transactions.groupby('UserID').first().reset_index(), how='left', on='UserID')


#======================================================================================================
# Reshaping a data.table

# Q58 Read datasets from CSV
users = pd.read_csv('https://raw.githubusercontent.com/ben519/DataWrangling/master/Data/users.csv')
transactions = pd.read_csv('https://raw.githubusercontent.com/ben519/DataWrangling/master/Data/transactions.csv')

# Q59 Convert date columns to Date type
users['Registered'] = pd.to_datetime(users.Registered)
users['Cancelled'] = pd.to_datetime(users.Cancelled)
transactions['TransactionDate'] = pd.to_datetime(transactions.TransactionDate)

# Q60 Add column TransactionWeekday as Categorical type with categories Sunday through Saturday
transactions['TransactionWeekday'] = pd.Categorical(transactions.TransactionDate.dt.weekday_name, categories=['Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday'])
