import pandas as pd
from transformers import BertTokenizer
import tensorflow_hub as hub
import math
import numpy as np

def tokenize_text(text_input):
    return tokenizer.convert_tokens_to_ids(tokenizer.tokenize(text_input))

'''
def mahaton(x,y):    #曼哈顿可能算的不如余弦值效果好
    return sum(map(lambda i, j: abs(i-j), x, y))
'''
def cosine_similarity(list1, list2):
    dot_product = sum([list1[i]*list2[i] for i in range(len(list1))])
    norm1 = math.sqrt(sum([x**2 for x in list1]))
    norm2 = math.sqrt(sum([x**2 for x in list2]))
    similarity = dot_product / (norm1 * norm2)
    return similarity

path = r'C:/Users\HUYIFAN\Desktop\5月\reportdata'
df_raw = pd.read_excel(path + r'\report4-1.xls', sheet_name='Sheet1')

bert_layer = hub.KerasLayer(r"./4", trainable=False)
# bert_layer = hub.KerasLayer("https://hub.tensorflow.google.cn/tensorflow/bert_zh_L-12_H-768_A-12/4",trainable=False)
# bert_layer = hub.KerasLayer("https://tfhub.dev//tensorflow/bert_zh_L-12_H-768_A-12/4",trainable=False)
vocabulary_file = bert_layer.resolved_object.vocab_file.asset_path.numpy()
to_lower_case = bert_layer.resolved_object.do_lower_case.numpy()
tokenizer = BertTokenizer(vocabulary_file, to_lower_case)

# Tokenize all the text, and find the nearest content in the data
text = []
sentences = list(df_raw['工单内容'])
tokenized_text = []
simlst = []
newlst = []
dfvalue = pd.DataFrame(columns=['i', 'maxval', 'idmax'])
dfvalue_insert = pd.DataFrame()   #columns=['i', 'maxval', 'idmax']
for i,tt in enumerate(sentences):  #text
    simlst1 = []    #这里必须在第一个循环中赋空列表，否则会让maxvalid没有参考意义
    tokenized_text.append(tokenize_text(tt))
    if len(tokenized_text[i]) < 300:
        tokenized_text[i] += [0]*(300-len(tokenized_text[i]))
    else:
        tokenized_text[i] = tokenized_text[i][:300]
    for j in list(range(i)):
         value = cosine_similarity(tokenized_text[i], tokenized_text[j])
         simlst1.append(value)
    if i != 0:
        maxvalue = max(simlst1)
        maxvalid = simlst1.index(maxvalue)
#    print(i)
#    print(maxvalue)
#    print(maxvalid) #这里是对于小于i的所有值进行遍历，然后返回最相像的值的index，这个和tokenized_text里面的编码是一致的
        listi = [i, maxvalue, maxvalid]   #第二个元素可以是tokenized_text[i]
        newlst.append(listi)
    print(i)
newlst.insert(0, [0, '第一行工单', 0])
newlst = pd.DataFrame(newlst, columns=["index", "maxvalue", "maxvalid"])
newlst.to_csv('同诉问题_COS_test.csv')