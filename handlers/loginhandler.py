#encoding:utf-8

import torndb
import tornado.httpserver
import tornado.ioloop
import tornado.options
import tornado.web
import session_zc

#mysql_conn = torndb.Connection("10.245.146.207:3306","wool",user="campuswool",password="campuswool",charset="utf8")
mysql_conn = torndb.Connection("localhost:3306","hitwool",user="wool",password="wool",charset="utf8")

#登陆
class LoginHandler(tornado.web.RequestHandler):
    def get(self,*args,**kwargs):
        self.render("login.html")

    def post(self,*args,**kwargs):
        #loginemail=self.get_argument('login_email').encode("utf-8")
        loginname=self.get_argument('login_name').encode("utf-8")
        password1=self.get_argument('password1').encode("utf-8")
        #self.render("query_1.html")

        # %s 要加上'' 否则会出现KeyboardInterrupt的错误
        temp = "select user_name,user_pwd from userinformation where user_name='%s' and user_pwd='%s'" % (loginname, password1)
        result = mysql_conn.query(temp)

        if result:
            #if loginname == 'admin' and password1 == 'admin':
            print('登陆成功')
            # 创建session对象，cookie保留1天
            session = session_zc.Session(self,1)
            # 将用户名保存到session
            session['yhm'] = loginname
            # 将密码保存到session
            session['mim'] = password1
            # 在session写入登录状态
            session['zhuangtai'] = True
            self.redirect('/')
        else:
            self.write("登录失败！")
            #self.render('login.html',tishi = '用户名或密码错误')