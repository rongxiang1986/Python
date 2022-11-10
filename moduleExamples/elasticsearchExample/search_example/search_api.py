from elasticsearch import Elasticsearch

elasticClient = Elasticsearch('http://192.168.31.3:9200')

query_body = {
    "track_total_hits": 10,
    "query": {
        "bool": {
            "must": {
                "match": {
                    "text_entry": "we"
                }
            }
        }
    },
    "from": 0,
    "size": 10,
    "sort": [{"_id": {"order": "desc"}}]
}

result = elasticClient.search(index="shakespeare", body=query_body)
print(result)
