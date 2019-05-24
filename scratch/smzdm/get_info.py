import os
import requests
import torndb
from bs4 import BeautifulSoup

mysql_conn = torndb.Connection("10.245.146.207:3306","wool",user="campuswool",password="campuswool",charset="utf8")
header = {
"Host": "www.smzdm.com",
"Connection": "keep-alive",
"Cache-Control": "max-age=0",
"Upgrade-Insecure-Requests": "1",
"User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.103 Safari/537.36",
"Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3",
"Accept-Encoding": "gzip, deflate, br",
"Accept-Language": "zh-CN,zh;q=0.9,en-US;q=0.8,en;q=0.7,zh-TW;q=0.6",
"Cookie":"Cookie: __jsluid=3e420ec97604b00d2700436d0ef726e6; __ckguid=OT15UO7ahvbj2HGKpaBfiL4; device_id=1879498792153636960962176191413fc0e80e0c1e7489fc98370de078; _ga=GA1.2.783582828.1536369612; smzdm_user_source=0E8220DE9114924BA7E1E7E43B0A36EB; homepage_sug=g; smzdm_user_view=E0EACC94A7BF5967787C1635E20CFDB4; zdm_qd=%7B%7D; ss_ab=ss14; Hm_lvt_9b7ac3d38f30fe89ff0b8a0546904e58=1553348600,1553525152,1553525157,1555768351; s_his=%E4%BF%9D%E9%99%A9%E6%9F%9C%2C%E9%B8%A1%E8%83%B8%2C%E7%B4%A2%E5%B0%BC%E7%94%B5%E8%A7%86%2C%E6%8B%BC%E5%A4%9A%E5%A4%9A; PHPSESSID=64898c2f76d05bcb807c1ba756205bb0; ad_date=22; ad_json_feed=%7B%7D; _gid=GA1.2.1443671292.1555921117; wt3_eid=%3B999768690672041%7C2153636961500530496%232155592131000413454; wt3_sid=%3B999768690672041; _zdmA.uid=ZDMA.1ZKqQVz-i.1555933946.2419200; _zdmA.vid=*; bannerCounter=%5B%7B%22number%22%3A2%2C%22surplus%22%3A1%7D%2C%7B%22number%22%3A2%2C%22surplus%22%3A1%7D%2C%7B%22number%22%3A2%2C%22surplus%22%3A1%7D%2C%7B%22number%22%3A0%2C%22surplus%22%3A3%7D%2C%7B%22number%22%3A2%2C%22surplus%22%3A1%7D%2C%7B%22number%22%3A0%2C%22surplus%22%3A3%7D%5D; _gat_UA-27058866-1=1; _dc_gtm_UA-27058866-1=1"
}
a = requests.get("http://www.smzdm.com/top/",headers=header,verify=False)

soup = BeautifulSoup(a.text,"lxml")
a,b,c = [],[],[]
for i in soup.find_all(name='div',attrs={"class":"feed-hot-pic"}):
	a.append(str(i)[43:-9])
for i in soup.find_all(name='div',attrs={"class":"feed-hot-title"}):
	b.append(i.text)
for i in soup.find_all(name='span',attrs={"class":"z-highlight"}):
	c.append(i.text.split(",")[0])

print a
print b

for i in range(len(b)):
	mysql_conn.execute("insert into infos(info_title,info_image,info_price) values(%s,%s,%s)",b[i],a[i],c[i])


images = mysql_conn.query("select info_image from infos;")

for i in images:
    if i['info_image']:
    	yuju = "curl "+" -o "+str(i['info_image']).split("/")[-1]+"  "+str(i['info_image'])
    	print (yuju)
        os.system(yuju)

mysql_conn.execute("delete from infos where info_price='';")







