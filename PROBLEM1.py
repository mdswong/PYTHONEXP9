import pandas as pd

data1 = {'Student': ['Ice Bear', 'Panda', 'Grizzly'], 'Math': [80, 95, 79]}
math = pd.DataFrame(data1, columns = ['Student', 'Math'])

data2 = {'Student': ['Ice Bear', 'Panda', 'Grizzly'], 'Electronics': [85, 81, 83]}
Electronics = pd.DataFrame(data2, columns = ['Student', 'Electronics'])

data3 = {'Student': ['Ice Bear', 'Panda', 'Grizzly'], 'GEAS': [90, 79, 93]}
GEAS = pd.DataFrame(data3, columns = ['Student', 'GEAS'])

data4 = {'Student': ['Ice Bear', 'Panda', 'Grizzly'], 'ESAT': [93, 89, 88]}
ESAT = pd.DataFrame(data4, columns = ['Student', 'ESAT'])

merge_wide = pd.merge(math, Electronics, how = 'right', on = 'Student')
merge_wide1 = pd.merge(merge_wide, GEAS, how = 'right', on = 'Student')
merge_wide2 = pd.merge(merge_wide1, ESAT, how = 'right', on = 'Student')

merge_long = pd.melt(merge_wide2, id_vars = 'Student', value_vars = ['Math', 'Electronics', 'GEAS', 'ESAT'])
merge_long1 = merge_long.rename(columns = {'variable': 'Subjects', 'value': 'Grades'})
merge_long2 = merge_long1.sort_values('Student').reset_index().drop(columns = 'index')

print('\n')
print('Wide Format:')
print('\n')
print(merge_wide2)
print('\n')
print('Long Format:')
print('\n')
print(merge_long2)
