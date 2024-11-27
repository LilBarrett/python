import pandas as pd

df_employees = pd.DataFrame({'First Name': ['Tom', 'Adam', 'Jane', 'Alice', 'Robert', 'Bob', 'John', 'Frank', 'Eva',
                                            'John', 'Lois'],
                   'Last Name': ['Brown', 'Green', 'Thompson', 'Smith', 'Newman', 'Parker', 'Williams', 'Taylor', 'Evans',
                                 'Lewis', 'White'],
                   'Type': ['Full-time Employee', 'Intern', 'Full-time Employee', 'Part-time Employee', 
                            'Full-time Employee', 'Intern', 'Intern', 'Part-time Employee', 'Part-time Employee',
                            'Full-time Employee', 'Part-time Employee'],
                   'Department': ['Administration', 'Technical', 'Administration', 'Technical', 'Management',
                                  'Administration', 'Management', 'Administration', 'Management', 'Technical',
                                  'Management'],
                   'YearsOfExperience': [4, 3, 5, 7, 6, 1, 2, 2, 4, 5, 2],
                   'Salary': [15000, 6000, 9000, 10000, 20000, 3000, 4000, 6000, 12000, 8000, 5500]})

def pretty_pivot(df_employees):
    table = pd.pivot_table(df_employees, 
                           values=['Salary', 'First Name'], index=['Type', 'Department'], 
                           aggfunc={'Salary':["sum", "mean"], 'First Name': "count"})
    table.columns = ['_'.join(col).strip() for col in table.columns.values]

    table = table[['Salary_sum', 'Salary_mean', 'First Name_count']]
    table.columns = ['Sum', 'Mean', 'Number_of_Employees']
    return table

print(pretty_pivot(df_employees))
