
import os
import logging
import sqlalchemy
from sqlalchemy.engine.url import URL
import dbConfig


logger = logging.getLogger()
logger.setLevel(logging.INFO)


class DB(object):

    def __init__(self, config):

        self.engine = sqlalchemy.create_engine(URL.create(**config),
                                               pool_pre_ping=True,
                                               pool_size=10,
                                               max_overflow=0,
                                               pool_recycle=36000,
                                               pool_timeout=60)

    def connect(self):
        return self.engine.connect()


if __name__ == '__main__':
    db = DB(dbConfig.mysql_db)
    print(db.connect())
