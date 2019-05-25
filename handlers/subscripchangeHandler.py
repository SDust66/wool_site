#encoding:utf-8

import torndb
import tornado.httpserver
import tornado.ioloop
import tornado.options
import tornado.web
import session_zc

#mysql_conn = torndb.Connection("10.245.146.207:3306","wool",user="campuswool",password="campuswool",charset="utf8")
mysql_conn = torndb.Connection("10.241.118.52:3306","hitwool",user="wool",password="wool",charset="utf8mb4")

class SubscriptionChangeHandler(tornado.web.RequestHandler):
    def get(self):
        tag = self.get_argument("tag").encode("utf-8")
        print("tag",tag)
        # 创建session对象，cookie保留1天
        session = session_zc.Session(self, 1)
        # 判断session里的zhuangtai等于True
        if session['zhuangtai'] == True:
            wzname = session['yhm']
            if tag=="zero":
                sql_tag = "SELECT user_tag FROM userinformation WHERE user_name = '%s'" % (wzname)
                tags = mysql_conn.query(sql_tag)
                tags = tags[0]['user_tag'].encode("utf-8")
                tags = tags.split(",")
                #print(tags)
                sql = "SELECT tag_name,tag_usenum FROM tags"
                ftags = mysql_conn.query(sql)
                #print(ftags)
                self.render('sub_change.html', tags=tags ,ftags=ftags, username=wzname)
            else:
                sql_tag = "SELECT user_tag FROM userinformation WHERE user_tag like '%%%%%s%%%%' and user_name = '%s'" % (tag, wzname)
                result = mysql_conn.query(sql_tag)
                #print(result)
                if result==[]:
                    sql_tag = "SELECT user_tag FROM userinformation WHERE user_name = '%s'" % (wzname)
                    tags = mysql_conn.query(sql_tag)
                    tags = tags[0]['user_tag'].encode("utf-8") + "," + tag
                    sql_tag = "UPDATE userinformation SET user_tag='%s' WHERE user_name ='%s' " % (tags, wzname)
                    mysql_conn.execute(sql_tag)
                    self.redirect('/sub_change?tag=zero')
                else:
                    sql_tag = "SELECT user_tag FROM userinformation WHERE user_name = '%s'" % (wzname)
                    tags = mysql_conn.query(sql_tag)
                    tags = tags[0]['user_tag'].encode("utf-8")
                    tags = tags.split(",")
                    tags.remove(tag)
                    in_tag = ",".join(tags)
                    sql_tag = "UPDATE userinformation SET user_tag='%s' WHERE user_name ='%s' " % (in_tag, wzname)
                    mysql_conn.execute(sql_tag)
                    self.redirect('/sub_change?tag=zero')

        else:
            self.redirect('/login')