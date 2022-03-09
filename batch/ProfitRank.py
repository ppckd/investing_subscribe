import schedule
import time
import sys
sys.path.append(r'C:/Users/bp/Documents/investing_subscribe/DAO')
import DAO


def rankCal():
    superchat = DAO.select_superchat()
    print(superchat)
    for i in superchat['roomNo'].unique():
        temp_pre_df = superchat[superchat['roomNo'] == i]

        for index, item_row in temp_pre_df.iterrows():

            code = item_row['stockCode']
            #날짜 가공
            acture_price = DAO.acture_price(code)
            acture_price = acture_price[acture_price['날짜'] <= item_row['predictDate']]
            acture_price = acture_price[acture_price['날짜'] > item_row['today']]

            # 점수 매기기
            for index, acture_row in acture_price.iterrows():
                if acture_row['종가'] >= item_row['predictPrice']:
                    DAO.update_ranking_point(item_row['chatNo'])

                    break
            # 랭킹 점수 업데이트

    for roomNo in superchat['roomNo'].unique():
        temp_pre_df = superchat[superchat['roomNo'] == roomNo]
        sum_point = temp_pre_df['point'].sum()
        DAO.update_ranking_sum_point(sum_point, roomNo)



schedule.every().day.at("00:05").do(rankCal)
# schedule.every(1).seconds.do(rankCal)

while True:
    schedule.run_pending()
    time.sleep(1)