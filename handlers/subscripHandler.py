#encoding:utf-8

import torndb
import tornado.httpserver
import tornado.ioloop
import tornado.options
import tornado.web
import session_zc

#mysql_conn = torndb.Connection("10.245.146.207:3306","wool",user="campuswool",password="campuswool",charset="utf8")
mysql_conn = torndb.Connection("10.241.118.52:3306","hitwool",user="wool",password="wool",charset="utf8")

class SubscriptionPageHandler(tornado.web.RequestHandler):
    def get(self):
        # 创建session对象，cookie保留1天
        session = session_zc.Session(self, 1)
        # 判断session里的zhuangtai等于True
        if session['zhuangtai'] == True:
            wzname = session['yhm']
            sql_tag = "SELECT user_tag FROM userinformation WHERE user_name = '%s'" % (wzname)
            tagstr = mysql_conn.query(sql_tag)
            #print(type(tagstr), type(tagstr[0]['usertag']),tagstr,tagstr[0]['usertag'])
            if len(tagstr)==0:
                self.redirect('/sub_change?tag=zero')
            else:
                tags = tagstr[0]['user_tag'].encode('utf-8')
                tags = tags.split(',')
                print("tags:",tags)
                infos = []
                for tag in tags:
                    #print(tag)
                    sql = "SELECT * FROM infos WHERE info_label LIKE '%%%%%s%%%%' ORDER BY info_id DESC LIMIT 100"%tag
                    info = mysql_conn.query(sql)
                    infos.extend(info)
                #print(infos)
                run_function = lambda x, y: x if y in x else x + [y]
                infos = reduce(run_function, [[], ] + infos)
                self.render('subscription.html',infos=infos,username=wzname)
        else:
            self.redirect('/login')