#encoding:utf-8

import torndb
import tornado.httpserver
import tornado.ioloop
import tornado.options
import tornado.web
import session_zc

#mysql_conn = torndb.Connection("10.245.146.207:3306","wool",user="campuswool",password="campuswool",charset="utf8")
mysql_conn = torndb.Connection("localhost:3306","hitwool",user="wool",password="wool",charset="utf8")

class RankPageHandler(tornado.web.RequestHandler):
    def get(self):
		sql = "SELECT * FROM infos ORDER BY info_up_num DESC, info_visited DESC, info_down_num LIMIT 40"
		infos = mysql_conn.query(sql)

		# 创建session对象，cookie保留1天
		session = session_zc.Session(self, 1)
		# 判断session里的zhuangtai等于True
		if session['zhuangtai'] == True:
			#wzname = session['yhm']
			self.render("rank_page.html",infos=infos,page=1,source="rank",username=session['yhm'])
		else:
			self.render("rank_page.html",infos=infos,page=1,source="rank",username=" ")
