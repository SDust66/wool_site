#encoding:utf-8

import torndb
import tornado.httpserver
import tornado.ioloop
import tornado.options
import tornado.web
import session_zc

#mysql_conn = torndb.Connection("10.245.146.207:3306","wool",user="campuswool",password="campuswool",charset="utf8")
mysql_conn = torndb.Connection("10.241.118.52:3306","hitwool",user="wool",password="wool",charset="utf8mb4")

class SearchPageHandler(tornado.web.RequestHandler):
    def get(self):
        '''
        返回对应标签的全部内容
        '''
        info_tag = self.get_argument('tag').encode('utf-8')
        #print(info_tag)
        try:
        	page = int(self.get_argument('page').encode("utf-8"))
        except:
        	page = 1
        start = 20*(page-1)
        end   = 20*page

        # 创建session对象，cookie保留1天
        session = session_zc.Session(self, 1)
        # 判断session里的zhuangtai等于True
    	if session['zhuangtai'] == True:
            name = session['yhm']
        else :
            name = " "

        infos = None
        brand_en,brand_cn = "",""

        if info_tag[0]=="$":
            info_tag = info_tag[1:]

            # print info_tag
            # print info_tag
            # print info_tag

            if "/" in info_tag:
                brand_en,brand_cn = info_tag.split("/")

            # if len(info_tag)<3 or len(brand_cn)<7 or len(brand_en)<3:
            #print "放弃FULLTEXT"
            sql = "SELECT * FROM infos WHERE info_label like '%%%%%s%%%%' ORDER BY info_id DESC LIMIT %s,%s"%(info_tag,start,end)
            infos = mysql_conn.query(sql)

            # else:
            #     print "使用FULLTEXT"
            #     sql = "SELECT * FROM infos WHERE MATCH(info_label) AGAINST(%s) ORDER BY info_id DESC LIMIT %s,%s"
            #     infos = mysql_conn.query(sql,info_tag,start,end)

            total = len(infos)
            self.render('main_page.html',infos=infos,page=page,total=total,source="tag",kwd=info_tag,username=name)

        else:
            sql = "SELECT * FROM infos WHERE info_title LIKE '%%%%%s%%%%' ORDER BY info_id DESC LIMIT %s,%s"%(info_tag,start,end)
            infos = mysql_conn.query(sql)
            total = len(infos)
            self.render('main_page.html',infos=infos,page=page,total=total,source="search",kwd=info_tag,username=name)


    def post(self):
    	'''
		在搜索框中输入内容
    	'''
        info_keyword = self.get_argument('info_keyword').encode("utf-8")
        try:
        	page = int(self.get_argument('page').encode("utf-8"))
        except:
        	page = 1
        start = 20*(page-1)
        end   = 20*page        
        sql = "SELECT * FROM infos WHERE info_title LIKE '%%%%%s%%%%' ORDER BY info_id DESC LIMIT %s,%s"%(info_keyword,start,end)
        infos = mysql_conn.query(sql)
        total = len(infos)

        # 创建session对象，cookie保留1天
        session = session_zc.Session(self, 1)
        # 判断session里的zhuangtai等于True
    	if session['zhuangtai'] == True:
            name = session['yhm']
        else :
            name = " "

        self.render('main_page.html',infos=infos,page=page,total=total,source="search",kwd=info_keyword,username=name)