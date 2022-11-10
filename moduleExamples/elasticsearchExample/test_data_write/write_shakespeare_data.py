from elasticsearch import Elasticsearch
from elasticsearch import helpers
import json

es_client = Elasticsearch(["192.168.31.3:9200"])

# 第一步 创建索引

create_index_body = {
    "settings": {
        "number_of_shards": 1,
        "number_of_replicas": 0},
    'mappings': {
        "_doc": {
            "properties": {
                "speaker": {"type": "keyword"},
                "play_name": {"type": "keyword"},
                "line_id": {"type": "integer"},
                "speech_number": {"type": "integer"}}}}
}

if not es_client.indices.exists(index="shakespeare"):
    print("索引不存在，创建索引。索引名为：{}".format("shakespeare"))
    es_client.indices.create(index="shakespeare", body=create_index_body)
else:
    print("索引已存在。索引名为：{}".format("shakespeare"))


# 第二步 读取数据并写入

test_data_file_name = "shakespeare.json"
with open(test_data_file_name) as f:
    data_list = f.readlines()

"""
数据案例
{"index":{"_index":"shakespeare","_id":0}}
{"type":"act","line_id":1,"play_name":"Henry IV", "speech_number":"","line_number":"","speaker":"","text_entry":"ACT I"}
"""

i = 0
actions = []
while i < len(data_list):
    meta_data = json.loads(data_list[i])
    real_data = json.loads(data_list[i + 1])

    action = {
        "_index": meta_data["index"]["_index"],
        "_id": meta_data["index"]["_id"],
        "_type": "_doc",
        "_source": real_data
    }
    actions.append(action)
    i = i + 2

# 批量写入
print("写入文档数量：", len(actions))
helpers.bulk(es_client, actions)


# 第三步 验证

print("查询index信息：", es_client.count(index="shakespeare"))

