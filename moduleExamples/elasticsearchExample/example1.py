from elasticsearch import Elasticsearch, RequestsHttpConnection, helpers
import pandas as pd


es = Elasticsearch(
    hosts=["127.0.0.1:9200"],
    connection_class=RequestsHttpConnection
)


datas = []
loop=0
timestamp = None
while loop < 161:
    timestamp = timestamp
    print('timestamp:', timestamp)
    if timestamp == None:
        body = {
            "query": {
                "bool": {
                    "filter": [
                        {
                            "terms": {
                                "organization_industries.keyword": [
                                    "Crypto",
                                    "crypto",
                                    "Crypto Industry",
                                    "crypto industry"
                                ]
                            }
                        }
                    ]
                }
            },
            "sort": [
                {
                    "@timestamp": "desc"
                }
            ],
            "_source": [
                "contact_id",
                "person_name",
                "person_email",
                "type",
                "@timestamp"
            ]
        }
    else:
        body = {
            "query": {
                "bool": {
                    "filter": [
                        {
                            "terms": {
                                 "organization_industries.keyword": [
                                    "Crypto",
                                    "crypto",
                                    "Crypto Industry",
                                    "crypto industry"
                                ]
                            }
                        }
                    ]
                }
            },
            "sort": [
                {
                    "@timestamp": "desc"
                }
            ],
            "search_after":[timestamp],
            "_source": [
                "contact_id",
                "person_name",
                "person_email",
                "type",
                "@timestamp"
            ]
        }
    res = es.search(body=body, size=10000, request_timeout=110)
    data = res['hits']['hits']
    print(data[-1]['_source']['@timestamp'])
    timestamp = data[-1]['_source']['@timestamp']
    loop += 1
    datas.extend(data)

csv_data = [dta['_source'] for dta in datas]


cs = pd.DataFrame(csv_data)

cs.to_csv('data_extractor_crypto_industry_06_10_2021.csv', index=False)