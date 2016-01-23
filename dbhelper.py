import MySQLdb as mysql
import utils


class DBHelper(object):

    SETTINGS = None

    def __init__(self, table):
        self.__table = table
        self.__conn = mysql.connect(
            DBHelper.SETTINGS['host'],
            DBHelper.SETTINGS['username'],
            DBHelper.SETTINGS['password'],
            DBHelper.SETTINGS['database'],
        )
        self.__cursor = None
        self.__columns = self.__fetch_columns()

    @classmethod
    def inject_settings(cls, settings):
        cls.SETTINGS = settings

    def begin_transaction(self):
        if self.__cursor:
            raise RuntimeError('There is an uncommitted cursor.')
        self.__cursor = self.__conn.cursor()

    def end_transaction(self):
        if self.__cursor:
            self.__cursor.close()
            self.__cursor = None

    def commit(self):
        if self.__cursor:
            self.__cursor.close()
            self.__conn.commit()
            self.__cursor = None
        else:
            utils.warn('Nothing committed!!!')

    def select(self, where_clause=None):
        self.__check_cursor()
        sql = "SELECT * FROM `%s`" % self.__table
        if where_clause:
            sql += " WHERE %s" % where_clause
        utils.debug("Will execute: %s" % sql)
        count = self.__cursor.execute(sql)
        if count == 0L:
            return ()
        return self.__cursor.fetchall()

    def insert(self, *values):
        self.__check_cursor()
        cols = ""
        for col in self.__columns:
            if not cols == "":
                cols += ", "
            cols += col[0]
        vals = ""
        for val in values:
            if not vals == "":
                vals += ", "
            if type(val) == type(str()):
                vals += "\"%s\"" % val
            elif not val:
                vals += "NULL"
            else:
                vals += str(val)
        sql = "INSERT INTO `%s` (%s) VALUES (%s)" % (self.__table, cols, vals)
        utils.debug("Will execute: %s" % sql)
        return self.__cursor.execute(sql)

    def close(self):
        self.__conn.close()

    def __fetch_columns(self):
        sql = "DESC `%s`" % self.__table
        cursor = self.__conn.cursor()
        cursor.execute(sql)
        res = cursor.fetchall()
        cursor.close()
        return res

    def __check_cursor(self):
        if not self.__cursor:
            raise RuntimeError('There is no cursor.')
