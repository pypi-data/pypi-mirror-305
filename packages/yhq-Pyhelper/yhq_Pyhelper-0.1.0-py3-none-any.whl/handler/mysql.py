#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Date    : 2021/10/19
# @Author  : HuiQing Yu
import logging
import time

import pymysql
import pymysql.cursors


class SQLStatement:
    logger = logging.getLogger()

    def __init__(self, tn=None, sql: str = None):
        self.__tn = tn
        self.__sql = sql
        self.__conn = None

    def get_sql(self):
        return self.__sql

    def client(self, host: str, port: int, user: str, pwd: str, database: str):
        try:
            self.__conn = pymysql.connect(host=host, port=port, user=user, password=pwd, database=database)
            self.logger.info(f"executing SQL -->> {self.__sql}")
            return self
        except Exception as e:
            self.logger.error(f"Error connecting to MySQL: {e}")

    def query(self, is_waiting=False):
        self.__conn.ping(reconnect=True)
        cursor = self.__conn.cursor(cursor=pymysql.cursors.DictCursor)
        try:
            data, tim = None, 0
            while True:
                cursor.execute(self.__sql)
                if cursor.rowcount == 0 and tim < 10:
                    if is_waiting:
                        self.logger.warning('no data found, Waiting for retry after 30s……')
                        time.sleep(30)
                        tim += 1
                        continue
                    else:
                        self.logger.warning('there is no data……')
                        return {}
                data = cursor.fetchone()
                break
            self.logger.info(f"查询结果：{'1 条' if data is not None else '0 条'}")
            # 清掉空值
            keys_to_remove = [key for key, value in data.items() if value in (None, '')]
            for key in keys_to_remove:
                del data[key]
            return data
        except Exception as e:
            self.logger.error(f"Error executing query: {e}")
            cursor.close()
            self.__conn.rollback()

    def queries(self, is_waiting=False):
        self.__conn.ping(reconnect=True)
        cursor = self.__conn.cursor(cursor=pymysql.cursors.DictCursor)
        try:
            data, tim = None, 0
            while True:
                cursor.execute(self.__sql)
                # 如果查询无结果，则不打印prettytable
                if cursor.rowcount == 0 and tim < 10:
                    if is_waiting:
                        self.logger.warning('no data found, Waiting for retry after 30s……')
                        time.sleep(30)
                        tim += 1
                        continue
                    else:
                        self.logger.warning('there is no data……')
                        return {}
                data = cursor.fetchall()
                break
            self.logger.info(f'There are {len(data)} pieces of data found')
            return data
        except Exception as e:
            self.logger.error(f"Error executing query: {e}")
            cursor.close()
            self.__conn.rollback()

    def modify(self):
        self.__conn.ping(reconnect=True)
        cursor = self.__conn.cursor(cursor=pymysql.cursors.DictCursor)
        try:
            cursor.execute(self.__sql)
            self.__conn.commit()
            return {"last_row_id": cursor.lastrowid, "affected_rows": self.__conn.affected_rows()}
        except Exception as e:
            self.logger.error(f"Error executing modify: {e}")
            cursor.close()
            self.__conn.rollback()

    def __del__(self):
        try:
            if self.__conn:
                self.__conn.close()
        except Exception as e:
            self.logger.error(e)

    def insert(self, values: dict):
        """
        :param values: 示例-> values={'key1':[1,2],'key2':[3,4]}
        :return:
        """
        vsl = [list(t) for t in zip(*values.values())]
        vs = []
        for v in vsl:
            t = f"({','.join(str(x) for x in v)})"
            vs.append(t)
        self.__sql = f"INSERT INTO {self.__tn} ({','.join(values.keys())}) VALUES {','.join(vs)}"
        return self

    def delete(self):
        self.__sql = "DELETE " + f" FROM {self.__tn}"
        return self

    def update(self, values):
        """
        :param values:示例->values={'key':'1'}
        :return:
        """
        values_str = ', '.join([f'{k}={v}' for k, v in values.items()])
        self.__sql = f"UPDATE {self.__tn} " + f"SET {values_str} "
        return self

    def select(self, columns=None):
        """
        :param columns:示例->['id','create_time']
        :return:
        """
        self.__sql = f"SELECT {'*' if columns is None else ','.join(columns)} FROM {self.__tn} "
        return self

    def where(self, condition, f='and'):
        """
        :param f: 条件方法
        :param condition: 示例->condition=['id = 1','num>2']
        :return:
        """
        if condition:
            self.__sql = f'{self.__sql} where {f" {f} ".join(condition)} '
        return self

    def limit(self, page):
        """
        :param page:示例->page={cur_page:1,page_size:10}
        :return:
        """
        self.__sql = self.__sql + f' limit {(page.cur_page - 1) * page.page_size},{page.page_size}'
        return self

    def order_by(self, columns, f='asc'):
        """
        :param f: 代表方式，不填则默认asc
        :param columns:  示例：columns=['id','create_time']
        :return:
        """
        self.__sql = self.__sql + 'order by ' + ','.join(columns) + f' {f} '
        return self
