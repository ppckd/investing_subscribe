import pymysql
import pandas as pd
import requests

#DB접속, 크롤링, 데이터프레임 가공 작업

def db_connect():
    ic_db = pymysql.connect(
        user='invest_admin',
        passwd='abc123',
        host='127.0.0.1',
        db='ic_db',
        charset='utf8'
    )
    return ic_db

def select_superchat():
    ic_db = db_connect()
    cursor = ic_db.cursor(pymysql.cursors.DictCursor)
    sql = """SELECT superchat.*, room.title
        FROM superchat
        join room
        ON superchat.roomNo = room.roomNo;"""
    cursor.execute(sql)

    superchat = cursor.fetchall()
    superchat = pd.DataFrame(superchat)
    superchat['today'] = pd.to_datetime(superchat['today'].astype(str), format='%Y/%m/%d')
    superchat['predictDate'] = pd.to_datetime(superchat['predictDate'].astype(str), format='%Y/%m/%d')

    return superchat

def insert_super_chat(roomNo, userID, stockName, stockCode, currentPrice, predictPrice, stopLossPrice, today,
                       predictDate, contents):
    ic_db = db_connect()
    cursor = ic_db.cursor(pymysql.cursors.DictCursor)
    sql = """INSERT INTO superchat(roomNo, userID, stockName, stockCode, currentPrice, predictPrice, stopLossPrice, today, predictDate, contents, createdTime)
            VALUES('{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}', NOW())
            """.format(roomNo, userID, stockName, stockCode, currentPrice,
                       predictPrice, stopLossPrice, today,
                       predictDate, contents)
    cursor.execute(sql)
    ic_db.commit()


def acture_price(stock_code):
    url = 'https://finance.naver.com/item/sise_day.nhn?code={}'.format(stock_code)

    # 해당 사이트는 반드시 헤더 정보를 요구하기 때문에 헤더를 넘겨줘야 함
    headers = {
        'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.103 Safari/537.36'}
    req = requests.get(url, headers=headers)

    # 모든 페이지 정보 데이터 프레임 생성
    acture_price = None
    for page in range(1, 10):  # 10주치만 긁기
        req = requests.get(f'{url}&page={page}', headers=headers)
        acture_price = pd.concat([acture_price, pd.read_html(req.text, encoding='euc-kr')[0]], ignore_index=True)

    # 데이터가 없는 행 삭제 및 재배열
    acture_price.dropna(inplace=True)
    acture_price.reset_index(drop=True, inplace=True)
    acture_price = acture_price[['날짜', '종가']]
    acture_price['날짜'] = pd.to_datetime(acture_price['날짜'].astype(str), format='%Y.%m.%d')

    return acture_price

def update_ranking_point(chatNo):
    ic_db = db_connect()
    cursor = ic_db.cursor(pymysql.cursors.DictCursor)
    sql = """UPDATE superchat
            SET point = 1
            WHERE chatNo = {};""".format(chatNo)
    cursor.execute(sql)
    ic_db.commit()

def update_ranking_sum_point(sumPoint, roomNo):
    ic_db = db_connect()
    cursor = ic_db.cursor(pymysql.cursors.DictCursor)
    sql = """UPDATE room
        SET rankingPoint = {}
        WHERE roomNo = {};""".format(sumPoint, roomNo)
    cursor.execute(sql)
    ic_db.commit()

def view_room_ranking():
    ic_db = db_connect()
    cursor = ic_db.cursor(pymysql.cursors.DictCursor)
    sql = """SELECT *
        FROM room
        ORDER BY rankingPoint DESC;"""
    cursor.execute(sql)
    room_ranking = cursor.fetchall()
    room_ranking = pd.DataFrame(room_ranking)
    room_ranking = room_ranking[['roomNo', 'title', 'fee', 'rankingPoint']]

    return room_ranking

def user_room(nickName):
    ic_db = db_connect()
    cursor = ic_db.cursor(pymysql.cursors.DictCursor)
    sql = """SELECT room.roomNo, room.title, room.fee, room.rankingPoint, member.userNo, member.nickname
        FROM room
        JOIN member
        ON room.roomNo = member.roomNo
        ORDER BY room.roomNo;""".format(nickName)
    cursor.execute(sql)
    inRoomInfo = pd.DataFrame(cursor.fetchall())
    return inRoomInfo
