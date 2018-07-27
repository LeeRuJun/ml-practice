import pymysql

class DbTools:
    def __init__(self):
        self.db = pymysql.connect(db='gslivedb_uat', host='localhost', port=55777, user='us_test_rj_li', passwd='',
                                  charset='utf8')
        self.cursor = self.db.cursor()

    def savaCity(self,A,B,C,D,E,F,G,H):
        sql = 'Insert into `%s` values("%s","%s","%s","%s","%s","%s","%s")' % (A, B, C, D, E, F, G, H)
        self.cursor.execute(sql)
        self.db.commit()
        return True




