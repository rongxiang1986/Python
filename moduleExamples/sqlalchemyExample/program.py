from sqlalchemy.orm import sessionmaker
from session import SessionHandler
from models import Test
from db import DB
import dbConfig

db = DB(dbConfig.mysql_db).connect()
engine = db.engine
Session = sessionmaker(bind=engine)
session = Session()

# 写入数据
try:
    user_session = SessionHandler.create(session, Test)
    data_list = []
    for i in range(10001):
        data_list.append({
      "first_name": "tom{}".format(i),
      "last_name": "test",
      "id_card_no": "1000",
      "email": "test{}@test.com".format(i)
    })
    print(len(data_list))
    user_session.add(data_list)

    session.commit()
except Exception as e:
    session.rollback()
    raise e
finally:
    session.close()


# update and insert
# try:
#     user_session = SessionHandler.create(session, Test)
#     # user_session.delete({'first_name': 'tom'})
#     # 查询语句
#
#     data = {'id': 1, 'first_name': 'tom1', 'last_name': 'test', 'id_card_no': 1000, 'email': 'test1@test.com'}
#     record_dict = {'first_name': 'tom2', 'last_name': 'test', 'id_card_no': 1000, 'email': 'test2@test.com'}
#     # user_session.upsert(data, record_dict)
#     user_session.update(record_dict, data)
#
#     session.commit()
# except Exception as e:
#     print(e)
# finally:
#     session.close()

# 查询数据
# try:
#     user_session = SessionHandler.create(session, Test)
#     # 查询语句
#     query_dict = {'last_name': 'test'}
#     result = user_session.get(query_dict)
#     print(user_session.count({}))
#     # result = user_session.get_all(query_dict, to_json=to_json)
#     print(result)
#
# except Exception as e:
#     print(e)
# finally:
#     session.close()