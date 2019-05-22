
import MySQLdb
from pprint import pprint
host="192.168.199.209"
user="songqin"
passwd ="songqin"
dbname="plesson"
connection = MySQLdb.connect(host=host,
                        user=user,
                        passwd=passwd,
                        db=dbname,
                        charset="utf8")
c=connection.cursor()

c.execute(f"select * from sq_teacher")

pprint(c)
connection.commit()
