import pandas as pd
import numpy as np

# 假设df是一个包含两列的DataFrame，其中一列是行下标，另一列是值
df = pd.read_csv('同诉问题_0.csv')
df = df[['maxvalue', 'maxvalid']]

matrix = np.zeros((len(df), len(df)))  #len(df.columns)
np.fill_diagonal(matrix, 1)

for index, row in df.iterrows():
    # 提取a和b的值
    a = row['maxvalue']
    b = row['maxvalid']
    # 将a的值赋给矩阵的相应位置
    matrix[int(b), index] = a  #matrix

transposed_matrix = matrix.T
result_matrix = matrix + transposed_matrix
np.fill_diagonal(result_matrix, 0)


def get_column_max(matrix):
    max_list = []
    for col in range(len(matrix[0])):
        max_value = max(matrix[:, col])
        max_index = matrix.argmax()
        max_list.append([max_value, max_index])
    return max_list

def get_row_max(matrix):
    max_list = []
    for row in matrix:
        max_value = max(row)
        max_index = np.argmax(row)
        max_list.append([max_value, max_index])
    return max_list


df_result = pd.DataFrame(get_row_max(result_matrix), columns=['maxvalue', 'maxvalid'])
df_result.to_csv('test_result.csv')