#encoding:utf-8

import torndb
import tornado.httpserver
import tornado.ioloop
import tornado.options
import tornado.web

#mysql_conn = torndb.Connection("10.245.146.207:3306","wool",user="campuswool",password="campuswool",charset="utf8")
mysql_conn = torndb.Connection("10.241.118.52:3306","hitwool",user="wool",password="wool",charset="utf8")

class CommentItemHandler(tornado.web.RequestHandler):
	def get(self):
		yn = self.get_argument("yn").encode("utf-8")
		info_id = self.get_argument("info_id").encode("utf-8")
		#print yn
		if yn == "y":
			sql = "UPDATE infos SET info_up_num = info_up_num + 1 WHERE info_id=%s;"
			mysql_conn.execute(sql,info_id)
			self.redirect("/item?info_id="+info_id)
		elif yn == "n":
			sql = "UPDATE infos SET info_down_num = info_down_num + 1 WHERE info_id=%s;"
			mysql_conn.execute(sql,info_id)
			self.redirect("/item?info_id="+info_id)