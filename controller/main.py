import sys
sys.path.append(r'C:/Users/bp/Documents/GitHub/investing_subscribe/DAO')
sys.path.append(r'C:/Users/bp/Documents/GitHub/investing_subscribe/templates')
import DAO
import RoomMetaData, SuperChatRoom, SuperChatInput, UserRoom
import SuperChatInputHtml
from flask import Flask, render_template, request

'''
기본기능
1. 리딩방 순위 보여주기(구현완료)
2. 방을 선택하면 메타데이터 보여주기(구현완료)
3. 슈퍼챗
    3-1. 슈퍼챗 입력하기(구현완료)
    3-2. 슈퍼챗 보기(구현완료)
    3-3. 슈퍼챗 구독하기(Enter)(구현미완료)
4. 일반채팅 하기(구현미완료)

추가기능
1. DB접속 확인하기
2. 로그 찍기
3. 접근 권한 설정하기
4. 입력 간소화 및 검증
'''

try:
    print("DB 접속 중")
    dbConnect = DAO.dbconnect()
except:
    print("DB접속 에러")

app = Flask(__name__, static_url_path='/static')

@app.route('/')
@app.route('/ranking')
def ranking():
    room_ranking = DAO.view_room_ranking().to_html(index=False)
    return f'<h1>만나서 반갑습니다.</h1> <h2> 리딩방 랭킹입니다 </h2> {room_ranking}'

@app.route('/ranking/<int:room_no>')
def room_meta_data(room_no):
    high_return, hit_Rate, room_title = RoomMetaData.roomMetaData(room_no)
    return f'<h1>{room_title}방의 메타데이터 </h1> <h2> 수익률 top3 </h2>{high_return} <h2>적중률: {hit_Rate}</h2>'

@app.route('/user/<user_name>')
def user(user_name):
    inRoomInfo = UserRoom.userRoom(user_name)
    return f'<h1>Hello, {user_name}</h1> 참여방 목록: {inRoomInfo}'

@app.route('/superChatInput',  methods=['GET', 'POST'])
def iunput_user():
    htmlcode = SuperChatInputHtml.superChatInputHtml()
    if request.method == 'POST':
        temp_list = []
        temp_list.append(request.form.get("roomNo"))
        temp_list.append(request.form.get("userID"))
        temp_list.append(request.form.get("stockName"))
        temp_list.append(request.form.get("stockCode"))
        temp_list.append(request.form.get("currentPrice"))
        temp_list.append(request.form.get("predictPrice"))
        temp_list.append(request.form.get("stopLossPrice"))
        temp_list.append(request.form.get("today"))
        temp_list.append(request.form.get("predictDate"))
        temp_list.append(request.form.get("contents"))
        SuperChatInput.superChatInput(temp_list)
    return htmlcode

@app.route('/user/<user_name>/<int:room_no>')
def super_chat_room(user_name, room_no):
    super_chat, room_title = SuperChatRoom.superChatRoom(room_no)
    return f'<h1>Hello, {user_name} </h1><h2> [{room_no}]{room_title}방 리딩정보:</h2> {super_chat}'


if __name__ == '__main__':
  app.run(host="127.0.0.1", port=8080, debug=True, threaded=True)


