import psycopg2

import psycopg2


class PostgresBaseManager:

    def __init__(self):

        self.database = 'ddrqvb30kbrdsa'
        self.user = 'lgectutbchtebn'
        self.password = '0dc73cbc693a2d36743e36248287bf4d90254a61205aa2f1647678ff5f4fdc75'
        self.host = 'ec2-3-209-61-239.compute-1.amazonaws.com'
        self.port = '5432'
        self.conn = self.connectServerPostgresDb()

    def connectServerPostgresDb(self):
        """
        :return: 連接 Heroku Postgres SQL 認證用
        """
        conn = psycopg2.connect(
            database = self.database,
            user = self.user,
            password = self.password,
            host = self.host,
            port = self.port)
        return conn

    def closePostgresConnection(self):
        """
        :return: 關閉資料庫連線使用
        """
        self.conn.close()

    def runServerPostgresDb(self):
        """
        :return: 測試是否可以連線到 Heroku Postgres SQL
        """
        cur = self.conn.cursor()
        cur.execute('SELECT VERSION()')
        results = cur.fetchall()
        print("Database version : {0} ".format(results))
        self.conn.commit()
        cur.close()


if __name__ == '__main__':
    postgres_manager = PostgresBaseManager()
    postgres_manager.runServerPostgresDb()
    print("Opened database successfully")
    postgres_manager.closePostgresConnection()
