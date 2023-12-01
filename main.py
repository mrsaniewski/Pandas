# Python Pandas

import pandas as pd


# Pandas Series, is one of the two basic data types in Pandas. This is a type that represents one
# column.


def pd_series():
    a = pd.Series([-1, 1, 3, 5, 7])

    print("Original Series:")
    print(a)

    print("\nMultiplied Series:")
    print(a * 10)

    print("\nAbsolute Values:")
    print(a.abs())

    print("\nDescriptive Statistics:")
    print(a.describe())

    a.index = ['Pierwsza', 'Druga', 'Trzecia', 'Czwarta', 'Piąta']

    print("\nNew indexes:")
    print(a)

    print("\nShow:")
    print(a['Piąta'])


# Pandas DataFrame
# The second basic data type in Pandas, after Pandas Series, is DataFrame. This is a multi-column type that we can
# compare to a more efficient table in Excel.


def pd_dataframe():
    # Creating a DataFrame ############################################################

        # Based on a list
    a = [['Ania', 24], ['Michal', 9], ['Darek', 40], ['Ewa', 43]]
    df_a = pd.DataFrame(a)
    df_a.columns = 'Imię', 'Wiek'
    print(df_a)

        # Based on a dictionary
    b = {'Imię': ['Ewa', 'Michał', 'Krzysiek', 'Kasia', 'Lucja'],
         'Miasto': ['Warszawa', 'Kraków', 'Gdańsk', 'Poznań', 'Łódź']}
    df_b = pd.DataFrame(b)
    print(df_b)

         # File loading
    df = pd.read_csv('http://analityk.edu.pl/wp-content/uploads/2020/01/Countries.csv')
    print(df)

    # Browsing DataFrame ############################################################
    print("First 3 lines:")
    print(df[:3])

    print("\nSpecific columns:")
    print(df[['Country', 'Region']])

    print("\nFirst 3 rows and first 3 columns:")
    print(df.iloc[0:3, 0:3])

    print("\nFirst 3 rows, first 3 columns and specific columns:")
    print(df.loc[:3, ['Country', 'Region', 'Population']])

    # Basic operations ############################################################

        #Copy
    df_pop = df[['Country', 'Region', 'Population', 'Phones per 1000']].copy()
    print(df_pop)

        #Divide
    df_pop['Population'] /= 1000000
    print(df_pop)

        #New column
    df_pop['Nowa kolumna'] = 1
    print(df_pop)

        #Show first 5 lines
    df_pop.head()
    print(df_pop)


# Iterations for loop ############################################################
    for index, row in df_pop.iterrows():
        if row['Population'] > 100:
            df_pop.loc[index, 'Size'] = 'Big'
            print (row['Country'], df_pop.loc[index, 'Size'])

# Itertuples function ############################################################
    for row in df_pop.itertuples():
        if row.Population > 200:
            print(row.Index, row.Country, row.Population)

# DataFrame Filtering ############################################################
    df_pop.Population == 147.365352

    df_pop[df_pop.Population == 147.365352]
   ### OR ###### df_pop[df_pop['Population'] == 147.365352]

    print(df_pop[(df_pop['Population']>100) & (df_pop['Population']<150)])

        #Summation, Grouping, and other calculations

    print( df_pop['Population'].sum() )
    print( df_pop['Population'].max() )
    print( df_pop['Population'].min() )
    print( df_pop['Population'].mean() )

    print( df_pop.groupby('Region')['Population'].size() )
    print( df_pop.groupby('Region')['Population'].sum() )
    print( df_pop.groupby('Region')['Population'].min() )
    print( df_pop.groupby('Region')['Population'].max() )
    print( df_pop.groupby('Region')['Population'].mean() )

    print(df_pop.groupby('Region')['Population'].agg([min, max, sum]))

        # Save the results in columns with specific names
    print(df_pop.groupby('Region', as_index=False)['Population'].agg({"Suma": "sum", "Max": "max"}))


# DataFrame Linking - SQL Join ######################################
def pd_dfjoin():

    a = [['Ania', 24], ['Michał', 9], ['Darek', 40], ['Ewa', 43]]
    df_a = pd.DataFrame(a)
    df_a.columns = 'Imię', 'Wiek'
    b = {'Imię': ['Ewa', 'Michał', 'Krzysiek', 'Kasia', 'Lucja'],
         'Miasto': ['Warszawa', 'Kraków', 'Gdańsk', 'Poznań', 'Łódź']}
    df_b = pd.DataFrame(b)

    print(df_a)
    print(df_b)

    # Part of the common
    pd.merge(df_a, df_b, on='Imię')
    # All rows from the left set, matching rows from the right set
    pd.merge(df_a, df_b, on='Imię', how='left')

    # All rows from the right set, matching rows from the left set
    pd.merge(df_a, df_b, on='Imię', how='right')

    # All rows
    print (pd.merge(df_a, df_b, on='Imię', how='outer'))


# Charts - Matplotlib ########################################
import matplotlib.pyplot as plt


df = pd.read_csv('http://analityk.edu.pl/wp-content/uploads/2020/01/Countries.csv')
df_pop = df[['Country', 'Region', 'Population', 'Phones per 1000']].copy()
df_pop.groupby('Region')['Population'].sum().plot(kind='pie')
plt.show()

if __name__ == '__main__':
    # pd_series()
    # pd_dataframe()
    pd_dfjoin()
