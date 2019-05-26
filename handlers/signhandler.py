#encoding:utf-8

import torndb
import tornado.httpserver
import tornado.ioloop
import tornado.options
import tornado.web
import re

#mysql_conn = torndb.Connection("10.245.146.207:3306","wool",user="campuswool",password="campuswool",charset="utf8")
mysql_conn = torndb.Connection("10.241.118.52:3306","hitwool",user="wool",password="wool",charset="utf8")

#注册
class SignHandler(tornado.web.RequestHandler):
    def get(self,*args,**kwargs):
        self.render("signin.html")

    def post(self,*args,**kwargs):
        loginemail=self.get_argument('login_email').encode("utf-8")
        loginname=self.get_argument("login_name").encode("utf-8")
        password1=self.get_argument('password1').encode("utf-8")
        password2=self.get_argument('password2').encode("utf-8")
        r_mail_addr=r"[a-z0-9\.\-+_]+@[a-z0-9\.\-+_]+\.[a-z]+"

        # %s 要加上'' 否则会出现KeyboardInterrupt的错误
        temp1 = "select user_mail,user_name from userinformation where user_mail='%s' or user_name='%s'" % (loginemail, loginname)
        result1 = mysql_conn.query(temp1)
        if result1:
            self.write('邮箱已注册或者用户名已存在！')
        else:
            if re.match(r_mail_addr,loginemail) and len(loginname)<16:
                if password1==password2 and password1!="":
                    try:
                        #执行语句
                        temp2 = "insert into userinformation(user_mail,user_name,user_pwd) values(%s,%s,%s)"
                    except Exception as e:
                        print(str(e))
                    mysql_conn.execute(temp2, loginemail, loginname, password1)
                    self.redirect("/login")
                else:
                    self.write("输入密码有误！")
            else:
                self.write("邮箱或用户名不符合要求！")