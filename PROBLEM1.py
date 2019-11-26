import pandas as pd

data1 = {'Student': ['Ice Bear', 'Panda', 'Grizzly'], 'Math': [80, 95, 79]}
math = pd.DataFrame(data1, columns = ['Student', 'Math'])

data2 = {'Student': ['Ice Bear', 'Panda', 'Grizzly'], 'Electronics': [85, 81, 83]}
Electronics = pd.DataFrame(data2, columns = ['Student', 'Electronics'])

data3 = {'Student': ['Ice Bear', 'Panda', 'Grizzly'], 'GEAS': [90, 79, 93]}
GEAS = pd.DataFrame(data3, columns = ['Student', 'GEAS'])

data4 = {'Student': ['Ice Bear', 'Panda', 'Grizzly'], 'ESAT': [93, 89, 88]}
ESAT = pd.DataFrame(data4, columns = ['Student', 'ESAT'])

merge = pd.merge(math, Electronics, how = 'right', on = 'Student')
merge1 = pd.merge(merge, GEAS, how = 'right', on = 'Student')
merge2 = pd.merge(merge1, ESAT, how = 'right', on = 'Student')

print(merge2)