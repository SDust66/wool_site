#encoding:utf-8

import torndb
import tornado.httpserver
import tornado.ioloop
import tornado.options
import tornado.web

mysql_conn = torndb.Connection("10.245.146.207:3306","wool",user="campuswool",password="campuswool",charset="utf8")

class MainPageHandler(tornado.web.RequestHandler):
    def get(self):
    	try:
    		page = int(self.get_argument('page').encode("utf-8"))
    	except:
    		page = 1
    	#page = int(page) if page else 1
        start = 20*(page-1)
        end   = 20*page
        sql = "SELECT * FROM infos ORDER BY info_id DESC LIMIT %s,%s"
        infos = mysql_conn.query(sql,start,end)

        self.render('main_page.html',infos=infos,page=page,source="main")