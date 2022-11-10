import pickle

# 序列化
dict_data = {"name": "Tom", "age": 20}
dumps = pickle.dumps(dict_data)
print(dumps)

# 反序列化
dict_data_unpickling = pickle.loads(dumps)
print(type(dict_data_unpickling))
print(dict_data_unpickling)

"""
<class 'dict'>
{'name': 'Tom', 'age': 20}
"""


# 序列化并写文件
with open('data.pickle', 'wb') as f:
    pickle.dump(dict_data, f)

# 读文件字节流并反序列化
with open('data.pickle', 'rb') as f:
    dict_data_unpickling = pickle.load(f)
    print(type(dict_data_unpickling))
    print(dict_data_unpickling)

"""
<class 'dict'>
{'name': 'Tom', 'age': 20}
"""
