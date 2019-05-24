#encoding:utf-8

import torndb
import tornado.httpserver
import tornado.ioloop
import tornado.options
import tornado.web

mysql_conn = torndb.Connection("10.245.146.207:3306","wool",user="campuswool",password="campuswool",charset="utf8")

class SearchPageHandler(tornado.web.RequestHandler):
    def get(self):
        '''
        返回对应标签的全部内容
        '''
        info_tag = self.get_argument('tag').encode("utf-8")
        try:
        	page = int(self.get_argument('page').encode("utf-8"))
        except:
        	page = 1
        start = 20*(page-1)
        end   = 20*page
        sql = "SELECT * FROM infos WHERE MATCH(info_tags) AGAINST(%s) ORDER BY info_id DESC LIMIT %s,%s"
        infos = mysql_conn.query(sql,info_tag,start,end)
        
        self.render('main_page.html',infos=infos,page=page,source="tag",kwd=info_tag)
    

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
        self.render('main_page.html',infos=infos,page=page,source="search",kwd=info_keyword)