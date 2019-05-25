#encoding:utf-8

import torndb
import tornado.httpserver
import tornado.ioloop
import tornado.options
import tornado.web
import session_zc

#mysql_conn = torndb.Connection("10.245.146.207:3306","wool",user="campuswool",password="campuswool",charset="utf8")
mysql_conn = torndb.Connection("localhost:3306","hitwool",user="wool",password="wool",charset="utf8")

class ReportHandler(tornado.web.RequestHandler):
    def get(self):
		info_id = self.get_argument('info_id').encode("utf-8")

		# 创建session对象，cookie保留1天
		session = session_zc.Session(self, 1)
		# 判断session里的zhuangtai等于True
		if session['zhuangtai'] == True:
			sql = "UPDATE infos SET info_report_num=info_report_num+1 WHERE info_id=%s"
			mysql_conn.execute(sql,info_id)
			sql = "INSERT INTO delete_infos SELECT * from infos WHERE info_report_num >=3; DELETE FROM infos WHERE info_report_num >=3;"
			mysql_conn.execute(sql)
			self.redirect("/")
		else:
			self.write("请登录后再操作!")