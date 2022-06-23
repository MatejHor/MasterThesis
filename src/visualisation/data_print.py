# import os
# import numpy as np

# name = 'result_2.csv'
# datas = []
# with open(os.path.join('.', name), 'r') as file:
#     for line in file.readlines():
#         datas.append(line.replace('\n', '').split(','))

# data = np.array(datas).T
# with open(os.path.join('.', 'table.csv'), 'w') as file:
#     for line in data:
#         string = ''
#         for word in line:
#             string += word + ','
#         string = string[0:-1]
#         # string += '\\\\\n'
#         string += '\n'
#         # string += '\\hline\n'
#         file.write(string)

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

data = pd.read_csv('table.csv')

print(data.columns)

# legend = True
legend = False

# name = 'Oznacenie'
# plt.figure(figsize=(10,1))
# plt.yticks([0, 1])
# plt.plot(data['Oznacenie'], 'gray', label='Označenie')
# # plt.plot(data[name], 'green', label=name)
# if legend: plt.legend(bbox_to_anchor=(1, 1))
# # plt.show()

name = 'ST inflexné body'
plt.figure(figsize=(10,1))
plt.yticks([0, 1])
# plt.plot(data['Oznacenie'], 'gray', label='Označenie')
plt.fill_between([i for i in range(len(data['Oznacenie']))], data['Oznacenie'], color='gray')
plt.plot(data[name], 'green', label=name)
if legend: plt.legend(bbox_to_anchor=(1, 1))
# plt.show()

name = 'ST prahovanie koherencie'
plt.figure(figsize=(10,1))
plt.yticks([0, 1])
# plt.plot(data['Oznacenie'], 'gray', label='Označenie')
plt.fill_between([i for i in range(len(data['Oznacenie']))], data['Oznacenie'], color='gray')
plt.plot(data[name], 'orange', label=name)
if legend: plt.legend(bbox_to_anchor=(1, 1))
# plt.show()

name = 'ST monotónosť'
plt.figure(figsize=(10,1))
plt.yticks([0, 1])
# plt.plot(data['Oznacenie'], 'gray', label='Označenie')
plt.fill_between([i for i in range(len(data['Oznacenie']))], data['Oznacenie'], color='gray')
plt.plot(data[name], 'r', label=name)
if legend: plt.legend(bbox_to_anchor=(1, 1))
# plt.show()

name = 'ST monotónosť O128'
plt.figure(figsize=(10,1))
plt.yticks([0, 1])
# plt.plot(data['Oznacenie'], 'gray', label='Označenie')
plt.fill_between([i for i in range(len(data['Oznacenie']))], data['Oznacenie'], color='gray')
plt.plot(data[name], 'blue', label=name)
if legend: plt.legend(bbox_to_anchor=(1, 1))
plt.show()
