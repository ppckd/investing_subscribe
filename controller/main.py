import sys
sys.path.append(r'C:/Users/bp/Documents/investing_subscribe/DAO')
import DAO
import RoomMetaData

import datetime
import logging
import os

from flask import Flask




room_ranking = DAO.view_room_ranking().to_html(index=False)
app = Flask(__name__, static_url_path='/static')

@app.route('/ranking')
def ranking():

    return f'<h1>리딩방 랭킹</h1>{room_ranking}'

@app.route('/user/<user_name>')
def user(user_name):
    inRoomInfo = DAO.user_room(user_name)
    inRoomInfo = inRoomInfo.loc[inRoomInfo['nickname']==user_name][['roomNo', 'title', 'fee', 'rankingPoint']].to_html(index=False)
    return f'<h1>Hello, {user_name}</h1> 참여방 목록: {inRoomInfo}'

@app.route('/user/<user_name>/<int:room_no>')
def superchat_room(user_name, room_no):
    superChat = DAO.select_superchat()
    superChat = superChat.loc[superChat['roomNo'] == room_no]
    roomTitle = superChat['title'].unique()[0]
    superChat = superChat[['stockName', 'currentPrice', 'predictPrice', 'stopLossPrice', 'today', 'predictDate', 'contents', 'point']]
    return f'<h1>Hello, {user_name} </h1><h2> [{room_no}]{roomTitle}방 리딩정보:</h2> {superChat.to_html(index=False)}'


if __name__ == '__main__':
    # threaded=True 로 넘기면 multiple plot이 가능해짐
  app.run(host="127.0.0.1", port=8080, debug=True)


'''
접속하면은

방 순위 보여주기

방을 선택하면은 메타데이터 보여주기

1. 슈퍼챗 들어가기
1-1 방장은 슈퍼챗 입력
1-1.1 슈퍼챗 뿌려주기

2. 일반채팅 하기
'''

# try:
#     print("DB 접속 중")
#     dbConnect = DAO.dbconnect()
# except:
#     print("DB접속 에러")




from threading import Thread

# 순위 공개
# room_ranking = DAO.view_room_ranking()
# print(room_ranking)
#
# while True:
#     print("""
#     =====menu======
#     1. 메타데이터 확인
#     2. 슈퍼챗(공지방) 입장
#     3. 채팅방 입장
#     ===============
#     """)
#     # 메타데이터
#     menuNum = input("메뉴를 선택하세요 :")
#
#     if menuNum == "1":
#         while True:
#             try:
#                 roomNum = int(input("보고 싶은 슈퍼챗 방번호를 입력하세요"))
#                 RoomMetaData.roomMetaData(roomNum)
#                 break
#             except:
#                 print("다시 숫자를 입력하세요")
#
#     elif menuNum == "2":
#         userName = input("사용자 ID를 입력하세요")
#         inRoomNo = DAO.user_room(userName)
#         print("입장할 방을 선택하세요", inRoomNo)
#         roomNum = int(input(":"))
#         superChat = DAO.select_superchat()
#
#
#     else:
#         break
#
#
