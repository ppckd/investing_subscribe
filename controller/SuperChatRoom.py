import sys
sys.path.append(r'C:/Users/bp/Documents/GitHub/investing_subscribe/DAO')
import DAO

def superChatRoom(roomNo):
    superChat = DAO.select_superchat()
    superChat = superChat.loc[superChat['roomNo'] == roomNo]
    roomTitle = superChat['title'].unique()[0]
    superChat = superChat[['stockName', 'currentPrice', 'predictPrice', 'stopLossPrice', 'today', 'predictDate', 'contents', 'point']].to_html(index=False)
    return superChat, roomTitle