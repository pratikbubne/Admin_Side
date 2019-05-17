#!C:/python37/python
import mysql.connector
import cgi
conn = mysql.connector.connect(host='localhost', database='test1', user='root', password='')
c = conn.cursor()
form = cgi.FieldStorage()
hnm = str(form.getvalue('htl_name'))
hty = str(form.getvalue('htl_type'))
hcd = str(form.getvalue('htl_code'))
hcy = str(form.getvalue('htl_city'))

sql1 = "INSERT INTO adminaddhotel (h_name, h_type, h_code, h_city) VALUES ('%s','%s','%s','%s') " % (hnm, hty, hcd, hcy)
c.execute(sql1)
conn.commit()
c.close()
print("Content-type: text/html\r\n\r\n")
print("<script>window.location.href = 'AdminHead.html';window.alert('Hotel Registation Successfully....!')</script>")
