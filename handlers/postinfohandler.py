#encoding:utf-8

import torndb
import tornado.httpserver
import tornado.ioloop
import tornado.options
import tornado.web

mysql_conn = torndb.Connection("10.245.146.207:3306","wool",user="campuswool",password="campuswool",charset="utf8")

class PostInfoHandler(tornado.web.RequestHandler):
    def get(self):
        self.render('post_page.html')

    def post(self):
        info_title = self.get_argument('info_title').encode("utf-8")
        info_price = self.get_argument('info_price').encode("utf-8")
        info_detail = self.get_argument('info_detail').encode("utf-8")
        label_usage = self.get_argument('label_usage').encode("utf-8")

        sql = "INSERT INTO infos(info_title,info_price,info_detail,label_usage)"\
                "VALUES (%s,%s,%s,%s)"
        mysql_conn.execute(sql,info_title,info_price,info_detail,label_usage)

        self.redirect("/")