import sys
sys.path.append(r'C:/Users/bp/Documents/GitHub/investing_subscribe/DAO')
import DAO

def userRoom(userName):
    inRoomInfo = DAO.user_room(userName)
    inRoomInfo = inRoomInfo.loc[inRoomInfo['nickname']==userName][['roomNo', 'title', 'fee', 'rankingPoint']].to_html(index=False)
    return inRoomInfo
