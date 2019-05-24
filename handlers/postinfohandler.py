#encoding:utf-8

import torndb
import tornado.httpserver
import tornado.ioloop
import tornado.options
import tornado.web
import session_zc

#mysql_conn = torndb.Connection("10.245.146.207:3306","wool",user="campuswool",password="campuswool",charset="utf8")
mysql_conn = torndb.Connection("localhost:3306","hitwool",user="wool",password="wool",charset="utf8")

class PostInfoHandler(tornado.web.RequestHandler):
    def get(self):
        # 创建session对象，cookie保留1天
        session = session_zc.Session(self, 1)
        # 判断session里的zhuangtai等于True
        if session['zhuangtai'] == True:
            wzname=session['yhm']
            self.render('post_page.html',username=wzname)
        else:
            self.redirect("/login")
        #self.render('post_page.html')

    def post(self):
        session = session_zc.Session(self, 1)
        wzname = session['yhm']
        info_title = self.get_argument('info_title').encode("utf-8")
        info_price = self.get_argument('info_price').encode("utf-8")
        info_detail = self.get_argument('info_detail').encode("utf-8")
        info_image = self.get_argument('info_image').encode("utf-8")
        source = self.get_argument('source').encode("utf-8")
        info_type = self.get_argument('info_type').encode("utf-8")
        brand = self.get_argument('brand').encode("utf-8")
        label = self.get_argument('label').encode("utf-8")
        label_usage = source + "," + info_type + "," + brand

        sql = "INSERT INTO infos(info_title,info_price,info_detail,info_image,info_label,info_act_id,info_update_user)"\
                "VALUES (%s,%s,%s,%s,%s,%s,%s)"
        mysql_conn.execute(sql,info_title,info_price,info_detail,info_image,label_usage,label,wzname)

        self.redirect("/")