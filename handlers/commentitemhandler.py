#encoding:utf-8

import torndb
import tornado.httpserver
import tornado.ioloop
import tornado.options
import tornado.web

mysql_conn = torndb.Connection("10.245.146.207:3306","wool",user="campuswool",password="campuswool",charset="utf8")

class CommentItemHandler(tornado.web.RequestHandler):
	def get(self):
		yn = self.get_argument("yn").encode("utf-8")
		info_id = self.get_argument("info_id").encode("utf-8")
		print yn
		if yn == "y":
			sql = "UPDATE infos_comment SET up = up + 1 WHERE info_id=%s;"
		elif yn == "n":
			sql = "UPDATE infos_comment SET down = down + 1 WHERE info_id=%s;"
	    	mysql_conn.execute(sql,info_id)