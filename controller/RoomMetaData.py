import sys
sys.path.append(r'C:/Users/bp/Documents/investing_subscribe/DAO')
import DAO


def roomMetaData(roomNo):
    superchat_df = DAO.select_superchat()
    superchat_df['returnRate'] = round((superchat_df['predictPrice'] / superchat_df['currentPrice'] - 1) * 100, 1)

    if roomNo in superchat_df['roomNo'].unique():
        room_df = superchat_df.loc[superchat_df['roomNo'] == roomNo]
        highReturn = room_df.loc[room_df['point'] == 1].sort_values(by='returnRate', ascending=False).head(3)
        hitRate = len(room_df.loc[room_df['point'] == 1]) / len(room_df)
        print("HightReturn: \n", highReturn[['stockName', 'returnRate']].to_string(index=False))
        print("Hit Rate: ", hitRate)