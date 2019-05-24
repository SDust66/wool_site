import torndb
import redis

mysql_conn = torndb.Connection("10.245.146.207:3306","wool",user="campuswool",password="campuswool",charset="utf8")
redis_conn = redis.Redis(host='10.245.146.207', port=6379)


sql = "DELETE FROM tags_count;"
mysql_conn.execute(sql)

sql = "SELECT info_tags FROM infos "
tagss = mysql_conn.query(sql)

total_dict = {}
for tags in tagss:
	if tags['info_tags']:
		real_tags = tags['info_tags'].split(",")
		for tag in real_tags:
			if tag:
				print tag
				if tag not in total_dict:
					total_dict[tag] = 1
				else:
					total_dict[tag] += 1
for k,v in total_dict.items():
	sql = "INSERT INTO tags_count(info_tag,info_count) VALUES(%s,%s)"
	mysql_conn.execute(sql,k,v)
