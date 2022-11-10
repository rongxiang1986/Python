import elasticsearch
import pickle

# es = elasticsearch.Elasticsearch()
# pickle.dumps(es)

# TypeError: cannot pickle '_thread.lock' object


def fun1():
    try:
        a=1
        return a
    except Exception as e:
        print(e)
    finally:
        print("finally")

b = fun1()
print(b)