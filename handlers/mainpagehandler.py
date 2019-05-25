#encoding:utf-8

import torndb
import tornado.httpserver
import tornado.ioloop
import tornado.options
import tornado.web
import session_zc

#mysql_conn = torndb.Connection("10.245.146.207:3306","wool",user="campuswool",password="campuswool",charset="utf8")
mysql_conn = torndb.Connection("10.241.118.52:3306","hitwool",user="wool",password="wool",charset="utf8")

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
        total = len(infos)
        print(total)

        # 创建session对象，cookie保留1天
        session = session_zc.Session(self, 1)
        # 判断session里的zhuangtai等于True
        if session['zhuangtai'] == True:
            #wzname = session['yhm']
            self.render('main_page.html',infos=infos,page=page,total=total,source="main",username=session['yhm'])
        else:
            self.render('main_page.html',infos=infos,page=page,total=total,source="main",username=" ")

        