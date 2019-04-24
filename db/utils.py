# @Time      : 2019.04.18
# @Author    : kawa Yeung
# @Licence   : MIT
# @function  : database utils


import os
import configparser

import pymysql
from DBUtils.PooledDB import PooledDB


current_path = os.path.dirname(__file__)


class DBUtils:
    """
    database utils
    """

    def __init__(self):
        conf = configparser.ConfigParser()
        conf.read(os.path.join(current_path, "..", "config.ini"))

        HOST = conf.get("mysql", "host")
        USER = conf.get("mysql", "user")
        PASSWORD = conf.get("mysql", "password")
        DB = conf.get("mysql", "db")

        self._pool = PooledDB(pymysql, host=HOST, user=USER, passwd=PASSWORD, db=DB, port=3306)
        self._conn = self._pool.connection()

    def get_conn(self):
        """
        get database connection
        :return:
        """

        return self._conn

    def __del__(self):
        self._conn.close()


db = DBUtils()
conn = db.get_conn()
