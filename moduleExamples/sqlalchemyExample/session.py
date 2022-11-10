import json
import datetime
import time
import pandas as pd
from sqlalchemy.dialects.mysql import insert
from sqlalchemy import UniqueConstraint
from db import DB


class SessionHandler(object):
    __instance = None

    def __init__(self, session, model):
        """ Virtually private constructor. """

        SessionHandler.__instance = self
        self.model = model
        self.session = session

    @staticmethod
    def create(session, model):
        SessionHandler.__instance = SessionHandler(session, model)
        return SessionHandler.__instance

    def add(self, record_list):
        return self.session.add_all([self.model(**record_dict) for record_dict in record_list])

    def update(self, query_dict, update_dict):
        return self.session.query(self.model).filter_by(**query_dict).update(update_dict)

    def upsert(self, data, record_dict):
        # statement = insert(self.model).values(id=0, first_name='tom', last_name='test', id_card_no=1000, email='test@test.com')
        # do_update_statement = statement.on_duplicate_key_update(
        #     first_name='tom10', last_name='test', id_card_no=1000, email='test10@test.com')
        statement = insert(self.model).values(**data)
        do_update_statement = statement.on_duplicate_key_update(**record_dict)

        return self.session.execute(do_update_statement)

    def count(self, query_dict):
        return self.session.query(self.model).filter_by(**query_dict).count()

    def get(self, query_dict):
        results = self.session.query(self.model).filter_by(**query_dict).all()
        # print(results)
        return pd.DataFrame(results)

    def delete(self, query_dict):
        return self.session.query(self.model).filter_by(**query_dict).delete()

