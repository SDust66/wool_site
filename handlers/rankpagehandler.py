#encoding:utf-8

import torndb
import tornado.httpserver
import tornado.ioloop
import tornado.options
import tornado.web

mysql_conn = torndb.Connection("10.245.146.207:3306","wool",user="campuswool",password="campuswool",charset="utf8")

class RankPageHandler(tornado.web.RequestHandler):
    def get(self,data):
		data = data.encode("utf-8")
		if data == "cabbage":
			kwd = "每日白菜"
			sql = "SELECT * FROM infos WHERE MATCH(info_tags) AGAINST(%s) ORDER BY info_update_time DESC LIMIT 40"
			infos = mysql_conn.query(sql,kwd)
			self.render("rank_page.html",infos=infos,page=1,source="rank")
		if data == "":
			pass
