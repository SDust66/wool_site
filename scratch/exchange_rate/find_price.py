#encoding:utf-8
import torndb
import requests
from bs4 import BeautifulSoup

mysql_conn = torndb.Connection("10.245.146.207:3306","wool",user="campuswool",password="campuswool",charset="utf8")

path = 'exchange_rate.html'
htmlfile = open(path,'r')
htmlhandle = htmlfile.read()
soup = BeautifulSoup(htmlhandle,"lxml")
a = soup.find_all(name="div",attrs={"class":"tgme_widget_message_text js-message_text before_footer"})
b = soup.find_all(name="time")
print len(a)
print b[0]['datetime']

for i in range(len(a)):
	if a[i].b:
		info_title = a[i].b.text + b[i]['datetime']
		info_price = a[i].text[10:]
		sql = "insert into infos(info_title,info_image,info_price,info_detail,info_tags) values(%s,%s,%s,%s,%s)"
		mysql_conn.execute(sql,info_title,"http://www.offcn.com/dl/2015/0226/20150226122439514.jpg",info_price[:10],info_price,"每日精选,汇率")
