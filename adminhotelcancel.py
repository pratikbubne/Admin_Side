#!C:/Python37/python
import mysql.connector
import cgi
conn = mysql.connector.connect(host='localhost', database='test1', user='root', password='')
c = conn.cursor()
form = cgi.FieldStorage()
hnm = str(form.getvalue('h_name'))
hcd = str(form.getvalue('h_code'))
sql = "select (h_name, h_code) from adminaddhotel"
c.execute(sql)
conn.commit()
sql1 = "delete"
c.close()
print("Content-type: text/html\r\n\r\n")
print("<script>window.location.href = 'HotelCancel.html';window.alert('Request Send Succesfully...')</script>")