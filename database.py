import psycopg2


class PgsqlConnect:
    """连接数据库，执行sql脚本"""

    def __init__(self, dbname, user, password, host, port, sql):
        """初始化连接数据库，获取游标"""

        self.dbname = dbname
        self.user = user
        self.password = password
        self.host = host
        self.port = port
        self.sql = sql

        # 连接数据库
        self.conn = psycopg2.connect(dbname=self.dbname, user=self.user, password=self.password, host=self.host,
                                     port=self.port)

        # 获取游标
        self.cursor = self.conn.cursor()

    def execute_sql(self):
        """游标执行sql，返回[()]型数据"""

        # 游标执行sql
        self.cursor.execute(self.sql)

        # 获取执行sql后的返回结果
        result = self.cursor.fetchall()

        # 提交执行sql后的数据（插入数据时需要提交）
        self.conn.commit()

        # 关闭游标
        self.conn.close()

        return result
