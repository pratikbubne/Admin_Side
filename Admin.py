#!C:/Python37/python
import mysql.connector
import cgi
conn = mysql.connector.connect(host='localhost', database='test1', user='root', password='')
c = conn.cursor()
form = cgi.FieldStorage()
anm = str(form.getvalue('a_name'))
apd = str(form.getvalue('a_pwd'))
sql = "select admin_name,paswd from adminlogin where admin_name='%s'"%(anm)
c.execute(sql)
row = c.fetchone()
print("Content-type: text/html\r\n\r\n")
if row[0] == anm and row[1] == apd:
    print("<script>window.location.href = 'AdminHead.html';window.alert('Welcome Admin..!')</script>")
else:
    print("<script>window.location.href = 'index.html';window.alert('Admin User id or Password is wrong..! ')</script>")
    c.close()

