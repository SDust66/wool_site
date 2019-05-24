#encoding:utf-8
import torndb
import requests
from bs4 import BeautifulSoup

mysql_conn = torndb.Connection("10.245.146.207:3306","wool",user="campuswool",password="campuswool",charset="utf8")
def url_generator(start,nums):
	urls = []
	for i in range(nums):
		urls.append("https://www.smzdm.com/p/"+str(13693500+i))
	return urls

def get_single_item_infos(url):
	header = {
        "Host"          :  "www.smzdm.com",
        "Connection":  "keep-alive",
        "Upgrade-Insecure-Requests" : "1",
        "User-Agent":  "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.103 Safari/537.36",
        "Accept"    :  "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3",
        "Accept-Encoding":      "gzip, deflate, br",
        "Accept-Language":      "zh-CN,zh;q=0.9,en-US;q=0.8,en;q=0.7,zh-TW;q=0.6",
        "Cookie"    :   "__jsluid=3e420ec97604b00d2700436d0ef726e6; __ckguid=OT15UO7ahvbj2HGKpaBfiL4; device_id=1879498792153636960962176191413fc0e80e0c1e7489fc98370de078; _ga=GA1.2.783582828.1536369612; smzdm_user_source=0E8220DE9114924BA7E1E7E43B0A36EB; homepage_sug=g; r_sort_type=score; ss_ab=ss47; smzdm_user_view=F38C591860E680372197F39FEEBC7630; is_first_youhui=1; s_his=%E7%94%B7%E5%AD%90%E5%B7%A5%E8%A3%85%E7%9F%AD%E8%A3%A4%2C%E7%9B%B4%E6%B5%81%E5%8F%98%E9%A2%91%20%E8%90%BD%E5%9C%B0%E6%89%87%2CMIJIA%20%E7%B1%B3%E5%AE%B6%20BPL%20DS01DM%201X%20%E7%9B%B4%E6%B5%81%E5%8F%98%E9%A2%91%20%E8%90%BD%E5%9C%B0%E6%89%87; zdm_qd=%7B%22referrer%22%3A%22https%3A%2F%2Fwww.google.com%2F%22%7D; ad_date=5; ad_json_feed=%7B%7D; PHPSESSID=bfc6c25b8dd6073edcd23b29cfead036; _gid=GA1.2.1606269054.1557027083; bannerCounter=%5B%7B%22number%22%3A1%2C%22surplus%22%3A1%7D%2C%7B%22number%22%3A0%2C%22surplus%22%3A1%7D%2C%7B%22number%22%3A1%2C%22surplus%22%3A1%7D%2C%7B%22number%22%3A0%2C%22surplus%22%3A1%7D%2C%7B%22number%22%3A1%2C%22surplus%22%3A1%7D%2C%7B%22number%22%3A0%2C%22surplus%22%3A2%7D%5D; _zdmA.uid=ZDMA.1ZKqQVz-i.1557027988.2419200; Hm_lvt_9b7ac3d38f30fe89ff0b8a0546904e58=1555768351,1556721162,1556803204,1557028485; wt3_sid=%3B999768690672041; wt3_eid=%3B999768690672041%7C2153636961500530496%232155702850500230961; Hm_lpvt_9b7ac3d38f30fe89ff0b8a0546904e58=1557031319; _gat_UA-27058866-1=1"
	}
	a = requests.get(url,headers=header,verify=False)
	soup = BeautifulSoup(a.text,"lxml")

	info_image = soup.find(name="img",attrs={"itemprop":"image"})['src']
	info_title = soup.find(name="em",attrs={"itemprop":"name"}).text.strip()
	info_price = soup.find(name="span",attrs={"class":"red"}).text.strip()
	info_link = soup.find(name="div",attrs={"class":"buy"}).a['href']
	info_tags_raw  = soup.find_all(name="div",attrs={"class":"meta-tags"})
	info_detail_raw = soup.find_all(name="div",attrs={"class":"baoliao-block"})
	
	info_detail = ""
	info_tags = ""

	for d in info_detail_raw:
		if d.text.strip():
			info_detail += str(d.text.encode("utf8").strip())
	for info_tag in info_tags_raw:
		info_tags += str(info_tag.a.text.encode("utf8").strip())+","

	return [
		info_title,
		info_image,
		info_price,
		info_link,
		info_detail,
		info_tags
	]

def save_item_info(infos):
	for i in infos:
		print type(i)
	sql = "insert into infos(info_title,info_image,info_price,info_link,info_detail,info_tags) values(%s,%s,%s,%s,%s,%s)"
	print sql
	print " sdfa"
	mysql_conn.execute(sql,infos[0],infos[1],infos[2],infos[3],infos[4],infos[5])


if __name__ == '__main__':
	to_do = url_generator(13693500,2000)
	for t in to_do:
		try:
			print save_item_info(get_single_item_infos(t))
			print "complete"
		except:
			pass
