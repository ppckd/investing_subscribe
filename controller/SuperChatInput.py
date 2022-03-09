import pymysql


class Calprofit:

    def predict_stock(self):
        ic_db = pymysql.connect(
            user='invest_admin',
            passwd='abc123',
            host='127.0.0.1',
            db='ic_db',
            charset='utf8'
        )

        sql = """INSERT INTO superchat(roomNo, userID, stockName, stockCode, currentPrice, predictPrice, stopLossPrice, today, predictDate, contents, createdTime)
                VALUES({}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {})
                """.format(roomNo, userID, stockName, stockCode, currentPrice, predictPrice, stopLossPrice, today,
                           predictDate, contents, createdTime)

        cursor.execute(sql)
        ic_db.commit()
        conn.close()

    def cal_stock(self):
        pass

