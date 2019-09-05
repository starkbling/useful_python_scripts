#以下代码实现了python的每天定时执行：
import datetime
import time
import pymysql

def doSth():

    # print('test')
    conn = pymysql.Connect(
        host='192.0.9.169',
        port=5507,
        user='writer',
        passwd='Apsdf',
        db='api_data',
        charset='utf8'
    )
    cur = conn.cursor()
    cur.execute("""select * from table1""")
    conn.commit()
    cur.close()
    conn.close()
    # 假装做这件事情需要一分钟

    time.sleep(60)



def main(h=23, m=0):

    '''h表示设定的小时，m为设定的分钟'''

    while True:

        # 判断是否达到设定时间，例如23:00

        while True:

            now = datetime.datetime.now()

            # 到达设定时间，结束内循环

            if now.hour==h and now.minute==m:

                break

            # 不到时间就等20秒之后再次检测

            time.sleep(20)

        # 做正事，一天做一次

        doSth()
if __name__ == '__main__':
    main()
