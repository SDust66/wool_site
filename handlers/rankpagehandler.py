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
    def get(self,data):
		data = data.encode("utf-8")

		# 创建session对象，cookie保留1天
		session = session_zc.Session(self, 1)
		# 判断session里的zhuangtai等于True
		if session['zhuangtai'] == True:
			#wzname = session['yhm']
			username=session['yhm']
			#self.render("rank_page.html",infos=infos,page=1,source="rank",username=session['yhm'])
		else:
			username=" "
			#self.render("rank_page.html",infos=infos,page=1,source="rank",username=" ")

		if data == "goods":
			sql = "SELECT * FROM infos WHERE info_act_id=0 ORDER BY info_up_num DESC, info_visited DESC, info_down_num LIMIT 40"
			infos = mysql_conn.query(sql)
			self.render("rank_page.html",infos=infos,page=1,source="rank",username=username)
		
		elif data == "activity":
			sql = "SELECT * FROM infos WHERE info_price='activity' ORDER BY info_up_num DESC, info_visited DESC, info_down_num LIMIT 40"
			infos = mysql_conn.query(sql)
			self.render("rank_page.html",infos=infos,page=1,source="rank",username=username)
		
		elif data == "visited":
			sql = "SELECT * FROM infos  ORDER BY info_visited DESC, info_up_num DESC, info_down_num LIMIT 40"
			infos = mysql_conn.query(sql)
			self.render("rank_page.html",infos=infos,page=1,source="rank",username=username)

		else:
			sql = "SELECT * FROM infos  ORDER BY info_up_num DESC, info_visited DESC, info_down_num LIMIT 40"
			infos = mysql_conn.query(sql)
			self.render("rank_page.html",infos=infos,page=1,source="rank",username=username)