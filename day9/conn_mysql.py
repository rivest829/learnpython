# -*- coding:utf-8 -*-
# Author Hsinhan Chiang
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column,Integer,String
from sqlalchemy.orm import sessionmaker
import random

engine=create_engine("mysql+pymysql://root:jiang123@localhost/test",
                                    encoding='utf-8', echo=True)
Base=declarative_base()
class Musician(Base):
    __tablename__='musician'
    id=Column(Integer,primary_key=True)
    name=Column(String(32))
    instrument=Column(String(32))
    age=Column(Integer)
    city = Column(String(32))
    niubility = Column(String(32))
class Band(Base):
    __tablename__='band'
    id = Column(Integer, primary_key=True)
    bandname = Column(String(32))
    style = Column(String(32))
    musician = Column(Integer)
Base.metadata.create_all(engine)

def randomArgs():
    randomArg=[]
    nameRepo=('jiang','jing','wei','shen','mei','hao','zhang','du','yang','wang','huang','wu','dang','gong','lang','tian','piao')
    instrumentRepo=('guitar','bass','piano','drum','voice','violin')
    cityRepo=('Xi\'an','Beijing','Xiamen','Fuzhou','Chengdu','Chongqing','Shenzhen'
          ,'Guangzhou','Shanghai','Shijiazhuang','Lanzhou','Xining','Lijiang','Dali','Kunming','Nanjing','Nanning')
    niubilityRepo=('rubbish','just_soso','normal','good','excellent','godlike')
    name=nameRepo[random.randrange(0,16)]+nameRepo[random.randrange(0,16)]+nameRepo[random.randrange(0,16)]
    instrument=instrumentRepo[random.randrange(0,5)]
    city=cityRepo[random.randrange(0,16)]
    niubility=niubilityRepo[random.randrange(0,5)]
    randomArg.append(name)
    randomArg.append(instrument)
    randomArg.append(random.randrange(20, 50))
    randomArg.append(city)
    randomArg.append(niubility)
    return randomArg

def randomBands():
    randomArg=[]
    bandnameRepo=('ing','sh','es','ar','er','bu','ti','li','ty','se','nu','is','as','su','bi','ci','ac')
    styleRepo=('hard_rock','post_rock','pop','death_metal','black_metal','classic')
    name=bandnameRepo[random.randrange(0,16)]+bandnameRepo[random.randrange(0,16)]+bandnameRepo[random.randrange(0,16)]+bandnameRepo[random.randrange(0,16)]
    style=styleRepo[random.randrange(0,5)]
    randomArg.append(name)
    randomArg.append(style)
    randomArg.append(random.randrange(1, 100000))
    return randomArg

def addRandomMusician():
    musicianArgs=randomArgs()
    musician=Musician(name=musicianArgs[0].encode(encoding='utf-8')
                      ,instrument=musicianArgs[1].encode(encoding='utf-8')
                      ,age=musicianArgs[2]
                      ,city=musicianArgs[3]
                      ,niubility=musicianArgs[4])
    session.add(musician)

def addRandomBand():
    bandArgs=randomBands()
    band=Band(bandname=bandArgs[0].encode(encoding='utf-8')
                      ,style=bandArgs[1].encode(encoding='utf-8')
                      ,musician=bandArgs[2])
    session.add(band)

session_class=sessionmaker(bind=engine)
session=session_class()

for i in range(100000):
    addRandomBand()

session.commit()

