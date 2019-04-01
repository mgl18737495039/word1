# class xiangmu():
#     def __init__(self,id,name,email):
#         self.id=id
#         self.name=name
#         self.email=email
#     def __str__(self):
#         return "id:%s name:%s price:%s"%(self.id,self.name,self.email)

from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import  *
engine = create_engine("mysql+mysqlconnector://root:123456@localhost/flaskdb",
                       encoding='utf8', echo=True)
Base=declarative_base(bind=engine)
class User (Base):
    __tablename__="user"
    id=Column(Integer,primary_key=True,autoincrement=True,nullable=False )
    username=Column(String(20),nullable=False)
    password=Column(String(50),nullable=False)
    email=Column(String(50),nullable=False)
class Userxiangmu(Base):
    __tablename__="xiangmu"
    id=Column(Integer,primary_key=True,autoincrement=True,nullable=False )
    textname=Column(String(50),nullable=False)
    text=Column(TEXT(10000),nullable=False)
    userid=Column(Integer,ForeignKey('user.id'),nullable=True)
if __name__ == "__main__":
    # 创建表  必须卸载main模块
    Base.metadata.create_all(bind=engine)