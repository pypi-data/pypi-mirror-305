from sqlalchemy import create_engine
from urllib import parse
import pymysql


WLY_117 =  {
     'ip': '192.168.11.117',
     'port': '3306',
     'user': 'emarket_tool',
     'pwd': 'pass@emarket_tool',
     }

WLY_112 = {
     'ip': '192.168.11.112',
     'port': '3306',
     'user': 'emarket_tool',
     'pwd': 'pass@emarket_tool',
     }

ALI_YUN =  {
     'ip': 'rm-7xvo7p6tiy920b97gvo.mysql.rds.aliyuncs.com',
     'port': '3306',
     'user': 'wlygd_admin',
     'pwd': 'Wanliyang@2022',
     }

WLY_101 = {
     'ip': '192.168.11.101',
     'port': '3306',
     'user': 'emarket_tool',
     'pwd': 'pass@emarket_tool',
     }

def wly_101(db:str):
    WLY_101['db'] = db
    db_info = WLY_101
    engine = create_engine(f'mysql+pymysql://{db_info["user"]}:{parse.quote_plus(db_info["pwd"])}@{db_info["ip"]}:3306/{db_info["db"]}')
    return engine

def wly_101_pym(db:str):
    WLY_101['db'] = db
    db_info = WLY_101
    engine = pymysql.connect(
        host=db_info['ip'],
        user=db_info['user'],
        password=db_info['pwd'],
        port=int(db_info['port']),
        database=db_info['db']
    )
    return engine

def aliyun(db:str):
    ALI_YUN['db'] = db
    db_info = ALI_YUN
    engine = create_engine(f'mysql+pymysql://{db_info["user"]}:{parse.quote_plus(db_info["pwd"])}@{db_info["ip"]}:3306/{db_info["db"]}')
    return engine

def aliyun_pym(db:str):
    ALI_YUN['db'] = db
    db_info = ALI_YUN
    engine = pymysql.connect(
        host=db_info['ip'],
        user=db_info['user'],
        password=db_info['pwd'],
        port=int(db_info['port']),
        database=db_info['db']
    )
    return engine

def wly_117(db:str):
    WLY_117['db'] = db
    db_info = WLY_117
    engine = create_engine(f'mysql+pymysql://{db_info["user"]}:{parse.quote_plus(db_info["pwd"])}@{db_info["ip"]}:3306/{db_info["db"]}')
    return engine

def wly_117_pym(db:str):
    WLY_117['db'] = db
    db_info = WLY_117
    engine = pymysql.connect(
        host=db_info['ip'],
        user=db_info['user'],
        password=db_info['pwd'],
        port=int(db_info['port']),
        database=db_info['db']
    )
    return engine

def wly_112(db:str):
    WLY_112['db'] = db
    db_info = WLY_112
    engine = create_engine(f'mysql+pymysql://{db_info["user"]}:{parse.quote_plus(db_info["pwd"])}@{db_info["ip"]}:3306/{db_info["db"]}')
    return engine

def wly_112_pym(db:str):
    WLY_112['db'] = db
    db_info = WLY_112
    engine = pymysql.connect(
        host=db_info['ip'],
        user=db_info['user'],
        password=db_info['pwd'],
        port=int(db_info['port']),
        database=db_info['db']
    )
    return engine
