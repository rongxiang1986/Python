import pickle

# 序列化
dict_data = {"k1": "v1", "k2": 123}
dumps = pickle.dumps(dict_data)
print(dumps)

# 序列化并写文件
with open('data.pickle', 'wb') as f:
    pickle.dump(dict_data, f)
