import pandas as pd
import numpy as np

# 假设df是一个包含两列的DataFrame，其中一列是行下标，另一列是值
df = pd.read_csv('同诉问题_0_mahaton.csv')
df = df[['minvalue', 'minvalid']]

matrix_mahaton = np.ones((len(df), len(df)))

for index, row in df.iterrows():
    # 提取a和b的值
    a = row['minvalue']
    b = row['minvalid']
    # 将a的值赋给矩阵的相应位置
    matrix_mahaton[int(b), index] = a


trasposed_matrix_mahaton = matrix_mahaton.T
result_matrix = matrix_mahaton + trasposed_matrix_mahaton



def get_column_min(matrix):
    min_list = []
    for col in range(len(matrix[0])):
        col_values = [row[col] for row in matrix if row[col] != 2]
        min_value = min(col_values)
        min_index = matrix[col_values.index(min_value)]
        min_list.append([min_value, min_index])
    return min_list

def get_row_min(matrix):
    min_list = []
    for row in matrix:
        row_values = [val for val in row if val != 2]
        if row_values:
            min_value = min(row_values)
            min_index = row_values.index(min_value)
            min_list.append([min_value, min_index])
    return min_list


df_result = pd.DataFrame(get_row_min(result_matrix), columns=['minvalue', 'minvalid'])
df_result.to_csv('test_result.csv')