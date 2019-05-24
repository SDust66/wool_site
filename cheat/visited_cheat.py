import torndb
import random

mysql_conn = torndb.Connection("10.245.146.207:3306","wool",user="campuswool",password="campuswool",charset="utf8")

info_ids = mysql_conn.query("SELECT info_id from infos_comment")

for info_id in info_ids:
	a,b,c = random.randint(1,49),random.randint(1,49),random.randint(1,49)

	mysql_conn.execute("update infos_comment set info_visited=%s where info_id=%s",str(a*b*c),info_id['info_id'])