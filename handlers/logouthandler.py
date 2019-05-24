#encoding:utf-8

import torndb
import tornado.httpserver
import tornado.ioloop
import tornado.options
import tornado.web
import session_zc

#mysql_conn = torndb.Connection("10.245.146.207:3306","wool",user="campuswool",password="campuswool",charset="utf8")
mysql_conn = torndb.Connection("localhost:3306","hitwool",user="wool",password="wool",charset="utf8")

#登出
class LogoutHandler(tornado.web.RequestHandler):
    def get(self,*args,**kwargs):
        # 创建session对象，cookie保留1天
        #session = session_zc.Session(self,1)
        # 将用户名保存到session
        #session['yhm'] = None
        # 将密码保存到session
        #session['mim'] = None
        # 在session写入登录状态
        #session['zhuangtai'] = False

        self.clear_cookie("xr_cookie")
        self.redirect('/')