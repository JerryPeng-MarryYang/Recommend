import pymysql
conn = pymysql.connect(host='127.0.0.1', user='root', passwd='1234567', db='MovieData')
cur = conn.cursor()
# cur.execute('SELECT * FROM user')
# print(cur.fetchall())
# cur.close()
# conn.close()
for i in range(1, 672):
    cur.execute("INSERT INTO user(user, passwd) VALUES (\"%s\", \"%s\")", (i, 1))
    cur.connection.commit()
cur.close()
conn.close()