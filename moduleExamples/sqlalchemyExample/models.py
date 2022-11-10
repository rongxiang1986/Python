from dataclasses import dataclass
from sqlalchemy import Column, Integer, String, DateTime, UniqueConstraint, func
from sqlalchemy.ext.declarative import declarative_base
from db import DB
import dbConfig

db = DB(dbConfig.mysql_db).connect()
engine = db.engine
Base = declarative_base()


@dataclass
class Test(Base):
    __tablename__ = 'test'
    # 唯一约束 UniqueConstraint
    __table_args__ = (UniqueConstraint('email', 'id_card_no'),)

    id = Column(Integer, primary_key=True)
    first_name: str = Column(String(200))
    last_name: str = Column(String(200))
    id_card_no: str = Column(String(200))
    email: str = Column(String(200))
    created_time = Column(DateTime(timezone=True), default=func.now())
    updated_time = Column(DateTime(timezone=True), default=func.now(), onupdate=func.now())


Base.metadata.create_all(engine)
