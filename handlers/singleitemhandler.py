#encoding:utf-8
import random
import torndb
import tornado.httpserver
import tornado.ioloop
import tornado.options
import tornado.web

mysql_conn = torndb.Connection("10.245.146.207:3306","wool",user="campuswool",password="campuswool",charset="utf8")

class SingleItemHandler(tornado.web.RequestHandler):

    def get_recommends(self,sql_param):
        '''
        根据当前优惠信息，推荐更多相似优惠信息
        '''
        sql = 'SELECT * FROM infos WHERE MATCH(info_tags) AGAINST(%s) UNION '\
                'SELECT * FROM infos WHERE MATCH(info_tags) AGAINST(%s) UNION '\
                'SELECT * FROM infos WHERE MATCH(info_tags) AGAINST(%s)\
                LIMIT 8;'

        recommends = mysql_conn.query(sql,sql_param[2],sql_param[1],sql_param[0])

        return recommends


    def get_top(self):
        '''
        推荐最热门的优惠信息
        '''
        sql = 'SELECT * FROM infos,infos_comment WHERE infos.info_id=infos_comment.info_id\
                 ORDER BY info_visited DESC LIMIT 5'

        top = mysql_conn.query(sql)

        return top

    def update_visited_count(self,info_id):
        '''
        每次有用户访问优惠信息页面，给对应记录的info_visited字段加一
        '''
        add_visited = random.randint(1,500)
        sql = "UPDATE infos_comment SET info_visited = info_visited + %s WHERE info_id=%s;"
        mysql_conn.execute(sql,str(add_visited),info_id)


    def get(self):
        '''
        返回单个优惠信息页面的全部内容
        '''
        info_id = self.get_argument('info_id').encode("utf-8")
        sql = "SELECT * FROM infos,infos_comment WHERE infos.info_id=%s and \
                infos.info_id=infos_comment.info_id"
        print mysql_conn.query(sql,info_id)
        infos = mysql_conn.query(sql,info_id)[0]
        if infos['info_detail']:
            infos['info_detail'] = infos['info_detail'].encode("utf-8").replace("。","。<br>")
        infos['info_tags'] = infos['info_tags'].split(",")[0:3]

        recommends = self.get_recommends(infos['info_tags'])
        top = self.get_top()
        self.update_visited_count(info_id)
        
        self.render('detail_page.html',infos=infos,recommends=recommends,top=top)

    def post(self):
        pass
        
        