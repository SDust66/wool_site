#encoding:utf-8

import torndb
import tornado.httpserver
import tornado.ioloop
import tornado.options
import tornado.web

mysql_conn = torndb.Connection("10.245.146.207:3306","wool",user="campuswool",password="campuswool",charset="utf8")

class TypesHandler(tornado.web.RequestHandler):
    def get(self):
    	sql = "SELECT * FROM tags_count ORDER BY info_count DESC LIMIT 1000"
    	tags_count = mysql_conn.query(sql)
    	self.render("type_page.html",tags_count=tags_count)
