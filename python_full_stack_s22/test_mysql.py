import pymysql

# connection = pymysql.connect(host="127.0.0.1",
#                      user="root",
#                      password="use_MySQL59",
#                      db="test_pymysql")


# try:
#     with connection.cursor() as cursor:
#         # Create a new record
#         sql = "INSERT INTO 'employee' ('first_name', 'last_name', 'age', 'sex', 'income') VALUES (%s, %s, %d, %s, %d)"
#         cursor.execute(sql, ('ryan', 'oligen', 30, 'male', 30000))

#     # connection is not autocommit by default. So you must commit to save
#     # your changes.
#     connection.commit()

#     with connection.cursor() as cursor:
#         # Read a single record
#         sql = "SELECT * FROM employee WHERE 'sex'=%s"
#         cursor.execute(sql, ('male',))
#         result = cursor.fetchone()
#         print(result)
# finally:
#     connection.close()



# connection = pymysql.connect(host="127.0.0.1",
#                      user="root",
#                      password="use_MySQL59",
#                      db="sql_invoicing")

# with connection.cursor() as cursor:
#     sql = "SELECT name, sum(invoice_total) total_invoice FROM clients join invoices using(client_id) GROUP BY name;" 
#     cursor.execute(sql)
#     for record in cursor.fetchall():
#         print(record)
# connection.close()

addr = '127.0.0.1'
print('Connection from %s:%s closed.' % addr)