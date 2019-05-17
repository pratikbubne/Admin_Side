#!C:/Python37/python
import mysql.connector
import cgi
conn = mysql.connector.connect(host='localhost', database='test1', user='root', password='')
c = conn.cursor()
form = cgi.FieldStorage()
sql1 = "select * from hotelregister"
c.execute(sql1)
row = c.fetchall()
print("Content-type: text/html\r\n\r\n")
print("<!DOCTYPE html>")
print("<html>")
print("<head>")
print("<link rel='stylesheet' href='style.css'>")
print("</head>")
print("<body class='rhr'>")
print("<label class='head1'>Request For Hotel Register</label>")
print("<table  border='1' class='border'>")
print("<tr><th>ID</th><th>Owner Name</th><th width='150px'>Owner Mobile</th><th>Owner Mail</th></th><th>Hotel Name</th><th>Hotel type</th><th>Hotel Hotel Address</th><th>Hotel City</th></tr>")
for i in row:
    print("<tr><td>%s</td><td>%s</td><td>%s</td><td>%s</td><td>%s</td><td>%s</td><td>%s</td><td>%s</td><tr>" % (i[0], i[1], i[2],i[3],i[4], i[5], i[6], i[7]))
print("</table>")
print("</body>")
print("</html>")
conn.commit()
c.close()