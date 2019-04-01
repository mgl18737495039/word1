from orm import model as mo

from sqlalchemy import *
engine = create_engine("mysql+mysqlconnector://root:123456@localhost/flaskdb",
                                    encoding='utf8', echo=True)
from sqlalchemy.orm import sessionmaker
session=sessionmaker()()

def insertUser (username,password,email):
    result=session.add(mo.User(username=username,password=password,email=email))
    session.commit()
    session.close()
def checkUser(username,pwd):
    result=session.query(mo.User).filter(mo.User.username ==username).filter(mo.User.password==pwd).first()

    return result
def checkUserId(cid):
    result = session.query(mo.User.username).filter(mo.User.id == cid).all()

    return result


def checkUserText(id):

    result=session.query(mo.Userxiangmu.textname).filter(mo.Userxiangmu.userid==id).all()
    if len(result)>0:
        return result
    else:
        pass

def checkUserAllText():

    result=session.query(mo.Userxiangmu.textname).all()
    if len(result)>0:
        return result
    else:
        pass

def checkText(name):
    result=session.query(mo.Userxiangmu.text).filter(mo.Userxiangmu.textname==name).first()
    return result
def inserttext(textname,text,mid):
    result=session.add(mo.Userxiangmu(userid=mid,text=text,textname=textname))
    session.commit()
    session.close()
def dele(nametext):
    t4=session.query(mo.Userxiangmu).filter(mo.Userxiangmu.textname==nametext).delete()
    session.commit()

def checkTextU(name):
    result=session.query(mo.Userxiangmu).filter(mo.Userxiangmu.textname==name).first()
    return result
def updataTxet(name,text1,rname):
    try:
        t5=session.query(mo.Userxiangmu).filter(mo.Userxiangmu.textname==rname).first()
        t5.textname=name
        t5.text=text1
        session.commit()
    except Exception as e:
        return e