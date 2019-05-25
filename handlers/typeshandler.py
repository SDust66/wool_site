#encoding:utf-8

import torndb
import tornado.httpserver
import tornado.ioloop
import tornado.options
import tornado.web
import session_zc

#mysql_conn = torndb.Connection("10.245.146.207:3306","wool",user="campuswool",password="campuswool",charset="utf8")
mysql_conn = torndb.Connection("localhost:3306","hitwool",user="wool",password="wool",charset="utf8")

class TypesHandler(tornado.web.RequestHandler):
    def get(self):
    	sql = "SELECT * FROM tags ORDER BY tag_usenum DESC LIMIT 1000"
    	tags_count = mysql_conn.query(sql)
    	#self.render("type_page.html",tags_count=tags_count)

		# 创建session对象，cookie保留1天
        session = session_zc.Session(self, 1)
        # 判断session里的zhuangtai等于True
    	if session['zhuangtai'] == True:
			self.render("type_page.html",tags_count=tags_count,username=session['yhm'])
        else:
			self.render("type_page.html",tags_count=tags_count,username=" ")